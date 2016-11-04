"""List comprehension example
"""
l = [0, 1, 2, 3]
m = ["a", "b"]
n = []
for s in m:
	for v in l:
		if v > 0:
			n.append(s* v)
print n," Sin comprension de listas"

l = [0, 1, 2, 3]
m = ["a", "b"]
n = [s * v for s in m
        	for v in l
		if v > 0]
print n, "Con compresion de listas"

