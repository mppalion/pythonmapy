lista_numeros=[]
def reducir_lista(lista_numeros):
    n=0
    lista_reducida=[]
    a=max(lista_numeros)
    for i in lista_numeros:
        if i != lista_numeros[n-1] and i!=a:
            lista_reducida.append(i)
            n=n+1
        else:
            pass
    return lista_reducida  

listaaa= [12,20,23,3]
a= list(set(listaaa))
print(a)
 
print(reducir_lista(lista_numeros=[12,20,23,3]))

def promedio(lista_reducida):
    suma=0
    p=0
    for i in lista_reducida:
        suma=suma+i
        p=p+1
    return (suma/p)
print(promedio(reducir_lista(lista_numeros=[12,20,23,3])))