import os

code = input("Please input the code: ")

file_name = "code.txt"

if file_name in os.listdir("."):
	f = open(file_name, "r")
	if f.read() == code:
		print("Correct code.")
	else:
		print("Incorrect code.")
	f.close()
else:
	f = open(file_name, "w")
	f.write(code)
	f.close()
	print("Code saved.")