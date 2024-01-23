"""► Enunciado:Escriba un programa que acepte un número entero (n) 
y calcule el valor de este número de la siguiente manera: n + nn + nnn
___
► Ejemplo:
Valor de Entrada: 5
Operación: 5 + 55 + 555
Resultado: 615"""

n = (input("Ingrese un numero entero: "))

def operacion(n):
    n1 = int(n)
    n2 = int(n+n)
    n3 = int(n+n+n)
    resultado = n1+n2+n3
    return resultado


print(f"El resultado es {operacion(n)}") 
    

