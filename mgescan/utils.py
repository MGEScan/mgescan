import os

def get_abspath(path):
    try:
        return os.path.abspath(path)
    except:
        # print [DEBUG] Failed to convert a path to an absolute path
        return path

def create_directory(path, skipifexists=True):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        if skipifexists:
            new_path = path + ".1"
            return create_directory(new_path, skipifexists)
    return get_abspath(path)

def exists(path):
    try:
        return os.path.exists(path)
    except:
        return False
