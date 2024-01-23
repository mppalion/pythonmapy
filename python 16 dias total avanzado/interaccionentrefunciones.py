import random
lista_palitos = ["-","--","---","----"]

def mezclar_lista(lista_palitos):
    random.shuffle(lista_palitos)
    return lista_palitos

#print(mezclar_lista(lista_palitos))

def elije_palito (lista_palitos):
    palito_elegido =""
    while palito_elegido not in ["1","2","3","4"]:
        palito_elegido = input ("Elije uno de los palitos 1,2,3 o 4")
        
        
        
