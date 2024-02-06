from pathlib import Path
from os import system

ruta = Path(Path.home(), "Documents", "PythonMapy", "pythonmapy", "python 16 dias total avanzado","Día 6","Recetas")
print(ruta)
cantidad_recetas=8
cantidad_categorias = 4
actividad=True
mensaje_volver_al_menu="\nIngrese alguna tecla para regresar al menú"
print("Bienvenido al Recetario joven!!\n")

def menu_principal (ruta,cantidad_recetas):
    print("        ReCeTaRiO ")
    print("______Menú Principal______\n")
    print(f"Las recetas se encuentran almacenadas dentro de PC en la dirección:\n{ruta}")
    print(f"Existen {cantidad_recetas} recetas en total")
    print("A continuación podrás ver todo lo que podrás hacer en este hermoso Recetario:\n")
    print(" [1] leer la Receta \n [2] Crear Receta \n [3] Crear Categoría \n [4] Eliminar Receta \n [5] Eliminar Categoría \n [6] Mostrar todas las recetas \n [7] Mostrar todas las categorias \n [8] Finalizar Programa" )
    opcion= input("Elije una de estas opciones: ")
    return opcion

def ingresar_correcto(opcion):
    while opcion not in ["1","2","3","4","5","6","7","8"]:
        print("Ingresaste una opción incorrecta, por favor vuelve a intentarlo nuevamente")
        input("presiona una tecla")
        system("cls")
        menu_principal (ruta,cantidad_recetas)
    return int (opcion)

def listar_categorias (ruta):
    lista=[]
    for child in ruta.iterdir():
        lista.append(child.name)
    return lista

print(listar_categorias(ruta))

"""def listar_recetas (ruta):
    for child in ruta.iterdir():
        print(child)"""
        
def finalizar_programa(ruta):
    system("cls")
    print("Seleccionaste la opción de salir!")
    confirmacionsalir = input("Deseas finalizar el programa? y/n: ")
    confirmacionsalir = confirmacionsalir.lower()
    if confirmacionsalir == "n":
        menu_principal(ruta,cantidad_recetas)
    else:
        system("cls")
        print("Gracias por haber ingresado al Recetario. Hasta Pronto!")
        return False
    return menu_principal(ruta,cantidad_recetas)


        
def listar_categorias(ruta):
    for txt in ruta.glob("*/**"):
        print(txt.stem)
        
def listar_recetas(ruta):
    for txt in ruta.glob("**/*.txt"):
        print(txt.stem)
        
def leer_receta (ruta):
    listar_categorias(ruta)
    opcion_categoria = input("Elige la categoría que más te guste: ")
    ruta_categoria =Path(ruta,opcion_categoria)
    listar_recetas(ruta_categoria)
    opcion_receta = input("Elige la receta que más te guste: ") + ".txt"
    print(ruta_categoria.read_text(opcion_receta))
    return True

def crear_receta (cantidad_recetas,ruta):
    print("Deseas crear una receta?")
    categoria = input("Ingresa la categoria en la que estaría tu nueva receta: ")
    ruta = open("archivo.txt","w")
    nombre_de_receta=("Genial! Ahora ingresa el nombre de tu nueva receta: ")
    cantidad_recetas=cantidad_recetas+1
    
def crear_categoria (categorias,ruta):
    nueva_categoria= input("Ingresa la nueva categoria que deseas adicionar: ")
    ruta = Path(Path.home(),f"{nueva_categoria}")
    print(f"Se ha creado la nueva categoría {nueva_categoria} dentro de Recetas ")
    return menu_principal (ruta,cantidad_recetas)

def eliminar_receta (cantidad_recetas,ruta,opcion):
    print("Deseas eliminar una receta?")
    categoria = input("Ingresa la categoria en la que estaría tu receta a eliminar: ")
    nombre_de_receta=("Genial! Ahora ingresa el nombre de la receta a eliminar: ")
    system("cls")
    print("Seleccionaste la opción de eliminar esta receta!")
    confirmacionborrar = input(f"Estás seguro que deseas eliminar la receta {nombre_de_receta}? y/n")
    confirmacionborrar = confirmacionborrar.lower()
    if confirmacionborrar == "n":
        opcion = ingresar_correcto(menu_principal (ruta,cantidad_recetas))
    else:
        cantidad_recetas=cantidad_recetas-1
        #REMOVER RECETA
        print("La receta ha sido eliminada permanentemente")
    return (cantidad_recetas, menu_principal (ruta,cantidad_recetas))


def eliminar_categoria(cantidad_categorias,opcion):
    listar_categorias(ruta)
    print("Deseas eliminar una categoria?")
    opcion_categoria = input("Elige la categoría que desees eliminar: ")
    ruta_categoria =Path(ruta,opcion_categoria)
    system("cls")
    confirmacionborrar = input(f"Estás seguro que deseas eliminar la categoria {opcion_categoria}? y/n")
    confirmacionborrar = confirmacionborrar.lower()
    if confirmacionborrar == "n":
        opcion = ingresar_correcto(menu_principal (ruta,cantidad_recetas))
    else:
        cantidad_categorias=cantidad_categorias-1
        #REMOVER CATEGORIA ruta.rmdir
        print("La categoría ha sido eliminada permanentemente")
    return True



while actividad==True:
    opcion = ingresar_correcto(menu_principal (ruta,cantidad_recetas))
    if opcion == 1:
        system("cls") 
        leer_receta (ruta)
        input(mensaje_volver_al_menu)
    elif opcion == 2:
        system("cls") 
        crear_receta(cantidad_recetas,ruta)
        input(mensaje_volver_al_menu)
    elif opcion == 3:
        system("cls")        
        crear_categoria(cantidad_categorias,ruta)
        input(mensaje_volver_al_menu)
    elif opcion == 4:
        system("cls")
        eliminar_receta (cantidad_recetas,ruta,opcion)
        input(mensaje_volver_al_menu)
    elif opcion == 5:
        system("cls")
        eliminar_categoria (cantidad_categorias,ruta,opcion)
        input(mensaje_volver_al_menu)
    elif opcion == 6:
        system("cls")
        listar_recetas(ruta)
        input(mensaje_volver_al_menu)
    elif opcion == 7:
        system("cls")
        for elemento in ruta.glob("*/**"):
            print(elemento.stem)
        input(mensaje_volver_al_menu)
    else:
        opcion = ingresar_correcto(menu_principal (ruta,cantidad_recetas))
    if opcion == 8:
        finalizar_programa(ruta)
            
