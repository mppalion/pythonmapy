#cuentas bancarias
class BankAccounts ():
    def __init__(self,numbercbu, holder,balance_en_pesos=0):
        print("A new bank account was created")
        self.numbercbu= numbercbu #ATRIBUTO
        self.holder= holder #ATRIBUTO
        self.balance_en_pesos=balance_en_pesos #ATRIBUTO
    
    def depositar(self,dinero,holder,numbercbu):
        self.balance_en_pesos= self.balance_en_pesos+dinero
        print(f"se han depositado ${dinero} quedando un balance de ${self.balance_en_pesos}\n de la cuenta {numbercbu} perteneciente a {holder}")
        return self.balance_en_pesos
        
    def retirar (self,dinero,holder,numbercbu):
        if self.balance_en_pesos>=dinero:
            self.balance_en_pesos=self.balance_en_pesos-dinero
            print(f"se han retirado ${dinero} quedando un balance de ${self.balance_en_pesos}\n de la cuenta {numbercbu} perteneciente a {holder}")
        else: 
            print("No hay saldo suficiente para realizar la transacción")
        return self.balance_en_pesos
    
    def transferir (self,dinero,holder,numbercbu,saldo_destinatario,cuenta_destinatario):
        if self.balance_en_pesos>=dinero:
            self.balance_en_pesos=self.balance_en_pesos-dinero
            saldo_destinatario=saldo_destinatario+dinero
            print(f"Se han transferido ${dinero} de la cuenta {numbercbu} perteneciente a {holder} a la cuenta de destinatario {cuenta_destinatario}")
        else: 
            print("No hay saldo suficiente para realizar la transacción")    
            
    def otro_comportamiento (self):
        pass
    
    def __str__(self):
        return f"Datos de la cuenta Bancaria: \n Titular: {self.holder},\n Número de CBU:{self.numbercbu} \n Saldo a la fecha: {self.balance_en_pesos}"