from data_convert.Module.base_convertor import BaseConvertor

from sdf_generate.Method.sample_sdf import convertSDFNearSurface


class SDFConvertor(BaseConvertor):
    def __init__(
        self,
        source_root_folder_path: str,
        target_root_folder_path: str,
        sample_point_num: int = 250000,
        gauss_scale: float = 0.0025,
    ) -> None:
        super().__init__(source_root_folder_path, target_root_folder_path)

        self.sample_point_num = sample_point_num
        self.gauss_scale = gauss_scale
        return

    def convertData(self, source_path: str, target_path: str) -> bool:
        convertSDFNearSurface(
            source_path,
            target_path,
            self.sample_point_num,
            self.gauss_scale,
            True,
        )
        return True
