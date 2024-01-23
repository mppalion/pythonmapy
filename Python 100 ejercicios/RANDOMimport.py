from random import * 
"""#NO PONER MISMO NOMBRE AL FILE QUE LA LIBRERÍA QUE VAS A USAR!!!ES MUCHO MUY IMPORTANTE
#TAMBIEN PUEDE SER from random import randint si SOLO vas a usar este método de la libreria"""
aleatorio = (randint(1,51)) #INTEGER
print(aleatorio)

aleatorio_decimal = uniform(1,5) #FLOAT
print(aleatorio_decimal)

## UNIFORM() siempre lleva PARÁMETROS

aleatorio_decimal_redondeo = round(uniform(1,5),2) # con dos números decimales
print(aleatorio_decimal_redondeo) 

aleatorio_decimal_redondeo = round(uniform(1,10),1) # redondeo con UN número decimal
print(aleatorio_decimal_redondeo)

metodo_vacio_random = random()
print(metodo_vacio_random) # no lleva parámetros, imprime FLOAT random sin rango

# como randomizar una tabla

numbers_table = list(range(0,501,5))
shuffle(numbers_table)
print(numbers_table) #shuffle NO ES PARA STRINGS, porque son inmutables. SHUFFLE es una modificación in situ, en el lugar.

"""
dic= {"A": 257, "B":258, "C":259}
shuffle(dic)
print(dic.values()) """ #no se puede hacer shuffle de dic ni values ni keys. con listas si

aleatorio = randint (1,5) # incluye 5 randint especificamente ojo range NOO incluye el último número
print(aleatorio)


aleatorio1 = round(uniform(0,1),1)
print(aleatorio1)

aleatorio2 = round(random(),2) # EL MÉTODO RANDOM() ELIGE UN DECIMAL ENTRE 0 Y 1 PORQUE ASÍ ESTÁ DISEÑADO
print(aleatorio2)

lista = list(range(1,50,1))
elije_un_aleatorio_de_la_lista = choice(lista)
print(elije_un_aleatorio_de_la_lista)