
def alphabetic_order (word):
    mi_set = set()
    for letra in word:
            mi_set.add(letra)
    lista = list(mi_set)
    lista.sort()
    return lista

print(alphabetic_order("cococos"))