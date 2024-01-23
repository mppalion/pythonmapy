"""► Enunciado: Programa que solicite al usuario los datos 
para calcular el área de un Triángulo (▲), finalmente mostrar el resultado en pantalla.
► Fórmula: Área del Triángulo 
Area = (Base*Altura)/2"""

print("Ingrese los datos correspondientes para calcular el área del triángulo: ")
base = int(input("¿Cuánto mide la base del triángulo?: "))
altura = int(input("¿Cuánto mide la altura del triángulo?: "))

area = int((base*altura)/2)

print(f"El área del triángulo mide: {area} en valores enteros")

area = ((base*altura)/2)

print(f"El área del triángulo mide: {area} en valores reales")
