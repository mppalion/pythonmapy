from clases import BankAccounts

cuenta1= BankAccounts(numbercbu=1000001726354263827311,holder="Maria Paula Palilon",balance_en_pesos=32000)
#Estos tres son "ATRIBUTOS" son propios de la cuenta, y de la clase, como la taza (brilla, tiene manija, es de cerámica)

print(type(BankAccounts))

print(type(cuenta1))

print(f"El balance de la cuenta es de {cuenta1.balance_en_pesos}")
print(f"el titular de la cuenta es: {cuenta1.holder}")
print(f"El Cbu de la cuenta es: {cuenta1.numbercbu}")

cuenta2=BankAccounts(1029273645192837465123,"Adrian Nestor Palilon", 52000)

print(f"El balance de la cuenta es de {cuenta2.balance_en_pesos}")
print(f"el titular de la cuenta es: {cuenta2.holder}")
print(f"El Cbu de la cuenta es: {cuenta2.numbercbu}")

#MÉTODOS, son los COMPORTAMIENTOS que puede hacer la clase, la taza sirve para tomar, para servir, para calentar en el microondas
#VERBOS, ACCIONES

cuenta1.depositar(40000,cuenta1.holder,cuenta1.numbercbu)
cuenta1.retirar(10000,cuenta1.holder,cuenta1.numbercbu)
cuenta1.transferir(30000,cuenta1.holder,cuenta1.numbercbu,cuenta2.balance_en_pesos,cuenta2.holder)
cuenta1.transferir(100000,cuenta1.holder,cuenta1.numbercbu,cuenta2.balance_en_pesos,cuenta2.holder)

print(cuenta1)
print(cuenta2)