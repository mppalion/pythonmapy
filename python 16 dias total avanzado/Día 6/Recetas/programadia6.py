from pathlib import Path
archivo= Path.home()
ruta =Path(Path(archivo).glob ("**/Matambre a la Pizza.txt"))

cantidad_recetas=0

def menu_principal (archivo,cantidad_recetas):
    print(f"Bienvenido al Recetario joven!!\n Las rutas de acceso están en:{archivo}")
    print("Existen {cantidad_recetas} recetas en total en este hermoso Recetario")
    print("Ingresa una de las siguientes opciones: ")
    print("[1] leer la Receta \n [2] Crear Receta \n [3] Crear Categoría \n [4] Eliminar Receta \n [5] Eliminar Categoría \n [6] Finalizar Programa" )

ingreso= input("Ingresa una de estas opciones listadas:")

def ingreso_erroneo (ingreso):
    while ingreso != ["1","2","3","4","5","6"]:
        ingreso = input ("Ingresaste una opción incorrecta, por favor vuelve a intentarlo nuevamente")
    else:
        return True

while ingreso_erroneo(ingreso) == True:
    
    def leer_receta ():
        elegir = input("Elige la categoría que más te guste: ")
        ruta =Path(Path(archivo).glob ("Recetas"))
        
    """    
    def Crear_Receta ():
        
    def Crear_Categoria ():

    def Eliminar_Receta ():

    def Eliminar_Categoria ():

def Finalizar_Programa(ingreso,archivo):
    if ingreso == "6":
        confirmaciónsalir = input("Deseas finalizar el programa? y/n")
        if confirmaciónsalir == "n":
            menu_principal(archivo)
        else:
            print("Gracias por haber ingresado al Recetario. Hasta Pronto!")
            
    else:
        return menu_principal(archivo)
        
"""
    
