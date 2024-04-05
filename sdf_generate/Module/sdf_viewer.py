import os
import skimage
import numpy as np
import open3d as o3d


class SDFViewer(object):
    def __init__(self) -> None:
        return

    def renderSDF(self, sdf_data: np.ndarray) -> bool:
        vertices, faces, normals, _ = skimage.measure.marching_cubes(sdf_data, level=0)
        mesh = o3d.geometry.TriangleMesh()
        mesh.vertices = o3d.utility.Vector3dVector(vertices)
        mesh.triangles = o3d.utility.Vector3iVector(faces)
        mesh.vertex_normals = o3d.utility.Vector3dVector(normals)
        o3d.visualization.draw_geometries([mesh])
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
