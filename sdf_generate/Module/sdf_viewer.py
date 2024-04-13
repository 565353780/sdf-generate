import os
import numpy as np
import open3d as o3d

from sdf_generate.Method.render import toSDFMesh, toNearSurfaceSDFPcd


class SDFViewer(object):
    def __init__(self) -> None:
        return

    def renderSDF(self, sdf_data: np.ndarray) -> bool:
        sdf_mesh = toSDFMesh(sdf_data)
        o3d.visualization.draw_geometries([sdf_mesh])
        return True

    def renderSDFFile(self, sdf_npy_file_path: str) -> bool:
        if not os.path.exists(sdf_npy_file_path):
            print("[ERROR][SDFViewer::renderSDFFile]")
            print("\t sdf npy file not exist!")
            print("\t sdf_npy_file_path:", sdf_npy_file_path)
            return False

        sdf_data = np.load(sdf_npy_file_path)

        if not self.renderSDF(sdf_data):
            print("[ERROR][SDFViewer::renderSDFFile]")
            print("\t renderSDF failed!")
            return False

        return True

    def renderNearSurfaceSDF(self, sdf_data: np.ndarray) -> bool:
        sdf_pcd = toNearSurfaceSDFPcd(sdf_data)
        o3d.visualization.draw_geometries([sdf_pcd])
        return True

    def renderNearSurfaceSDFFile(self, sdf_npy_file_path: str) -> bool:
        if not os.path.exists(sdf_npy_file_path):
            print("[ERROR][SDFViewer::renderNearSurfaceSDFFile]")
            print("\t sdf npy file not exist!")
            print("\t sdf_npy_file_path:", sdf_npy_file_path)
            return False

        sdf_data = np.load(sdf_npy_file_path)

        if not self.renderNearSurfaceSDF(sdf_data):
            print("[ERROR][SDFViewer::renderNearSurfaceSDFFile]")
            print("\t renderNearSurfaceSDF failed!")
            return False

        return True
