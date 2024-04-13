from sdf_generate.Method.to_manifold import toManifold
from sdf_generate.Method.sample_sdf import convertSDFNearSurface
from sdf_generate.Module.sdf_viewer import SDFViewer


def test():
    mesh_file_path = "/home/chli/chLi/Dataset/ShapeNet/Core/ShapeNetCore.v2/02691156/1026dd1b26120799107f68a9cb8e3c/models/model_normalized.obj"
    manifold_file_path = "./output/test_manifold.obj"
    sdf_npy_file_path = "./output/test_sdf.npy"

    if True:
        toManifold(mesh_file_path, manifold_file_path, True)

    if True:
        convertSDFNearSurface(
            manifold_file_path,
            sdf_npy_file_path,
            250000,
            True,
        )

    sdf_viewer = SDFViewer()
    sdf_viewer.renderNearSurfaceSDFFile(sdf_npy_file_path)
    return True
