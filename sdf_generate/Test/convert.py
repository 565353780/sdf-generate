import numpy as np
import open3d as o3d

from sdf_generate.Method.to_manifold import toManifold
from sdf_generate.Method.sample_sdf import convertSDFNearSurface
from sdf_generate.Method.render import toNearSurfaceSDFPcd


def test():
    mesh_file_path = "/home/chli/chLi/Dataset/ShapeNet/Core/ShapeNetCore.v2/02691156/1026dd1b26120799107f68a9cb8e3c/models/model_normalized.obj"
    manifold_file_path = "./output/test_manifold.obj"
    sdf_npy_file_path = "./output/test_sdf.npy"
    sample_point_num = 250000
    gauss_scale = 0.25
    overwrite = True

    if False:
        toManifold(mesh_file_path, manifold_file_path, overwrite)

    if True:
        convertSDFNearSurface(
            manifold_file_path,
            sdf_npy_file_path,
            sample_point_num,
            gauss_scale,
            overwrite,
        )

    sdf_data = np.load(sdf_npy_file_path)

    sdf_pcd = toNearSurfaceSDFPcd(sdf_data)

    o3d.io.write_point_cloud("./output/test_sdf_pcd.ply", sdf_pcd)
    return True
