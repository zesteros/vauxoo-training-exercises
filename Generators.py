def mi_generador(n, m, s):
	while(n <= m):
		yield n
		n += s
x = mi_generador(0, 5, 1)
print x
for n in mi_generador(0, 5, 1):
	print n
