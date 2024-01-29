my_list = ["mapy", "graciela", "adrian", "adriancito"]
print(my_list[1])
print(my_list[-4])
print(len(my_list))

print(my_list[0:2]) ## slicing imprime segmentando la lista, en este caso dos elementos seguidos de la lista
print(my_list[0:3])

my_list.append ("Gonzalo") ##append agrega al final parámetro QUÉ AGREGA
print(my_list[4])

my_list.insert(5,"Marina") #2 parámetros, EN QUé LUGAR (indice) y QUÉ SE INSERTA
print(my_list)
## esto no se puede hacer print(my_list.insert(5,"marina") primero se inserta luego se imprime porque primero imprime

my_list.remove("Marina") ## PARÁMETROS QUÉ SACA, NO ÍNDICE
print(my_list)

my_list.pop() ##si no ponés argumento saca el últimoooo SIEMPRE EL ÚLTIMO SINO PONÉS PARÁMETROS
print(my_list)

my_list.pop(3) #solo 1 argumento
print(my_list)

my_list.sort()
print(my_list)


"""- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals"""

zoo = ["lemur","python","tigre de bengala", "elefante", "girafa"]
print(zoo)
zoo.pop(3)
print(zoo)
zoo.append("leon")
print(zoo)
zoo.remove("lemur") ## zoo.pop(0)
print(zoo)

print(zoo[0:3])
"""  o también:
for i in zoo:
print(i)"""


