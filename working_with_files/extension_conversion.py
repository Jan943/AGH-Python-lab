import os

path = "example_files"

current_dir = os.getcwd()

os.chdir(path)

for file in os.listdir("."):
	name, extension = file.split(".")
	if extension in "jpg":
		os.rename(file, name + ".png")
	elif extension in "png":
		os.rename(file, name + ".jpg")

os.chdir(current_dir)