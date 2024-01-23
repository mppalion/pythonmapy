""" Une dos listas, creando una lista de tuplas""" #QUE TENEMOS QUE CASTEAR EN UNA LISTA

nombres = ["Juan", "Pablo", "Ana"]
edades = [12, 18, 22]
origen = ["Suecia","Noruega", "Suiza"]

combinado = list(zip(nombres,edades,origen))

print(combinado)

for nombres,edades,origen in combinado:
    print(f"{nombres} tiene {edades} años y su origen es de {origen}")

## TENEMOS QUE CASTEARLO SIEMPRE ADENTRO DE UNA LISTA SINO NO SIRVE EL ZIP
# list(zip(nombres,edades) arrojaría: [("Juan",12),("Pablo",18),("Ana",22)]

"""LISTA=[]
#TUPLAS = ()"""


español = ["uno","dos","tres","cuatro", "cinco"]
portugues = ["um","dois","três", "quatro", "cinco"]
ingles = ["one","two","three","four","five"]

numeros = list(zip(español,portugues,ingles))

print(numeros)