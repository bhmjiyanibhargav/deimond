from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

            
        return requirements

setup(
    name='dimandprice',
    version='0.0.1',  # Added single quotes around version number
    author='bhargav',
    author_email='bhimjiyanibhargav@gmail.com',  # Added comma at the end of the line
    install_requires=get_requirements('requirements.txt'),  # Corrected typo here
    packages=find_packages()
)
