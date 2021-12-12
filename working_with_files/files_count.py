import os

path = "/dev"

number_of_files = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

print(f"Number of files(not together with directories) in '{path}': {number_of_files}")
