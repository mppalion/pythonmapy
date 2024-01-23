"""► Enunciado:Programa que solicite al usuario los datos para calcular 
el área de un Cuadrado (■), finalmente mostrar el resultado en pantalla.
► Fórmula: Área del cuadrado
Area = Lado ** 2"""

print("Ingrese los siguientes datos para calcular el área del un cuadrado: ")
lado1= input ("¿Cuánto mide el lado 1? ")
lado2= input ("¿Cuánto mide el lado 2? ")

lado1 = int(lado1)
lado2 = int(lado2)

area = lado1*lado2

print(f"El área del cuadro mide: {area}")

print("Perfecto! Ahora ¿Qué pasa si el cuadrado es rectángulo(todos sus lados son iguales)?")
lado= input ("¿Cuánto mide uno de sus lados? ")

lado = int(lado)
area = lado**2

print(f"Esta vez, el área del cuadro mide: {area}")