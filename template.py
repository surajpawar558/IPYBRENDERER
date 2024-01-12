import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the project_name: ")
    if project_name != "":
        break

logging.info(f"Creating project name: {project_name}")

# List of files:
list_of_files = [
    ".github/workflows/.gitkeep",
    f"SRC/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"File is already present at: {filepath}")





        