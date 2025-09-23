import torch

from data_convert.Module.base_convertor import BaseConvertor

from sdf_generate.Lib.sharp_edge_sampling.to_watertight_mesh import (
    generate_dense_grid_points,
    remesh,
)


class WatertightConvertor(BaseConvertor):
    def __init__(
        self,
        source_root_folder_path: str,
        target_root_folder_path: str,
        resolution: int = 4096,
        use_pcu: bool = True,
    ) -> None:
        super().__init__(source_root_folder_path, target_root_folder_path)

        self.resolution = resolution
        self.use_pcu = use_pcu

        self.grid_xyz, self.grid_size = generate_dense_grid_points(
            resolution=resolution
        )
        if use_pcu:
            self.grid_xyz = self.grid_xyz.astype(float)
        else:
            self.grid_xyz = torch.FloatTensor(self.grid_xyz).cuda()
        return

    def convertData(self, source_path: str, target_path: str) -> bool:
        try:
            remesh(
                self.grid_xyz,
                self.grid_size,
                source_path,
                target_path,
                self.resolution,
                self.use_pcu,
            )
            torch.cuda.empty_cache()
        except Exception as e:
            print(f"ERROR: in processing path: {source_path}. Error: {e}")
            torch.cuda.empty_cache()
        return True
