from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]: 
    """
    This function will return a list of requirements
    """

    requirements = []

    with open(file_path, encoding='utf-8') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements




setup(
    name = 'mlproject',
    version='0.0.1',
    author='sahil katariya',
    description='it is a machine learning project which is used to predict student performance based on some parameters',
    author_email='sahilkatariya012@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)