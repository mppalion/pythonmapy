"""Escribir un programa que lea un entero positivo, 
introducido por el usuario y después muestre en pantalla 
la suma de todos los enteros desde 1. La suma de los primeros 
enteros positivos puede ser calculada de la siguiente forma:"""

entero_positivo = input("Ingresa un entero positivo: ")
entero_positivo = int(entero_positivo)

def sumatoria (entero_positivo):
    suma=0
    i=0
    while i <= entero_positivo:
        suma = i+suma
        i = i+1
    return suma

sumatotal = (sumatoria(entero_positivo))
print(f"La suma de todos los numeros enteros positivos desde 1 hasta el entero ingresado {entero_positivo} es igual a: {sumatotal}")
