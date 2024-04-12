from shutil import copyfile

from sdf_generate.Module.sdf_viewer import SDFViewer


def demo():
    sdf_npy_file_path = "/home/chli/chLi/Dataset/SDF/ShapeNet/sdf/02691156/1026dd1b26120799107f68a9cb8e3c/models/model_normalized_obj.npy"

    sdf_viewer = SDFViewer()
    sdf_viewer.renderNearSurfaceSDFFile(sdf_npy_file_path)

    mesh_file_path = "/home/chli/chLi/Dataset/ShapeNet/Core/ShapeNetCore.v2/02691156/1026dd1b26120799107f68a9cb8e3c/models/model_normalized.obj"
    manifold_file_path = "/home/chli/chLi/Dataset/SDF/ShapeNet/manifold/02691156/1026dd1b26120799107f68a9cb8e3c/models/model_normalized_obj.obj"
    copyfile(mesh_file_path, "./output/test_mesh.obj")
    copyfile(manifold_file_path, "./output/test_manifold.obj")
    return True
