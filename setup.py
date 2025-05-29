from setuptools import find_packages,setup
from typing import List

HYPEN_CON = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_CON in requirements:
            requirements.remove(HYPEN_CON)
    
    return requirements
         
setup(
    name='MLPROJECTPIPE',
    version='0.0.1',
    author='Wajahath',
    author_email='wajahathalinajmis@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires = get_requirements('requirements.txt')
)