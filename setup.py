from setuptools import setup
import sys
from os.path import abspath, join, dirname, realpath

def read_requirements_file(filename):
    req_file_path = '%s/%s' % (dirname(realpath(__file__)), filename)
    with open(req_file_path) as f:
        return [line.strip() for line in f]
setup(name='pypurl',
      version='0.0.1',
      python_requires='>=3.5',
      install_requires=read_requirements_file('requirements.txt'),
      description='Implementation of an easy way of building and handling the Package URLs.',
      author='Victor Barbaros',
      url='https://github.com/vBarbaros/pypurl',
)
