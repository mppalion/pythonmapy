"""► Enunciado:
Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente, 
para ello solo necesita establecer el precio de su trabajo por hora.
Se estiman 40 horas de trabajo a la semana.
Las Fórmulas para calcular el pago Semanal y Mensual son:
1) Pago_Semanal = (DolaresPorHora x 40)
2) Pago_Mensual = (DolaresPorHora x 160)
___
► Variables:
Dolares_Por_Hora: Cantidad de Dólares que gana el Freelancer por hora.
Pago_Semanal: Almacena el resultado del pago semanal."""


Dolares_Por_Hora = int(input("Ingrese la cantidad de dólares que gana por hora: ")) #SIEMPRE INT o FLOAT PORQUE INGRESA COMO STRING
#SIEMPRE INT o FLOAT PORQUE INGRESA COMO STRING
sPago_Semanal = 0
Pago_mensual = 0

def Pago_semanal_funcion (Dolares_Por_Hora):
    Pago_Semanal = (Dolares_Por_Hora*40)
    return Pago_Semanal

def Pago_mensual_funcion (Dolares_Por_Hora):
    Pago_mensual = (Dolares_Por_Hora*160)
    return Pago_mensual

print(f"si ganas {Dolares_Por_Hora} USD por hora, entoncés ganarás {Pago_semanal_funcion (Dolares_Por_Hora)} USD por semana y {Pago_mensual_funcion (Dolares_Por_Hora)} USD por mes")


    


