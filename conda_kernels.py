"""
Inspect list of conda environments to find Jupyter kernels.

Adapted from an IPython patch by Phil Elson, @pelson, in this gist:
https://gist.github.com/pelson/ca05c73f4027371f6de4
"""

import glob
import os
import subprocess
import json
from jupyter_client.kernelspec import KernelSpecManager, _list_kernels_in


# last-resort place to look for conda
ROOT_CONDA_PATH = '/opt/miniconda/bin/conda'


def conda_envs():
    # Get conda off the path.
    try:
        conda = subprocess.check_output(['which', 'conda']).strip()
    except subprocess.CalledProcessError as e:
        conda = ROOT_CONDA_PATH
    if not os.path.exists(conda):
        return []

    envs = subprocess.check_output([conda, 'env', 'list', '--json']).decode()

    envs = json.loads(envs)['envs']
    return [os.path.join(env, 'share', 'jupyter', 'kernels') for env in envs]


# Put all centrally installed environments in the kernel path.
_CENTRAL_ENVS = '/opt/conda/envs/*/share/jupyter/kernels/'


class CondaKernelSpecManager(KernelSpecManager):

    def find_kernel_specs(self):
        """Returns a dict mapping kernel names to resource directories."""
        d = {}
        # Dynamically update the potential kernel directories.
        envs = conda_envs()
        self.kernel_dirs.extend(envs)
        self.kernel_dirs.extend(glob.glob(_CENTRAL_ENVS))
        for kernel_dir in set(self.kernel_dirs):
            d.update(_list_kernels_in(kernel_dir))

        return d
