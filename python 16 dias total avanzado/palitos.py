jfrom random import shuffle

palitos= ["-","--","---","----"]
intento = 0

def mezclar_palitos (palitos):
    shuffle(palitos)
    return palitos

def probar_suerte ():
    intento=0
    while intento not in["1","2","3","4"]:
        intento = input("Ingrese un número del 1 al 4: ")
    return int(intento)

def comprobacion(palitos,intento):
    if palitos[intento-1] == ("-"):
        print("A lavar los platos")
    else: 
        print("te salvaste")
    print(f"te tocó el palito {palitos[intento-1]}")
    
#list=[dog,cat,bird]
#a=list.index(cat)
#print(a) el output es 1
#b=list[1]
#print(b) el output es cat

mezclar_palitos(palitos)
comprobacion(palitos,intento = probar_suerte())