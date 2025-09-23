#  Copyright (c) 2024 Bytedance Ltd. and/or its affiliates
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  code builder: Dora team (https://github.com/Seed3D/Dora)
import torch
import cubvh
import trimesh
import numpy as np
from diso import DiffDMC
import point_cloud_utils as pcu


def generate_dense_grid_points(
    bbox_min=np.array((-1.05, -1.05, -1.05)),  # array([-1.05, -1.05, -1.05])
    bbox_max=np.array((1.05, 1.05, 1.05)),  # array([1.05, 1.05, 1.05])
    resolution=512,
    indexing="ij",
):
    length = bbox_max - bbox_min  # array([2.1, 2.1, 2.1])
    num_cells = resolution  # 512
    x = np.linspace(bbox_min[0], bbox_max[0], resolution + 1, dtype=np.float32)
    y = np.linspace(bbox_min[1], bbox_max[1], resolution + 1, dtype=np.float32)
    z = np.linspace(bbox_min[2], bbox_max[2], resolution + 1, dtype=np.float32)
    [xs, ys, zs] = np.meshgrid(x, y, z, indexing=indexing)
    xyz = np.stack((xs, ys, zs), axis=-1)
    xyz = xyz.reshape(-1, 3)  # 513*513*513，3
    grid_size = [resolution + 1, resolution + 1, resolution + 1]  # 513，513，513

    return xyz, grid_size


def remesh(grid_xyz, grid_size, mesh_path, remesh_path, resolution, use_pcu):
    eps = 2 / resolution
    mesh = trimesh.load(mesh_path, force="mesh")

    # normalize mesh to [-1,1]
    vertices = mesh.vertices
    bbmin = vertices.min(0)
    bbmax = vertices.max(0)
    center = (bbmin + bbmax) / 2
    scale = 2.0 / (bbmax - bbmin).max()
    vertices = (vertices - center) * scale
    if use_pcu:
        grid_sdf, fid, bc = pcu.signed_distance_to_mesh(
            grid_xyz, vertices.astype(np.float32), mesh.faces
        )
        grid_udf = (
            torch.FloatTensor(np.abs(grid_sdf))
            .cuda()
            .view((grid_size[0], grid_size[1], grid_size[2]))
        )
    else:
        f = cubvh.cuBVH(
            torch.as_tensor(vertices, dtype=torch.float32, device="cuda"),
            torch.as_tensor(mesh.faces, dtype=torch.float32, device="cuda"),
        )  # build with numpy.ndarray/torch.Tensor
        grid_udf, _, _ = f.unsigned_distance(grid_xyz, return_uvw=False)
        grid_udf = grid_udf.view((grid_size[0], grid_size[1], grid_size[2]))
    diffdmc = DiffDMC(dtype=torch.float32).cuda()
    vertices, faces = diffdmc(grid_udf, isovalue=eps, normalize=False)
    bbox_min = np.array((-1.05, -1.05, -1.05))
    bbox_max = np.array((1.05, 1.05, 1.05))
    bbox_size = bbox_max - bbox_min
    vertices = (vertices + 1) / grid_size[0] * bbox_size[0] + bbox_min[0]
    mesh = trimesh.Trimesh(vertices=vertices.cpu().numpy(), faces=faces.cpu().numpy())
    # keep the max component of the extracted mesh
    components = mesh.split(only_watertight=False)
    bbox = []
    for c in components:
        bbmin = c.vertices.min(0)
        bbmax = c.vertices.max(0)
        bbox.append((bbmax - bbmin).max())
    max_component = np.argmax(bbox)
    mesh = components[max_component]
    mesh.export(remesh_path)
