import sys

sys.path.append("../data-convert")

import os

from data_convert.Module.pipeline_convertor import PipelineConvertor

from sdf_generate.Module.watertight_convertor import WatertightConvertor
from sdf_generate.Module.sharp_edge_sdf_convertor import SharpEdgeSDFConvertor


def demo():
    HOME = os.environ["HOME"]

    dataset_root_folder_path = HOME + "/chLi/Dataset/Objaverse_82K/"
    resolution = 512
    use_pcu = False
    angle_threshold = 15.0
    point_number = 32768

    pipeline_convertor = PipelineConvertor()

    convertor_list = [
        WatertightConvertor(
            dataset_root_folder_path + "glbs/",
            dataset_root_folder_path + "manifold/",
            resolution,
            use_pcu,
        ),
        SharpEdgeSDFConvertor(
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
