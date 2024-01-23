def repite_ceroseguido (*args):
    lista = list(args)
    doscerosjuntos=False
    n=0
    while n < len(lista)-1:
        if lista[n] == 0 and lista[n+1]==0:
            doscerosjuntos=True
        n=n+1  
    return doscerosjuntos

print(repite_ceroseguido (20,0,1,0)) #TRUE
print(repite_ceroseguido (0,1,1,1)) #FALSE
print(repite_ceroseguido (1)) #FALSE
print(repite_ceroseguido (0,1,0,0,1,1,0,0)) #TRUE
print(repite_ceroseguido (0,1,1,1)) #FALSE

