import os

os.environ["PYOPENGL_PLATFORM"] = "egl"

import trimesh
import numpy as np
from mesh_to_sdf import mesh_to_voxels

from sdf_generate.Method.path import createFileFolder


def convertSDFGrid(
    manifold_mesh_file_path: str,
    save_sdf_npy_file_path: str,
    resolution: int = 256,
    scale_ratio: float = 1.0,
    overwrite: bool = False,
) -> bool:
    if os.path.exists(save_sdf_npy_file_path):
        if not overwrite:
            return True

    createFileFolder(save_sdf_npy_file_path)

    mesh = trimesh.load_mesh(manifold_mesh_file_path)
    voxels = mesh_to_voxels(mesh, resolution, scale_ratio=scale_ratio)

    np.save(save_sdf_npy_file_path, voxels)
    return True
