dic = {"key1":200,"key2":300, "key3":400}

print(dic.popitem())
print(dic)

print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:_#"))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)

print(conjuntos_aislados)

a =list(marcas_tv)
a.extend(list(marcas_smartphones))
print(a)

def invertir_palabra (caracteres):
    var_invertir = ""
    for i in caracteres:
        var_invertir = i + var_invertir
    return var_invertir.upper()
    
palabra = invertir_palabra ("Python")
print(palabra)
