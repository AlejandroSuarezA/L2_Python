# -*- coding: utf-8 -*-
# Construye un programa en el que se declare una matriz de dimensiones 5 x 8
# (5 filas y 8 columnas) Asigna a las posiciones de la matriz números enteros
# generados al azar y comprendidos entre 0 y 100. Calcula cuál es el número más pequeño
# y el mayor de la tabla y muéstralos por pantalla indicando la posición que ocupan en la matriz.
# Muestra también la tabla por pantalla para comprobar los resultados.
import random


def exercise(exerciseMatrix):
    createMatrix(exerciseMatrix)
    searchBigger(exerciseMatrix)
    searchSmall(exerciseMatrix)


def createLine(newMatrix):
    newLine = []
    while len(newLine) < 8:
        newLine.append(random.randint(0, 100))
    newMatrix.append(newLine)
    # print(newMatrix)


def searchBigger(matrix):
    biggerNum = 0
    for line in matrix:
        if max(line) > biggerNum:
            biggerNum = max(line)

            positionLine = matrix.index(line)
            positionNum = line.index(biggerNum)
            positionString = "The position of " + str(biggerNum) + " is [" + str(positionLine) + "]" + "[" + str(positionNum) + "]"
        else:
            pass
    print (positionString)


def searchSmall(matrix):
    smallerNum = 101
    for line in matrix:
        if min(line) < smallerNum:
            smallerNum = min(line)

            positionLine = matrix.index(line)
            positionNum = line.index(smallerNum)
            positionString = "The position of " + str(smallerNum) + " is [" + str(positionLine) + "]" + "[" + str(positionNum) + "]"
        else:
            pass
    print (positionString)


def createMatrix(emptyMatrix):
    while len(emptyMatrix) < 5:
        createLine(emptyMatrix)
    for line in emptyMatrix:
        print(line)


if __name__ == "__main__":

    # TEST
    # test 1
    # Check createLine WHILE LOOP

    test1 = []
createLine(test1)
if len(test1[0]) == 8:
    print("TEST 1 OK")
else:
    print("TEST 1 Error")
print("-" * 5 + "TEST 1 END" + "-" * 5)

# test 2
# Check createMatrix WHILE LOOP
test2 = []
createMatrix(test2)
if len(test2) == 5:
    print("TEST 2 OK")
else:
    print("TEST 2 Error")
print("-" * 5 + "TEST 2 END" + "-" * 5)

# test 3
# Find the smaller num
test3 = [[35, 34, 31, 2, 67, 48, 44, 51],
    [23, 33, 91, 43, 43, 57, 49, 9],
    [75, 92, 81, 27, 76, 91, 70, 63],
    [19, 27, 70, 40, 72, 31, 67, 19],
    [0, 58, 96, 45, 39, 93, 59, 83]]
print("TEST 3 actual position = [4][0]")
searchSmall(test3)
print("-" * 5 + "TEST 3 END" + "-" * 5)

# test 4
# Check createMatrix and then searchSmall & searchBigger
test4 = []
createMatrix(test4)
searchSmall(test4)
searchBigger(test4)
print("-" * 5 + "TEST 4 END" + "-" * 5)

# test 5
# Check exercise call
test5 = []
exercise(test5)
