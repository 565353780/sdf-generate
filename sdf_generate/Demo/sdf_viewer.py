from sdf_generate.Module.sdf_viewer import SDFViewer


def demo():
    dataset_root_folder_path = "/home/chli/chLi/Dataset/Objaverse_82K/"
    manifold_folder_name = "manifold"
    sharp_edge_sample_folder_name = "sharp_edge_sdf"

    sdf_viewer = SDFViewer(
        dataset_root_folder_path,
        manifold_folder_name,
        sharp_edge_sample_folder_name,
    )

    sdf_viewer.renderSDF()
    return True
