from setuptools import setup, find_packages
from os.path import dirname, join, realpath
from textwrap import dedent

PROJECT_ROOT = dirname(realpath(__file__))
REQUIREMENTS_FILE = join(PROJECT_ROOT, "requirements.txt")

with open(REQUIREMENTS_FILE) as f:
    install_reqs = f.read().splitlines()

install_reqs.append("setuptools")

setup(
    name='highdimensional_boundary',
    version='1.0.0',
    author='Tamas Madl',
    packages=find_packages(),
    install_requires=install_reqs,
)
