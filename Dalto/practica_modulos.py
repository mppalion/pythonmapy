import sys
from modulo_saludar import saludar as saludar_informalmente,saludar_formal

saludo=(saludar_informalmente("mapy".capitalize()))

saludo_formal = (saludar_formal("compañeros"))

print(saludo+"\n")
print(saludo_formal)



print(sys.path)