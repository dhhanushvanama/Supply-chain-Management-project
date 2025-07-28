from setuptools import find_packages, setup

from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
setup(
    name='supply chain management',
    author='Dhhanush',
    author_email='dhhanushvanama999@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
    )