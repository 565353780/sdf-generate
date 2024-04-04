import os
from typing import Union
from subprocess import Popen, PIPE

def runCMD(cmd: Union[str, list]) -> bool:
    subproc = Popen(cmd, stdout=PIPE)
    subproc.wait()
    return True

def toManifold(mesh_file_path: str, save_manifold_mesh_file_path: str, overwrite: bool=False):
    if os.path.exists(save_manifold_mesh_file_path):
        if not overwrite:
            return True

    cmd = '../sdf-generate/sdf_generate/Lib/Manifold/build/manifold ' + mesh_file_path + \
        ' ' + save_manifold_mesh_file_path

    if not runCMD(cmd):
        print('[ERROR][to_manifold::toManifold]')
        print('\t runCMD failed!')
        return False

    return True
