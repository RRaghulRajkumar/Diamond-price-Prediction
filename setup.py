from setuptools import find_packages,setup
from typing import List 
'''
Automating Package Installation
'''
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
"""
Creating Our Own Package
"""

setup(
    name="DiamondPricePrediction",
    version='0.0.1',
    author='RaghulRajkumar.R',
    author_email='rraghulrajkumar@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)