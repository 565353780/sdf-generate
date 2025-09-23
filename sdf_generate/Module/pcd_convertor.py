import open3d as o3d

from data_convert.Module.base_convertor import BaseConvertor


class PcdConvertor(BaseConvertor):
    def __init__(
        self,
        source_root_folder_path: str,
        target_root_folder_path: str,
        gt_points_num: int = 400000,
    ) -> None:
        super().__init__(source_root_folder_path, target_root_folder_path)

        self.gt_points_num = gt_points_num
        return

    def convertData(self, source_path: str, target_path: str) -> bool:
        mesh = o3d.io.read_triangle_mesh(source_path)

        pcd = mesh.sample_points_poisson_disk(self.gt_points_num)

        o3d.io.write_point_cloud(target_path, pcd, write_ascii=True)
        return True
