import os

dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]

print("Directories:", dirs)
print("Files:", files)
