import sys

sys.path.append("../data-convert")

import os

from data_convert.Method.tag import clearTag

if __name__ == "__main__":
    HOME = os.environ["HOME"]

    dataset_root_folder_path = HOME + "/chLi/Dataset/Objaverse_82K/"

    clearTag(dataset_root_folder_path + "manifold/")
    clearTag(dataset_root_folder_path + "sharp_edge_sdf/")
