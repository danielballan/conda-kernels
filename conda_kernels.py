"""
Inspect list of conda environments to find Jupyter kernels.

Adapted from an IPython patch by Phil Elson, @pelson, in this gist:
https://gist.github.com/pelson/ca05c73f4027371f6de4
"""

import time
from traitlets import List, Unicode
import os
import subprocess
import json
from jupyter_client.kernelspec import KernelSpecManager, _list_kernels_in


# last-resort place to look for conda
ROOT_CONDA_PATH = '/opt/conda/bin/conda'


def conda_envs():
    # Get conda off the path.
    try:
        conda = subprocess.check_output(['which', 'conda']).strip()
    except subprocess.CalledProcessError:
        conda = ROOT_CONDA_PATH
    if not os.path.exists(conda):
        return []

    envs = subprocess.check_output([conda, 'env', 'list', '--json']).decode()

    envs = json.loads(envs)['envs']
    return [os.path.join(env, 'share', 'jupyter', 'kernels') for env in envs]


class CondaKernelSpecManager(KernelSpecManager):
    # Jupyter calls `find_kernel_specs` several times in quick succession,
    # and since conda is slow, we cache for 10 seconds.
    cache_last_updated = 0
    cache = {}

    def find_kernel_specs(self):
        """Returns a dict mapping kernel names to resource directories."""
        specs = super().find_kernel_specs()
        if time.time() - self.cache_last_updated > 10:
            self.cache.clear()
            # Dynamically update the potential kernel directories.
            for kernel_dir in set(conda_envs()):
                self.cache.update(_list_kernels_in(kernel_dir))
            self.cache_last_updated = time.time()
        specs.update(self.cache)
        return specs
