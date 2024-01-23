from random import choice 
a=0
lista_numeros=[0,1,2,3,4]

def lanzar_moneda ():
    a=("Cara","Cruz")
    a= choice(a)
    return a
    
def probar_suerte(a,lista_numeros):
    if a=="Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros
        
print(probar_suerte(lanzar_moneda(),lista_numeros))
