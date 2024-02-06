from random import choice
def funcion_inicio ():
    print("Vamos a jugar al juego del ahorcado")
    print("Tenes que adivinar una palabra")
    lista=["perro","gato","camaleon","conejo","tigre","lobo","pato"]
    palabra= choice(lista)
    lista_espacios = []
    for i in palabra:
        lista_espacios.append("-")
    print(f"La palabra tiene los siguientes espacios:{lista_espacios} ")
    return (lista_espacios,palabra)

def chequearletra(letra):
    letra= letra.strip()
    while not letra.isalpha():
        letra = input("Ingresaste cualquier cosa, ingresá una letra: ")
    return letra
    
def funcion_juego (lista_espacios,palabra):
    vidas= 6
    palabra_en_lista = list(palabra)
    while vidas > 0:
        letra = input("ingresa una letra: ")
        letra = letra.strip()
        chequearletra(letra)
        if letra in palabra:
            n=0
            print("Muy bien la letra está en la palabra")
            for elemento in palabra_en_lista:
                if letra == palabra_en_lista[n]:
                    lista_espacios[n] = elemento
                n=n+1
            funcion_ahorcado(vidas,lista_espacios)
            if mostrarvictoria(lista_espacios,palabra)== True:
                break
        else: 
            print("oh!oh!. Esa letra no forma parte de la palabra")
            print(f"te quedan {vidas-1} vidas más")
            vidas = vidas-1
            funcion_ahorcado(vidas,lista_espacios)
            
def mostrarvictoria(lista_espacios,palabra):
    palabra_en_lista = list(palabra)
    if lista_espacios==palabra_en_lista:
        print("GANASTE!!!!!AAAAA")
        return True
    else:
        return False
               
def funcion_ahorcado(vidas,lista_espacios):
    if vidas==6:
        print(f"{lista_espacios}")
    if vidas==5:
        print("    ______  ")
        print("    |    |  ")
        print("    |    O  ")   
        print(f"    |       {lista_espacios}")   
        print("    |       ")   
        print("  __|__     ")
    elif vidas==4:
        print("   ______  ")
        print("   |    |  ")
        print("   |    O  ")   
        print(f"   |    |  {lista_espacios}")   
        print("   |       ")   
        print(" __|__     ")
    elif vidas==3:
        print("   ______  ")
        print("   |    |  ")
        print("   |    O  ")   
        print(f"   |   /|  {lista_espacios}")   
        print("   |       ")   
        print(" __|__     ")
    elif vidas==2:
        print("   ______  ")
        print("   |    |  ")
        print("   |    O  ")   
        print(f"   |   /|\ {lista_espacios}")   
        print("   |       ")   
        print(" __|__     ")  
    elif vidas==1:
        print("   ______  ")
        print("   |    |  ")
        print("   |    O  ")   
        print(f"   |   /|\ {lista_espacios}")   
        print("   |   /   ")   
        print(" __|__     ")              
    elif vidas==0:
        print("   ______  ")
        print("   |    |  ")
        print("   |    O  ")   
        print(f"   |   /|\ {lista_espacios}")   
        print("   |   / \ ")   
        print(" __|__     ")   

(lista_espacios,palabra) = funcion_inicio ()
funcion_juego(lista_espacios,palabra)