import sys

sys.path.append("../data-convert")

import os

from data_convert.Module.pipeline_convertor import PipelineConvertor

from sdf_generate.Module.manifold_convertor_v2 import ManifoldConvertorV2
from sdf_generate.Module.sharp_edge_pcd_convertor import SharpEdgePcdConvertor


def demo():
    HOME = os.environ["HOME"]

    dataset_root_folder_path = HOME + "/chLi/Dataset/Objaverse_82K/"
    resolution = 512
    use_pcu = False
    angle_threshold = 15.0
    point_number = 32768

    pipeline_convertor = PipelineConvertor()

    convertor_list = [
        ManifoldConvertorV2(
            dataset_root_folder_path + "glbs/",
            dataset_root_folder_path + "manifold/",
            resolution,
            use_pcu,
        ),
        SharpEdgePcdConvertor(
            dataset_root_folder_path + "manifold/",
            dataset_root_folder_path + "sharp_edge_sample/",
            angle_threshold,
            point_number,
        ),
    ]

    data_type_list = [
        ".glb",
        ".obj",
        "/",
    ]

    pipeline_convertor = PipelineConvertor(convertor_list)

    pipeline_convertor.convertAll(data_type_list)
    return True
