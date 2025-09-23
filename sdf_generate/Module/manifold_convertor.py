from data_convert.Module.base_convertor import BaseConvertor

from sdf_generate.Method.to_manifold import toManifold


class ManifoldConvertor(BaseConvertor):
    def __init__(
        self,
        source_root_folder_path: str,
        target_root_folder_path: str,
        depth: int = 8,
    ) -> None:
        super().__init__(source_root_folder_path, target_root_folder_path)

        self.depth = depth
        return

    def convertData(self, source_path: str, target_path: str) -> bool:
        toManifold(source_path, target_path, self.depth, True)
        return True
