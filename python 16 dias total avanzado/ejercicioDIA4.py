import time
from random import randint
print("Este es el juego de los números mágicos")
name = input("Para iniciar ingresa tu nombre:")
tiempo = time.localtime().tm_hour
if tiempo < 12: 
    print(f"Buenos Dias {name}! Bienvenido al Juego de los Números Mágicos!")
elif (int(tiempo) >= 12 and int(tiempo) <=19):
    print(f"Buenas Tardes {name}! Bienvenido al Juego de los Números Mágicos!")
else: (f"Buenos Noches {name}! Bienvenido al Juego de los Números Mágicos!")

magicnumber = randint(0,101)

print(f"Bueno, {name} he pensado un número entre 0 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

oportunidades = 8
restantes = 8
while oportunidades > 0:
    userinput = (input("Ingresa el número: "))    
    if userinput.isnumeric() == False:
        print("Ingresaste cualquier cosa, dale de nuevo")
        continue
    usernumber= int(userinput)
    if usernumber > 100 or usernumber < 0:
        oportunidades= oportunidades-1
        print(f"el número está fuera del rango, tienes {oportunidades} oportunidades más")
    
    if usernumber == magicnumber:
        print(f"Perfecto! has adivinado el número mágico, solo te ha llevado {restantes - oportunidades} intentos")
        break
    elif usernumber > magicnumber:
        oportunidades= oportunidades-1
        print("Oh! lo siento, ese número es más alto que el que había pensado, intentalo nuevamente.") 
        print(f"Te quedan {oportunidades} oportunidades")
             
    else:
        oportunidades= oportunidades-1
        print("Oh! lo siento, ese número es más bajo que el que había pensado, intentalo nuevamente")
        print(f"Te quedan {oportunidades} oportunidades")


print("El juego ha terminado")
    




