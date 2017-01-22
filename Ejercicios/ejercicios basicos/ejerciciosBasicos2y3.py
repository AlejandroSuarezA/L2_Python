#Escribe un programa que pida por teclado el radio de una circunferencia, y que a
#continuación calcule y escriba en pantalla la longitud de la circunferencia y del área del círculo.
import math
valor = int(input("Introduzca el radio de una circunferencia: "))

def longitud(radio):
    longitudCircunferencia = math.pi * (radio*2)
    print (longitudCircunferencia)

def area(radio):
    areaCircunferencia = math.pi * (radio**2)
    print (longitudCircunferencia)


longitud(valor)
area(valor)
