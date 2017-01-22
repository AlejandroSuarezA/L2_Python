#Escribe un programa que pida por teclado tres valores de tipo entero,
#y que calcule si se cumple que la suma de dos de ellos es igual al tercero.
#La salida del programa tiene que tener el formato:
#Números introducidos: N1	N2 N3 (tabulador)
#Y una de las cuatro líneas de salida siguientes:
#Se cumple que N1 = N2 + N3
#Se cumple que N2 = N1 + N3
#Se cumple que N3 = N1 + N2
#Los números no cumplen la condición



def ejercicio(primero, segundo, tercero):
    if primero == segundo + tercero:
        print ("Se cumple que " + str(primero) + "= " + str(segundo)+ "+" + str(tercero))

    elif segundo == primero + tercero:
        print ("Se cumple que " + str(segundo) + "= " + str(primero)+ "+" + str(tercero))

    elif tercero == primero + segundo:
        print ("Se cumple que " + str(tercero) + "= " + str(primero)+ "+" + str(segundo))

    else:
        print ("No cumplen la condicion")
