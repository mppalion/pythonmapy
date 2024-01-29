##SET lo mismo que LISTA pero NO SE PUEDE REPETIR EL CONTENIDO EJEMPLO:
my_set = {"mapy","Adrian", "Graciela", "Adriancito","Adrian"}
## te los da ordenados
print(my_set)
#si repetís lo borra UNIQUE VALUES
print(len(my_set))
##tampoco te da el largo del set completo si tenes valores repetidos, te lo da con valores únicos
for i in my_set:
    print(i)
## PERO EL SET No se puede imprimir por índice porque no sabe donde lo ordenó pero lo trae ordenado
## NO SE PUEDE HACER print(my_set[1])

## si se puede descartar
my_set.discard("mapy")
print(my_set)

my_set.clear()##borra todo el SET
print(my_set)

my_set.add("marina") ##agrega
print(my_set)

## SOLO PARA VALORES NUMÉRICOS
"""my_set.update(5,6,7,8)
print(my_set)"""