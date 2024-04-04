import os

from sdf_generate.Module.sdf_generator import SDFGenerator


def demo():
    HOME = os.environ["HOME"]

    shape_root_folder_path = HOME + "/chLi/Dataset/ShapeNet/Core/ShapeNetCore.v2/"
    save_root_folder_path = HOME + "/chLi/Dataset/SDF/ShapeNet/"
    force_start = False

    sdf_generator = SDFGenerator(
        shape_root_folder_path,
        save_root_folder_path,
        force_start,
    )

    sdf_generator.convertAll()
    return True
