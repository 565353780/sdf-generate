import os

from sdf_generate.Module.sdf_generator import SDFGenerator


def demo():
    HOME = os.environ["HOME"]

    shape_root_folder_path = HOME + "/chLi/Dataset/ShapeNet/Core/ShapeNetCore.v2/"
    save_root_folder_path = HOME + "/chLi/Dataset/SDF/ShapeNet/"
    force_start = False
    resolution = 256
    scale_ratio = 1.0
    sample_point_num = 250000

    sdf_generator = SDFGenerator(
        shape_root_folder_path,
        save_root_folder_path,
        force_start,
        resolution,
        scale_ratio,
        sample_point_num,
    )

    sdf_generator.convertAll()
    return True
