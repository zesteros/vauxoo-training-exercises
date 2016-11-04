def sumar(a,b,suma):
	suma = a+b
z = 4
y = 10
w = 0
sumar(z,y,w)
print "w", w

def add_item(lista, items):
	lista.extend(items)
z = [1,2]
y = [3,4]
w = z
add_item(z,y)
print "z",z
print "w", w
print "y", y
