def listar_primos_de_una (numero):
    listado=[]
    contador_de_primos=0
    booleano=0
    for i in range(2,numero):
        for x in range(2,i-1):
            if x % i == 0:
                booleano=False
            if booleano == True:
                listado.append(x)
            contador_de_primos = contador_de_primos+1
    return (listado,contador_de_primos)

print(listar_primos_de_una(25))

"""
lista = list(range(2,25+1))
print(lista)
lista=[32,2,3]
print(lista[2])
"""