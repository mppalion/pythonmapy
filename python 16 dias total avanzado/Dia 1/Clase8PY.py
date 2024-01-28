def validacion_usuario ()
    nom = str ("ingrese un nombre de usuario: ")
    listanom = list nom
    if (len (nom) < 6):
        print ("El nombre de usuario debe contener al menos 6 caracteres")
    elif  (len (nom) > 12):
        print("El nombre de usuario no puede contener más de 12 caracteres")
    while true:
        listanom


# Verificar longitud User
def validar_usuario(usuario):
    if len(usuario) < 6:
        return "El usuario debe contener al menos 6 caracteres"
    elif len(usuario) > 12:
        return "El usuario no puede excederse de 12 caracteres"

    # Verificar si User es alfanum
    if not usuario.isalnum():
        return "El usuario puede contener solo letras y números"
    else:
        return True


# Programa User
usuario = input("Ingrese el nombre de usuario por favor: ")
validacion = validar_usuario(usuario)
if validacion is True:
    print("Nombre de usuario válido.")
else:
    print(validacion)


while True:
    usuario = input("Ingrese el nombre de usuario por favor: ")
    validacion = validar_usuario(usuario)
    if validacion is True:
        print("Nombre de usuario válido.")
    else:
        usuario = input("Ingrese el nombre de usuario por favor: ")