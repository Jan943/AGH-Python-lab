from random import randrange

matrix_dimension = 8
M1 = [[randrange(0, 10) for _ in range(matrix_dimension)] for _ in range(matrix_dimension)]
M2 = [[randrange(0, 10) for _ in range(matrix_dimension)] for _ in range(matrix_dimension)]

def multiply_matrices(M1, M2):
	result = [[0 for _ in range(matrix_dimension)] for _ in range(matrix_dimension)]
	rows_M1 = len(M1)
	cols_M1 = len(M1[0])
	rows_M2 = len(M2)
	cols_M2 = len(M2[0])
	for i in range(rows_M1):
		for j in range(rows_M2):
			for k in range(cols_M2):
				result[i][j] += M1[i][k] * M2[k][j]
	return result

def print_matrix(M):
	for row in M:
		print(row)

print("Matrix 1:")
print_matrix(M1)
print("Matrix 2:")
print_matrix(M2)
print("Their multiplication:")
result = multiply_matrices(M1, M2)
print_matrix(result)