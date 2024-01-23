import random
dado1=0
dado2=0

def lanzar_dadosa():
    dado1= random.randint(1,6)
    return dado1

def lanzar_dadosb():
    dado2= random.randint(1,6)
    return dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        return(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        return(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

print(evaluar_jugada(lanzar_dadosa(), lanzar_dadosb()))

 
