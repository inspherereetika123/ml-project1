from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file.
    """
    requirements = []
    with open(file_path, encoding='utf-8') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Reetika',
    author_email='reetika.singh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
