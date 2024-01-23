lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

tuplelist_indice=list(enumerate(lista_nombres)) #lista de tuples

for indice,nombre in tuplelist_indice:
    print(f'{nombre} se encuentra en el índice {indice}')