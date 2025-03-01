import os

def list_dir_files(path="."):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return dirs, files

dirs, files = list_dir_files()
print("Directories:", dirs)
print("Files:", files)
