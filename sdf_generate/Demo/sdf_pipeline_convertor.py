import sys

sys.path.append("../data-convert")

import os

from data_convert.Module.pipeline_convertor import PipelineConvertor

from sdf_generate.Module.single_mesh_convertor import SingleMeshConvertor
from sdf_generate.Module.normalized_mesh_convertor import NormalizedMeshConvertor
from sdf_generate.Module.manifold_convertor import ManifoldConvertor
from sdf_generate.Module.sdf_convertor import SDFConvertor


def demo():
    HOME = os.environ["HOME"]

    dataset_root_folder_path = HOME + "/chLi/Dataset/Objaverse_82K/"
    include_texture = False
    scale = 0.99
    depth = 8
    sample_point_num = 250000
    gauss_scale = 0.0025

    pipeline_convertor = PipelineConvertor()

    convertor_list = [
        SingleMeshConvertor(
            dataset_root_folder_path + "glbs/",
            dataset_root_folder_path + "single_mesh/",
            include_texture,
        ),
        NormalizedMeshConvertor(
            dataset_root_folder_path + "single_mesh/",
            dataset_root_folder_path + "normalized_mesh/",
            scale,
        ),
        ManifoldConvertor(
            dataset_root_folder_path + "normalized_mesh/",
            dataset_root_folder_path + "normalized_manifold_mesh/",
            depth,
        ),
        SDFConvertor(
            dataset_root_folder_path + "normalized_manifold_mesh/",
            dataset_root_folder_path
            + "sdf_"
            + str(gauss_scale).replace(".", "_")
            + "/",
            sample_point_num,
            gauss_scale,
        ),
    ]

    data_type_list = [
        ".glb",
        ".obj",
        ".obj",
        ".obj",
        ".npy",
    ]

    pipeline_convertor = PipelineConvertor(convertor_list)

    pipeline_convertor.convertAll(data_type_list)
    return True
