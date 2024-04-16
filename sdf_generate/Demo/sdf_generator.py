import os

from sdf_generate.Module.sdf_generator import SDFGenerator


def demo():
    if False:
        HOME = os.environ["HOME"]

        shape_root_folder_path = HOME + "/chLi/Dataset/ShapeNet/Core/ShapeNetCore.v2/"
        save_root_folder_path = HOME + "/Dataset/SDF/ShapeNet/"
        force_start = False
        resolution = 256
        scale_ratio = 1.0
        sample_point_num = 250000
        gauss_scale = 0.25

        sdf_generator = SDFGenerator(
            shape_root_folder_path,
            save_root_folder_path,
            force_start,
            resolution,
            scale_ratio,
            sample_point_num,
            gauss_scale,
        )

        sdf_generator.convertAll()

    if True:
        shape_root_folder_path = "../../ASDF/ma-sh/output/"
        save_root_folder_path = "./output/"
        force_start = False
        resolution = 256
        scale_ratio = 1.0
        sample_point_num = 250000
        gauss_scale = 0.25

        sdf_generator = SDFGenerator(
            shape_root_folder_path,
            save_root_folder_path,
            force_start,
            resolution,
            scale_ratio,
            sample_point_num,
            gauss_scale,
        )

        sdf_generator.convertOneShape("mac_chair_2.ply")

    return True
