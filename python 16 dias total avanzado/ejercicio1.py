def devolver_distintos (*args):
    suma=sum(args)
    lista = list(args)
    lista.sort()
    if suma> 15:
        return max(lista) #<
    elif suma<10:
        return min(lista)
    else:
        return lista[1]
            
print(devolver_distintos (10,3,1))