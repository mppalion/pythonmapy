# ejercicio2 de modulos
def validacionNombre(nom):
    if len(nom) < 6:
        print("El nombre de usuario debe contener al menos 6 caracteres")
    elif len(nom) > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
    elif not (nom.isalnum()):
        print("El nombre de usuario puede contener solo letras y números")
    else:
        return True
