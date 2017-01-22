#Escribe un programa que pida por teclado un número y que a continuación muestre
#el mensaje el número leído es positivo o bien el número leído es negativo
#dependiendo de que el número introducido por teclado sea positivo o negativo.
#Consideramos al número 0 positivo.

numeroSolicitado = int(input())

def comprobar(numeroEjercicio):
    if numeroEjercicio >= 0:
        return ("El numero es positivo")
    else:
        return ("El numero es negativo")
