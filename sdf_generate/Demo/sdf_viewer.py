from sdf_generate.Module.sdf_viewer import SDFViewer


def demo():
    sdf_npy_file_path = "./output/model_normalized_obj.npy"

    sdf_viewer = SDFViewer()
    sdf_viewer.renderSDFFile(sdf_npy_file_path)
    return True
