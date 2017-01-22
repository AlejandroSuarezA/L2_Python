#Escribe un programa que nos pida por teclado dos números enteros y
#que a continuación muestre en pantalla la suma de los dos números solamente
#si son los dos positivos. Si no se cumple que los dos números sean positivos
#se visualizará un mensaje indicándolo. La salida ha de tener
#el siguiente formato: “La suma de los dos números es: xxx” o
#“No se calcula la suma porque alguno de los números o los dos no son positivos”.

numeroUno = int(input())
numeroDos = int(input())

def ejercicio(primero, segundo):
    if primero >= 0 and segundo >= 0:
        print ("La suma de los numeros es: " +str(primero+segundo))
    else:
        print ("No se calcula por que uno o los dos numeros no son positivos")
