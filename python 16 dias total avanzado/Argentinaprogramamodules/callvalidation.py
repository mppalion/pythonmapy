# importa modulo de validacion de nombre y el de contrasenia
from validacioncontrasenia import *
from validacionNombre import *

nom = input ("Ingrese nombre a validar: ")
if validacionNombre(nom) is True:
    print ("nombre valido")
else:
    print ("contrasena invalida")
cont = input ("Ingrese contrasena a validar: ")
if validacioncontrasenia(cont) is True:
    print ("contrasenia valida")
else:
    print ("contrasena invalida")