import os
from pathlib import Path
import logging

logging.basicConfig(
                    level=logging.INFO,
                    format="[%(asctime)s: %(levelname)s: %(message)s]")

while True:
    project_name=input("Enter the project name")
    if project_name!="":
        break

logging.info(f"Creating the project {project_name}")


list_of_files=[".github/workflows/.gitkeep",
               f"src/{project_name}/__init__.py",
               f"tests/__init__.py",
               f"tests/unit/__init__.py",
               f"tests/intergration/__init__.py",
               "init_setup.sh",
               "requirements.txt",
               "requirements_dev.txt",
               "setup.py",
               "project.toml",
               "setup.cfg",
               "tox.ini",]

for file in list_of_files:

    file=Path(file)
    filedir,filename=os.path.split(Path(file))
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory at: {filedir} for file {filename}")

    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open (file,'w') as f:
            pass
        logging.info(f"Creating a new file {filename} at path : {file}")
    else:
        logging.info(f"file is already present at {file}")
