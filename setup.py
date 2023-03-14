from setuptools import find_packages,setup
from typing import List


hypen_e_dot="-e."
def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
        if hypen_e_dot in requirments:
            requirments.remove(hypen_e_dot)

    return requirments 





setup(
    name="spproject",
    version='0.0.1',
    author='Arc',
    author_email='xarv68@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')

)