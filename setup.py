
from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path: str)-> List[str]:
    ## This function is used to create a list of all requirements
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace ("\n","") for req in requirement]

    return requirement

setup (
    name = "Shipment Price Prediction",
    version = "0.0.1",
    author= "Ankit kumar",
    author_email= "kumar06112003@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
)
