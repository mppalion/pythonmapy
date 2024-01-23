"""Escribir un programa que pregunte el nombre y apellido del usuario. Luego de ser introducidos 
los datos muestre por pantalla la cadena ¡Hola {nombre} {apellido}, 
gusto en conocerte!, donde:{nombre} y {apellido} son los valores introducidos."""

nombre = input("¿Cuál es tu nombre? ")
apellido = input ("¿Cuál es tu apellido? ")

print(f"Hola {nombre} {apellido}, gusto en conocerte!")

# Declaracion de variables
nombre = ""
apellido = ""
 
# Solicitud de Datos
print(">>> Introduce tu nombre: ")
nombre = input("> ")
print(">>> Introduce tu apellido: ")
apellido = input("> ")

# Mensaje en Pantalla: Operador de Formato %
print("Hola %s %s, gusto en conocerte!" %(nombre,apellido))