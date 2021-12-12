from random import randrange

matrix_dimension = 128
M1 = [[randrange(0, 1000) for _ in range(matrix_dimension)] for _ in range(matrix_dimension)]
M2 = [[randrange(0, 1000) for _ in range(matrix_dimension)] for _ in range(matrix_dimension)]

def sum_matrices(M1, M2):
	for i in range(len(M1)):
		for j in range(len(M1[0])):
			M1[i][j] += M2[i][j]
	return M1

def print_matrix(M):
	for row in M:
		print(row)

print(f"Matrix1:")
print_matrix(M1)
print(f"Matrix2:")
print_matrix(M2)
print(f"Their sum:")
result = sum_matrices(M1, M2)
print_matrix(result)