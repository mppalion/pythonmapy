
def es_primo (num):
    if num==0 or num==1:
        return False
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True

print(es_primo(4))

def listar_primos (num):
    listado = []
    for i in range(2,num):
        if es_primo(i) == True:
            listado.append(i)
    return listado
    
print(listar_primos(25))

 



            

    
"""Esta función va a mostrar en pantalla todos los números 
primos existentes en el rango que va desde cero hasta ese 
número incluido, y va a devolver la cantidad de números 
primos que encontró."""