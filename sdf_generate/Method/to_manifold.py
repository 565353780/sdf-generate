import os
from typing import Union
from subprocess import Popen, PIPE

from sdf_generate.Method.path import createFileFolder


def runCMD(cmd: Union[str, list]) -> bool:
    if isinstance(cmd, list):
        cmd_str = ""
        for i in range(len(cmd) - 1):
            cmd_str += cmd[i] + " "
        cmd_str += cmd[-1]
    else:
        cmd_str = cmd
    os.system(cmd_str)
    return True
    subproc = Popen(cmd, stdout=PIPE)
    subproc.wait()
    return True


def toManifold(
    mesh_file_path: str, save_manifold_mesh_file_path: str, overwrite: bool = False
):
    if os.path.exists(save_manifold_mesh_file_path):
        if not overwrite:
            return True

    createFileFolder(save_manifold_mesh_file_path)

    cmd = [
        "../sdf-generate/sdf_generate/Lib/Manifold/build/manifold",
        mesh_file_path,
        save_manifold_mesh_file_path,
    ]

    try:
        if not runCMD(cmd):
            print("[ERROR][to_manifold::toManifold]")
            print("\t runCMD failed!")
            return False
    except:
        print("[ERROR][to_manifold::toManifold]")
        print("\t runCMD failed!")
        return False

    return True
