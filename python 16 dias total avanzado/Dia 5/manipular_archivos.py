archivo = open("prueba.txt")
a=archivo.read()
print(a)



# una vez que leyo se queda donde terminó por eso lo volvemos a abrir
archivo = open("prueba.txt")

una_linea = archivo.readline()
print(una_linea)

una_linea = archivo.readline()
print(una_linea.rstrip().upper())#saca el salto de línea por eso borra el espacio y después lo convierte a MAYUS

una_linea = archivo.readline()
print(una_linea)

archivo.close()

archivo_abierto = open("prueba.txt")

linea1 = archivo_abierto.readline()
linea2 = archivo_abierto.readline()

print(linea2)

archivo_abierto.close()

archivo= open("prueba.txt","a")
nueva_linea =  archivo.write("yo soy la cuarta linea\n")
archivo.close()

archivo= open("prueba1.txt","w")
nuevo_texto = archivo.write("yo soy un nuevo archivo")
archivo.close()