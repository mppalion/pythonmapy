# ejercicio2 de modulos
def validacioncontrasenia(cont):
    cantmayus = 0
    cantminus = 0
    noalpha = 0
    space = 0
    if len(cont) >= 8:
        for i in cont:
            if i.isupper():
                cantmayus = cantmayus + 1
        for i in cont:
            if i.islower():
                cantminus = cantminus + 1
        for i in cont:
            if not i.isalnum():
                noalpha = noalpha + 1
        for i in cont:
            if i == " ":
                space = space + 1
        if cantmayus > 0 and cantminus > 0 and noalpha > 0 and space ==0:
            return True
        else:
            return print("La contraseña elegida no es segura")
    return print("La contraseña elegida no es segura")
