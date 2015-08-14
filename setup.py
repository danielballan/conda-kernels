import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='conda_kernels',
      version='0.0.1',
      author='Daniel B. Allan',
      author_email='daniel.b.allan@gmail.com',
      py_modules=['conda_kernels'],
      description='Use conda environments as Jupyter kernels',
      url='http://github.com/danielballan/conda-kernels',
      install_requires=['jupyter_client > 4.0.0'],
      platforms='Cross platform (Linux, Mac OSX, Windows)',
      license="BSD",
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   ],
      long_description = read('README.md'),
      )
