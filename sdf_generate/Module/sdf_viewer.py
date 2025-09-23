import os
import numpy as np
import open3d as o3d

from sdf_generate.Method.render import getPcd


class SDFViewer(object):
    def __init__(
        self,
        dataset_root_folder_path: str,
        manifold_folder_name: str,
        sharp_edge_sdf_folder_name: str,
    ) -> None:
        self.dataset_root_folder_path = dataset_root_folder_path
        self.manifold_folder_name = manifold_folder_name
        self.sharp_edge_sdf_folder_name = sharp_edge_sdf_folder_name

        self.manifold_folder_path = (
            self.dataset_root_folder_path + self.manifold_folder_name + "/"
        )
        self.sharp_edge_sdf_folder_path = (
            self.dataset_root_folder_path + self.sharp_edge_sdf_folder_name + "/"
        )
        return

    def renderSDF(self) -> bool:
        for root, _, files in os.walk(self.manifold_folder_path):
            for file in files:
                if not file.endswith(".obj"):
                    continue

                rel_file_basepath = (
                    os.path.relpath(root, self.manifold_folder_path) + "/"
                )

                file_id = file.split(".")[0]

                manifold_mesh_file_path = (
                    self.manifold_folder_path + rel_file_basepath + "/" + file
                )

                sample_sdf_file_path = (
                    self.sharp_edge_sdf_folder_path
                    + rel_file_basepath
                    + "/"
                    + file_id
                    + ".npz"
                )

                if not os.path.exists(manifold_mesh_file_path):
                    continue
                if not os.path.exists(sample_sdf_file_path):
                    continue

                manifold_mesh = o3d.io.read_triangle_mesh(manifold_mesh_file_path)
                manifold_mesh.compute_vertex_normals()

                sample_sdf_data = np.load(sample_sdf_file_path)

                sample_sdf_dict = {
                    key: sample_sdf_data[key] for key in sample_sdf_data.files
                }

                for key, item in sample_sdf_dict.items():
                    print(f"{key}: {item.shape}, {item.dtype}")

                fps_sharp_surface = sample_sdf_dict["fps_sharp_surface"]
                sharp_near_surface = sample_sdf_dict["sharp_near_surface"]
                fps_coarse_surface = sample_sdf_dict["fps_coarse_surface"]
                rand_points = sample_sdf_dict["rand_points"]

                fps_sharp_surface_pcd = getPcd(
                    fps_sharp_surface[:, 0, :3],
                    fps_sharp_surface[:, 0, 3:],
                )

                sharp_near_surface_pcd = getPcd(sharp_near_surface[:, :3])

                fps_coarse_surface_pcd = getPcd(
                    fps_coarse_surface[:, 0, :3],
                    fps_coarse_surface[:, 0, 3:],
                )

                rand_points_pcd = getPcd(rand_points[:, :3])

                fps_sharp_surface_pcd.translate([2.5, 0, 0])

                sharp_near_surface_pcd.translate([5.0, 0, 0])

                fps_coarse_surface_pcd.translate([7.5, 0, 0])

                rand_points_pcd.translate([10.0, 0, 0])

                o3d.visualization.draw_geometries(
                    [
                        manifold_mesh,
                        fps_sharp_surface_pcd,
                        sharp_near_surface_pcd,
                        fps_coarse_surface_pcd,
                        rand_points_pcd,
                    ]
                )
        return True
