import importlib.resources as resources
import os
from shutil import copyfile


def get_path_of_data_file(data_file):

    path = get_path_of_data_dir()

    file_path = os.path.join(path, data_file)

    return file_path


def get_path_of_data_dir():
    
    path = resources.files("gbmgeometry") / "data"

    return str(path)
