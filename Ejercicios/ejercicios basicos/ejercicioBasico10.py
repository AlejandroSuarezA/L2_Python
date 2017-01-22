#Modifica el programa anterior para que en vez de mostrar un mensaje genérico
#en el caso de que alguno o los dos números sean negativos,
#escriba una salida diferenciada para cada una de las situaciones que se puedan producir,
#utilizando los siguientes mensajes:
#No se calcula la suma porque el primer número es negativo.
#No se calcula la suma porque el segundo número es negativo.
#No se calcula la suma porque los dos números son negativos.


numeroUno = int(input())
numeroDos = int(input())

def ejercicio(primero, segundo):
    if primero >= 0 and segundo >= 0:
        print ("La suma de los numeros es: " +str(primero+segundo))
    else:
        if primero < 0 and segundo >= 0:
            print ("No se calcula, el primer numero es negativo")
        elif segundo < 0 and primero >= 0:
            print ("No se calcula, el segundo numero es negativo")
        else:
            print ("No se calcula, ambos numeros son negativos")
