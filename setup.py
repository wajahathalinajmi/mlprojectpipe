from setuptools import find_packages,setup
from typing import List

HYPEN_CON = '-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]

            if HYPEN_CON in requirements:
                requirements.remove(HYPEN_CON)
        print(f"parsed succesfully {requirements}")
        return requirements
    except FileNotFoundError:
        print("file was not found")
        return []
         
setup(
    name='mlpipeproject',
    version='0.0.1',
    author='Wajahath',
    author_email='wajahathalinajmis@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
)