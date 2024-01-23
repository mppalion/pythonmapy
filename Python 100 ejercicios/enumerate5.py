lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
index_list = list(enumerate(lista_nombres))
elemento = 0

for x,y in index_list:
    elemento = (y[0])
    if elemento =="M":
        print(x)

## Te imprime en pantalla los índices de la lista en los cuales los nombres comienzan con "M"