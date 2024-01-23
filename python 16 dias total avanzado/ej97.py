def todos_positivos(lista_numeros):
    a=True
    for n in lista_numeros:
        if n >= 0:
            a = True
        else:
            a = False
            break
    return a

lista = [1,2,4]
lista2 = [-1,2,3]

print(todos_positivos(lista))
print(todos_positivos(lista2))

lista_numeros = []
lista_numeros = [-1,100,2,4,2]
def suma_menores(lista_numeros):
    suma = 0 
    for n in lista_numeros:
        if n in range (0,1000):
            suma = suma + n
    return suma

print(suma_menores(lista_numeros))

lista_numeros = [1, 50, 502, 755, 34]
def cantidad_pares(lista_numeros):
    suma_pares = 0
    for n in lista_numeros:
        if n % 2 == 0:
            suma_pares = suma_pares + n
        else:
            pass
    return suma_pares
cantidad_pares (lista_numeros)

print(cantidad_pares(lista_numeros))