"""► Enunciado:Programa que solicite al usuario los datos
para calcular el área de un Círculo (●), finalmente mostrar el resultado en pantalla.
► Fórmula: Área del Círculo
Area = PI*(Radio**2)"""

print("Ingrese los siguientes datos para calcular el área del Círculo: ")

radio = int(input("El radio del círculo es: "))
area = 3.14*radio**2 #si pones coma (3,14) te arroja el print con ()

print(f"El área del Círculo es: {area}")