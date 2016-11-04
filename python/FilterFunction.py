def es_par(n):
	"""Function to ilustrate filters"""
	return (n % 2.0 == 0)
l = [1, 2, 3]
l2 = filter(es_par, l)
print l2
