nombres = ["carlos", "maria", "teresa", "alicia"]
print(min(nombres))  #la palabra que empieza con la letra mas cercana del alfabeto en un MIN(LISTA) de una lista

numeros = [42,2,6,2,9,3457,1,-1]
print(max(numeros))

nombres = "carlos"

print(max(nombres)) #la letra mas lejana del alfabeto en un STRING

nombres = "Maria"
print(min(nombres)) #primero cuenta mayúsculas

nombres = "maRia"
print(min(nombres.lower())) ##lo paso primero a lower case

#DICCIONARIOS

dic= {"A": 257, "B":258, "C":259}
print(min(dic)) #imprime la clave MAS BAJA, no tiene en cuenta el VALOR
print(min(dic.values())) # imprime la VALOR MÁS BAJO
print(min(dic.values())) # imprime la VALOR MÁS BAJO