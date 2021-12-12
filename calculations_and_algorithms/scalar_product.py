a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

def scalar_product(a, b):
	if len(a) != len(b):
		raise Exception("Vector dimensions don't match!")
	sum = 0
	for i in range(len(a)):
		sum += a[i] * b[i]
	return sum

print(f"Scalar product of {a} and {b}: {scalar_product(a, b)}")