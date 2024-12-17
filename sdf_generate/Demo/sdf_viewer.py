import numpy as np
import open3d as o3d

from sdf_generate.Method.render import toNearSurfaceSDFPcd
from sdf_generate.Module.sdf_viewer import SDFViewer


def demo():
    sdf_npy_file_path = "/home/chli/chLi/Dataset/Objaverse_82K/sdf_0_0025/000-001/112c059282cf4511a01fd27211edcae8.npy"
    manifold_file_path = '/home/chli/chLi/Dataset/Objaverse_82K/manifold/000-001/112c059282cf4511a01fd27211edcae8.obj'

    sdf_data = np.load(sdf_npy_file_path)
    sdf_pcd = toNearSurfaceSDFPcd(sdf_data)

    manifold_mesh = o3d.io.read_triangle_mesh(manifold_file_path)
    o3d.visualization.draw_geometries([sdf_pcd, manifold_mesh])

    return True

    sdf_viewer = SDFViewer()
    sdf_viewer.renderNearSurfaceSDFFile(sdf_npy_file_path)

    return True
