lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
lista_iniciales = []
elemento = 0
for i in lista_nombres:
    elemento = (i[0])
    if elemento =="M":
        lista_iniciales.append(elemento)

print(lista_iniciales)

index_list = list(enumerate(lista_iniciales))

print(index_list)

"""
# string which is to be stripped 
string = "++++x...y!!z* geeksforgeeks"
# Removes given set of characters from left. 
print(string.lstrip("+.!*xyz"))"""