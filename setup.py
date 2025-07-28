from setuptools import setup, find_packages

def requirements(filepath:str) -> list[str]:
    requirements = []
    with open(filepath, 'r') as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
setup(
    name='my_package',
    version='0.1',
    author='Dhhanush',
    author_email='dhhanushvanama999@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
)

