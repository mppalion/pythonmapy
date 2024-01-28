vendedor = (input("Ingresa el nombre del vendedor a consultar:"))
ingresos = (input("ingresa los ingresos del vendedor"))
comision = (int(ingresos))*13/100
comisiondosde = round(comision,2)
print ("la comisión de {} es igual a {}".format(vendedor,comisiondosde))