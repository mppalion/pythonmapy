
texto = str (input ("ingrese un texto: "))
letrasEleccion1 = ( input ("ingrese una letra a eleccion: ") )
letrasEleccion2 = ( input ("ingrese una segunda letra a eleccion: " ))
letrasEleccion3 = ( input ("ingrese una tercer letra a eleccion: "))

listaletras = [letrasEleccion1.lower(),letrasEleccion2.lower(),letrasEleccion3.lower()]

textominus = texto.lower()

listaminus = list (textominus)

lista_spliteada = texto.split()

print ("la cantidad de letras que figura son {} en el texto".format (len(listaminus)))
print ("la cantidad de palabras que figura son {} en el texto".format (len(lista_spliteada)))



print ("la letra {} figura {} veces en el texto".format(listaletras[0],listaminus.count(listaletras[0])))
#print (f"la letra {listaletras[0]} figura {listaminus.count(listaletras[0])} veces en el texto")
print ("la letra {} figura {} veces en el texto".format(listaletras[1],listaminus.count(listaletras[1])))
print ("la letra {} figura {} veces en el texto".format(listaletras[2],listaminus.count(listaletras[2])))

lista = list(texto)
print ("la ultima letra del texto es:  {} y la primera letra es: {}".format(lista[0],lista[-1]))

print(lista_spliteada)

#listaJuntaReversada = lista_spliteada.sort(key=len, reverse=True)

#print(listaJuntaReversada)

#reversada ="".join(listaJuntaReversada)

#print(reversada)

estapython = "Python" in texto
dic_estapython = {True:"si esta en el texto", False:"no esta en el texto"}
print("la palabra Python {}".format (dic_estapython[estapython]))

