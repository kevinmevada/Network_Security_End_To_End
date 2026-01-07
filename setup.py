from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != HYPHEN_E_DOT:
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_list


setup(
    name="Network_Security",
    version="0.0.1",
    author="Kevin Mevada",
    author_email="mevadakevin@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
