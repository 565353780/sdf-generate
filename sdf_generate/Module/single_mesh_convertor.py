import trimesh

from data_convert.Module.base_convertor import BaseConvertor


class SingleMeshConvertor(BaseConvertor):
    def __init__(
        self,
        source_root_folder_path: str,
        target_root_folder_path: str,
        include_texture: bool = False,
    ) -> None:
        super().__init__(source_root_folder_path, target_root_folder_path)

        self.include_texture = include_texture
        return

    def convertData(self, source_path: str, target_path: str) -> bool:
        try:
            mesh = trimesh.load(source_path)
        except KeyboardInterrupt:
            print("[INFO][SingleMeshConvertor::convertData]")
            print("\t program interrupted by the user (Ctrl+C).")
            exit()
        except:
            print("[ERROR][SingleMeshConvertor::convertData]")
            print("\t load mesh file failed!")
            print("\t source_path:", source_path)
            return False

        if isinstance(mesh, trimesh.Scene):
            sub_mesh_list = [
                geometry
                for geometry in mesh.geometry.values()
                if isinstance(geometry, trimesh.Trimesh)
            ]
            if len(sub_mesh_list) == 0:
                print("[ERROR][SingleMeshConvertor::convertData]")
                print("\t the mesh file contains no mesh!")
                print("\t source_path:", source_path)
                return False

            mesh = trimesh.util.concatenate(sub_mesh_list)

        mesh.export(target_path, include_texture=self.include_texture)
        return True
