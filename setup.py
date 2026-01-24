"""
setup.py is used for packaging and distributing Python projects.
It defines project metadata and dependencies.
"""
from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    try:
        with open("requirements.txt") as f:
            return [line.strip() for line in f if line.strip() and line.strip() != "-e ."]
    except FileNotFoundError:
        return []

setup(
    name="network_Security",
    version="0.1",
    author="Kevin Mevada",
    author_email="kmevada@hawk.illinoistech.edu",
    packages= find_packages(),
    install_requires= get_requirements()
)