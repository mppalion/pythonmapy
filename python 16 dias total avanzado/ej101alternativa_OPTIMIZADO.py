lista_numeros= [1,2,15,7,2,8]
def reducir_lista_mejor ():
    lista_numeros.sort()
    print(lista_numeros)
    lista_numeros.pop()
    return lista_numeros

def promedio_lista(lista_numeros):
    valor_medio= sum(lista_numeros)/len(lista_numeros)
    return valor_medio

print(reducir_lista_mejor ())
print(promedio_lista(lista_numeros))
    