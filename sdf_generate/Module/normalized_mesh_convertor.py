import trimesh
import numpy as np

from data_convert.Module.base_convertor import BaseConvertor


class NormalizedMeshConvertor(BaseConvertor):
    def __init__(
        self,
        source_root_folder_path: str,
        target_root_folder_path: str,
        scale: float = 0.99,
    ) -> None:
        super().__init__(source_root_folder_path, target_root_folder_path)

        self.scale = scale
        return

    def convertData(self, source_path: str, target_path: str) -> bool:
        mesh = trimesh.load(source_path)

        min_bound = np.min(mesh.vertices, axis=0)
        max_bound = np.max(mesh.vertices, axis=0)
        length = np.max(max_bound - min_bound)
        scale = self.scale / length
        center = (min_bound + max_bound) / 2.0

        mesh.vertices = (mesh.vertices - center) * scale

        mesh.export(target_path)
        return True
