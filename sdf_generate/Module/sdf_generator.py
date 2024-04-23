import os

from sdf_generate.Method.path import createFileFolder
from sdf_generate.Method.flip_axis import flipAxis
from sdf_generate.Method.to_manifold import toManifold
from sdf_generate.Method.sample_sdf import convertSDFGrid, convertSDFNearSurface


class SDFGenerator(object):
    def __init__(
        self,
        shape_root_folder_path: str,
        dataset_root_folder_path: str,
        force_start: bool = False,
        resolution: int = 256,
        scale_ratio: float = 1.0,
        sample_point_num: int = 250000,
        gauss_scale: float = 0.0025,
    ) -> None:
        self.shape_root_folder_path = shape_root_folder_path
        self.dataset_root_folder_path = dataset_root_folder_path
        self.force_start = force_start
        self.resolution = resolution
        self.scale_ratio = scale_ratio
        self.sample_point_num = sample_point_num
        self.gauss_scale = gauss_scale

        self.manifold_folder_path = (
            self.shape_root_folder_path + "Manifold/ShapeNet/manifold/"
        )
        self.manifold_folder_path = (
            self.dataset_root_folder_path + "Mash/ShapeNet/normalized_mesh/"
        )
        self.sdf_folder_path = self.dataset_root_folder_path + "SDF/ShapeNet/"
        return

    def convertOneShape(self, rel_shape_file_path: str) -> bool:
        shape_file_name = rel_shape_file_path.split("/")[-1]

        rel_shape_folder_path = rel_shape_file_path.split(shape_file_name)[0]

        shape_file_path = self.shape_root_folder_path + rel_shape_file_path

        if not os.path.exists(shape_file_path):
            print("[ERROR][SDFGenerator::convertOneShape]")
            print("\t shape file not exist!")
            print("\t shape_file_path:", shape_file_path)
            return False

        unit_rel_folder_path = rel_shape_folder_path + shape_file_name.replace(".", "_")

        finish_tag_file_path = (
            self.sdf_folder_path + "tag/" + unit_rel_folder_path + "/finish.txt"
        )

        if os.path.exists(finish_tag_file_path):
            return True

        start_tag_file_path = (
            self.sdf_folder_path + "tag/" + unit_rel_folder_path + "/start.txt"
        )

        if os.path.exists(start_tag_file_path):
            if not self.force_start:
                return True

        createFileFolder(start_tag_file_path)

        with open(start_tag_file_path, "w") as f:
            f.write("\n")

        if False:
            flip_axis_shape_file_path = (
                self.dataset_root_folder_path
                + "flip_axis/"
                + unit_rel_folder_path
                + shape_file_name
            )
            flipAxis(shape_file_path, flip_axis_shape_file_path, True)

        manifold_shape_file_path = (
            self.manifold_folder_path + unit_rel_folder_path.replace("_obj", ".obj")
        )

        if not os.path.exists(manifold_shape_file_path):
            createFileFolder(manifold_shape_file_path)
            toManifold(shape_file_path, manifold_shape_file_path, True)

        if False:
            save_sdf_npy_file_path = (
                self.dataset_root_folder_path + "sdf/" + unit_rel_folder_path + ".npy"
            )
            convertSDFGrid(
                manifold_shape_file_path,
                save_sdf_npy_file_path,
                self.resolution,
                self.scale_ratio,
                True,
            )

        save_sdf_npy_file_path = (
            self.sdf_folder_path + "sdf/" + unit_rel_folder_path + ".npy"
        )
        if not os.path.exists(save_sdf_npy_file_path):
            convertSDFNearSurface(
                manifold_shape_file_path,
                save_sdf_npy_file_path,
                self.sample_point_num,
                self.gauss_scale,
                True,
            )

        with open(finish_tag_file_path, "w") as f:
            f.write("\n")

        return True

    def convertAll(self) -> bool:
        os.makedirs(self.dataset_root_folder_path, exist_ok=True)

        print("[INFO][Convertor::convertAll]")
        print("\t start convert all shapes to mashes...")
        solved_shape_num = 0
        for root, _, files in os.walk(self.shape_root_folder_path):
            for filename in files:
                if filename[-4:] != ".obj":
                    continue

                rel_file_path = (
                    root.split(self.shape_root_folder_path)[1] + "/" + filename
                )

                self.convertOneShape(rel_file_path)

                solved_shape_num += 1
                print("solved shape num:", solved_shape_num)

        return True
