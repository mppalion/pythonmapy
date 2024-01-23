"""Cree un programa que solicite al usuario su nombre y su edad.
Imprimir un mensaje personalizado con el nombre del usuario que 
indique el año en el cual la persona cumplirá 100 años."""

nombre = input ("Indica tu nombre completo: ")
edad = input ("indica tu edad: ")
edad = int (edad)
cumplio_este_anio = input("¿Has cumplido años este año? Y/N ")

def funcion_edad (edad):
    cien_anios = 100 - edad
    if cumplio_este_anio == "Y":
        fecha_cien_anios = 2023 + cien_anios
    else: 
        fecha_cien_anios =2024 + cien_anios
    return fecha_cien_anios

funcion_edad(edad)

print(f"{nombre}!! cumplirás 100 años en el {funcion_edad(edad)}")