from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from the given file.
    It removes '-e .' if present.
    '''
    requirements = []
    Hype_dot_E = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read lines from the file
        requirements = [req.replace('\n', '') for req in requirements]  # Clean up newlines
        if Hype_dot_E in requirements:
            requirements.remove(Hype_dot_E)  # Remove '-e .' if it's in the list
    return requirements

setup(
    name="MLProject",
    version="0.0.1",
    author="Niranjan",
    author_email="niranjanbokare2112@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Get requirements from the file
)
