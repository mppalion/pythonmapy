""" 2► Enunciado: Programa que solicite al usuario los datos para llevar 
Grados Farenheit a Grados Celcius. 
► Fórmula: Grados Farenheit a Grados Celcius
celcius = (fahrenheit - 32.0) * 5.0 / 9.0 """

print("Le solicitaremos los siguientes datos a fin de realizar una conversión de grados F° a C°")
grados_f = input("Ingrese los grados Farenheit que desee convertir a Celsius: ")
grados_f = float(grados_f)
grados_c = (grados_f-32) * 5.0 / 9.0
grados_c = round(grados_c,2)

print(f"{grados_f}°F son equivalentes a {grados_c}°C")