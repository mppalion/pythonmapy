from operaciones import *

try:
    import operaciones
except ModuleNotFoundError as e:
    print("Hubo un error al importar el modulo:", e)

a,b = 10 , 20

print("la suma de {} y {} es igual a {}".format (a , b,suma(a,b)))
print("la resta de {} y {} es igual a {}".format (a,b,resta(a,b)))
print("la multiplicacion de {} y {} es igual a {}".format (a,b,multiplica(a,b)))
print("la division de {} y {} es igual a {}".format (a,b,divide(a,b)))