from random import randrange

matrix_dimension = 3

M3 = [[randrange(0, 10) for _ in range(matrix_dimension)] for _ in range(matrix_dimension)]

for row in M3:
	print(row)

positive, negative = 0, 0

for i in range(len(M3[0])):
	temp = 1
	for j in range(len(M3)):
		temp *= M3[j][(i + j) % len(M3[0])]
	positive += temp

for i in range(len(M3[0])):
	temp = 1
	for j in range(len(M3))[::-1]:
		temp *= M3[j][(i - j) % len(M3[0])]
	negative += temp

determinant = positive - negative

print("Matrix determinant:")
print(determinant)