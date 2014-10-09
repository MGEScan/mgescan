import os

def get_abspath(path):
    try:
        return os.path.abspath(path)
    except:
        # print [DEBUG] Failed to convert a path to an absolute path
        return path

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return get_abspath(path)
    else:
        new_path = path + ".1"
        return create_directory(new_path)
