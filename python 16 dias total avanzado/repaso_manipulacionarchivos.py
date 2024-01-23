"""mi_archivo = open("prueba.txt")

lectura = mi_archivo.read()
print(lectura.strip())

mi_archivo.close()


mi_archivo = open("prueba.txt","w")

lectura = mi_archivo.write("Ahora si borré todo y soy el nuevo texto")

print(lectura)

mi_archivo.close()

"""
"""

nuevo_archivo = open("nuevo archivo.txt","r")


nuevo = nuevo_archivo.read()

print(nuevo)

nuevo_archivo.close()
"""
"""
nuevo_archivo = open("nuevo archivo.txt","a")
nuevo_archivo.write("\nBueno voy a escribir algo nuevo,\n")
nuevo_archivo.write("soy un nuevo archivo y voy a vivir")
print(nuevo_archivo)
nuevo_archivo.close()"""

"""
abrir_miarchivo= open("mi_archivo.txt","w")
abrir_miarchivo.write("Nuevo Texto\n")
abrir_miarchivo.close()
leer_miarchivo = open("mi_archivo.txt","r")
print(leer_miarchivo.read())
leer_miarchivo.close()
"""
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
nuevo_registro = open("registro.txt","a")
for i in registro_ultima_sesion:
    nuevo_registro.writelines(i +"\t")
nuevo_registro.close()

leer_registros= open("registro.txt","r")
print(leer_registros.read())
leer_registros.close()