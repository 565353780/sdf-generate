import gc
import math

from data_convert.Module.base_convertor import BaseConvertor

from sdf_generate.Lib.sharp_edge_sampling.sharp_sample import process_mesh


class SharpEdgeSDFConvertor(BaseConvertor):
    def __init__(
        self,
        source_root_folder_path: str,
        target_root_folder_path: str,
        angle_threshold: float = 15.0,
        point_number: int = 32768,
    ) -> None:
        super().__init__(source_root_folder_path, target_root_folder_path)

        self.angle_threshold = angle_threshold
        self.point_number = point_number

        self.sharpness_threshold = math.radians(angle_threshold)
        return

    def convertData(self, source_path: str, target_path: str) -> bool:
        try:
            process_mesh(
                source_path,
                self.point_number,
                target_path + "pcd.ply",
                target_path + "sdf.npz",
                self.sharpness_threshold,
            )
            gc.collect()
        except Exception as e:
            print(f"ERROR: in processing path: {source_path}. Error: {e}")
            gc.collect()
        return True
