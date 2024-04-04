import os
import numpy as np
import open3d as o3d
from copy import deepcopy

from sdf_generate.Method.path import createFileFolder


def flipAxis(mesh_file_path: str, save_flip_axis_mesh_file_path: str, overwrite: bool = False) -> bool:

    if not os.path.exists(mesh_file_path):
        return False

    if os.path.exists(save_flip_axis_mesh_file_path):
        if not overwrite:
            return True

    createFileFolder(save_flip_axis_mesh_file_path)

    mesh = o3d.io.read_triangle_mesh(mesh_file_path)
    vertices = np.asarray(mesh.vertices)
    flip_axis_vertices = np.vstack((vertices[:, 2], vertices[:, 1], -vertices[:, 0])).T

    flip_axis_mesh = deepcopy(mesh)
    flip_axis_mesh.vertices = o3d.utility.Vector3dVector(flip_axis_vertices)

    o3d.io.write_triangle_mesh(save_flip_axis_mesh_file_path, flip_axis_mesh)

    return True
