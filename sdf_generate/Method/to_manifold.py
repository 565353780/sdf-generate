import os

from sdf_generate.Method.path import createFileFolder


def runCMD(command: str) -> bool:
    os.system(command)
    return True

def toManifold(
    mesh_file_path: str, save_manifold_mesh_file_path: str, depth: int = 8, overwrite: bool = False
):
    if os.path.exists(save_manifold_mesh_file_path):
        if not overwrite:
            return True

    createFileFolder(save_manifold_mesh_file_path)

    command = "../sdf-generate/sdf_generate/Lib/ManifoldPlus/build/manifold" + \
        " --input " + mesh_file_path + \
        " --output " + save_manifold_mesh_file_path + \
        " --depth " + str(depth)

    try:
        if not runCMD(command):
            print("[ERROR][to_manifold::toManifold]")
            print("\t runCMD failed!")
            print('\t command:', command)
            return False
    except:
        print("[ERROR][to_manifold::toManifold]")
        print("\t runCMD ExceptionError found!")
        print('\t command:', command)
        return False

    return True
