f = open("archivo.txt", "r")
while True:
	linea = f.readline()
	if not linea: break
	print linea
f = open("archivo.txt", "w")
n = 0
while n < 20:
	f.write(str(n))
	n+=1 
