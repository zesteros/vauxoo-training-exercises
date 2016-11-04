def sumar(x, y):
	return x + y
l = [1, 2, 3]
l2 = reduce(sumar, l)
print l2
