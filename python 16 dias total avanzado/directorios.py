from os import chdir
from os import getcwd
from os import makedirs

ruta = getcwd()

ruta = chdir("C:\\Users\\27369041881\\Documents\\Python\\python 16 dias total avanzado\\carpetaalternativapracticadirectorios")

print(ruta)

archivo = open("lo encontraste.txt","r")

print(archivo.read())


ruta_nueva = makedirs("C:\\Users\\27369041881\\Documents\\Python\\python 16 dias total avanzado\\esta_carpeta_es_nueva_y_la_creé_yo_misma_desde_python_con_el_modulo_makedirs_de_la_librería_os")
