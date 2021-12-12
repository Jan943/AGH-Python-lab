def calculate_roots(a, b, c):
	delta = b**2 - 4 * a * c
	if delta < 0:
		raise Exception("No real roots!")
	elif delta == 0:
		return - b / (2 * a)
	else:
		return (- b + delta**(1/2) ) / (2 * a), (- b - delta**(1/2) ) / (2 * a)

print("Checking results in 3 cases: ")
print("Delta = 0 : ")
print(calculate_roots(1, 2, 1))
print("Delta > 0 : ")
print(calculate_roots(1, 4, 1))
print("Delta < 0 : ")
print(calculate_roots(10, 2, 1))