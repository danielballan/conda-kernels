Inspect conda environments to automatically generate Jupyter kernels.

**WARNING: This is a work in progress, shared prematurely to solicit some help.
It has never operated successfully.**

As noted in the code, this is adapted from [this gist](https://gist.github.com/pelson/ca05c73f4027371f6de4) by Phil Elson (@pelson).

```
ipython notebook --NotebookApp.kernel_spec_manager_class=conda_kernels.CondaKernelSpecManager
```
