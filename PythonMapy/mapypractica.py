print("Hola Mundo!")

name= "Maria Paula"
last_name = "Palilon"

print("Hola"+" "+name)

print(f"¿Cómo estás {name}?")

oracion_de_saludo = "Buen día {} {}"

print(oracion_de_saludo.format(name,last_name))#Ojo si ponés dos corchetes si o si tenes que poner dos parámetros, un parámetro para cada corchete del .format

print(f"¿Cómo estás {name} {last_name}?")

name = input ("Ingresa tu nombre: ")
print (f"Hola cómo estás {name}?")