from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    ''' this function will return a list of requirements from a file '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='ML-project',
    version='0.0.1',
    author='Anuj Patel',
    author_email='anujpatel997780@gmail.com',
    packages=find_packages(where='src'),
    install_requires=get_requirements('requirements.txt')
    
)