#Escribe un programa que pida por teclado dos números y que muestre en pantalla
#uno de los dos mensajes siguientes en función de los números leídos:
#a) el primer número (valor) es mayor que el segundo (valor)(introduciendo el valor de los números en el mensaje);
#b) el primer número (valor) es menor que el segundo (valor; c) los dos números son iguales (valor).

numeroUno = int(input())
numeroDos = int(input())

def ejercicio(primer, segundo):
    if primer == segundo:
        print ("los dos numeros son iguales")
    elif primer > segundo:
        print("el primer numero es mayor que el segundo")
    else:
        print("el segundo numero es mayor que el primero")
