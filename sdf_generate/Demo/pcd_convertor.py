import sys

sys.path.append("../data-convert")

import os

from sdf_generate.Module.uniform_pcd_convertor import PcdConvertor


def demo():
    HOME = os.environ["HOME"]

    dataset_root_folder_path = HOME + "/chLi/Dataset/Objaverse_82K/"
    gt_point_num = 250000

    pcd_convertor = PcdConvertor(
        dataset_root_folder_path + "normalized_manifold_mesh/",
        dataset_root_folder_path + "pcd_" + str(gt_point_num) + "/",
    )

    pcd_convertor.convertAll(".obj", ".ply")
    return True
