a=0
b=0
def suma(*args):
    
    total=0
    for argumento in args:
        total += argumento
    return (total)

print(suma(3,4,5,10))

"""
Lo mismo que hacer con sum
ojo sum solo puede tomar hasta 2 argumentos por eso:
"""

def suma2(*args):
    total =0
    total = sum(args)
    return total

print(suma2(3,4,5,10))

def suma_absolutos(*args):
    suma=0
    for argumento in args:
        absoluto = 0
        absoluto = abs(argumento)
        suma =  suma + absoluto
    return suma
print(suma_absolutos(3,4,5,10,-1))

def suma_cuadrados (*args):
    total_cuadrados = 0
    for arguments in args:
        total_cuadrados = total_cuadrados + (arguments**2)
    return total_cuadrados
        
suma_cuadrados(1,2,3)

def numeros_persona (nombre, *args):
    suma_numeros=0
    for num in args:
        suma_numeros = suma_numeros + num
    return (f"{nombre}, la suma de tus números es {suma_numeros}")

nombre = input("Ingresa tu nombre: ")

print(numeros_persona (nombre,32,1,2,3))