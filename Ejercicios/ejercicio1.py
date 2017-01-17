# -*- coding: utf-8 -*-
# Verificar si una cadena de texto leída por teclado es un DNI correcto o no.
# Suponer que los DNI tienen 8 dígitos y a continuación una letra mayúscula.


def verifyDNI(dni):
    if len(dni) == 9:
        letter = dni[-1]
        nums = dni[0:8]
        if letter.isupper() and nums.isdigit():
            print ("DNI has the correct structure")
        else:
            print ("DNI format incorrect")
    else:
        print ("DNI has an incorrect lenght of characters")
