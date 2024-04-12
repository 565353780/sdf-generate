from sdf_generate.Module.sdf_viewer import SDFViewer


def demo():
    sdf_npy_file_path = "/home/chli/chLi/Dataset/SDF/ShapeNet/sdf/02691156/1026dd1b26120799107f68a9cb8e3c/models/model_normalized_obj.npy"

    sdf_viewer = SDFViewer()
    sdf_viewer.renderNearSurfaceSDFFile(sdf_npy_file_path)
    return True
