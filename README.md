Inspect conda environments to automatically generate Jupyter kernels.

As noted in the code, this is adapted from [this gist](https://gist.github.com/pelson/ca05c73f4027371f6de4) by Phil Elson (@pelson).

**This is designed to be used with the remotekernel project, and currently
it does not work without it. Making it work as a standalone would be
straightforward. Get in touch if you need this.**

To make a conda environment "discoverable" by Jupyter, run

```
conda install -n MY_ENV_NAME -c danieballan/kernelize
```

(The conda receipe for `kernelize` is included in this package, so you can
build it yourself and replace `danielballan` with your anaconda channel.)

Then, with conda-kernels installed, launch jupyter like so:

```
jupyter notebook --NotebookApp.kernel_spec_manager_class=conda_kernels.CondaKernelSpecManager
```
