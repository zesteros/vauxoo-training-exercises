try:
	edad = raw_input("Cuantos anyos tienes? ")
	dias = int(edad) * 365
	print "Has vivido " + str(dias) + " dias"
except ValueError:
	print "Eso no es un numero"
