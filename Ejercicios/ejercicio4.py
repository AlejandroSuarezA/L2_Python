# -*- coding: utf-8 -*-
# Almacenar en un vector (una lista) 5 números enteros leídos por teclado.
# Leer a continuación otro número y comprobar si está en el vector o no.
# En el caso de que esté visualizar qué posición ocupa.
# Sino indicarlo mediante un mensaje.
# Visualizar también el elemento más pequeño, el más grande y
# la posición de ambos en el vector.


def findPosition(number, vector):
    if number in vector:
        print ("The position in the vector is: " + str(vector.index(number)))
    else:
        print ("Cannot find the number in the vector")


def smallerAndHigher(vector):
    smallNumber = min(vector)
    highNumber = max(vector)

    smallPosition = vector.index(smallNumber)
    highPosition = vector.index(highNumber)

    smallString = "The smallest number is " + str(smallNumber) + " and his position is " + str(smallPosition)
    highString = "The highest number is " + str(highNumber) + " and his position is " + str(highPosition)

    print (smallString, "\n", highString)


testVector = []

for i in range(0, 5):
    testVector.append(int(input("Creating exercise vector...")))
print(testVector)

newInput = int(input("Introduce a new number:"))

findPosition(newInput, testVector)

smallerAndHigher(testVector)
