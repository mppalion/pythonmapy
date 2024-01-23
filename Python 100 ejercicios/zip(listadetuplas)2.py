capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

listoftuples_geography = list(zip(capitales,paises))

for x,y in listoftuples_geography:
    print(f"La capital de {x} es {y}")
   
##Lo mismo que decir:  
"""for paises,capitales in listoftuples_geography:
    print(f"La capital de {paises} es {capitalesw}")
    """
    
    ## OJO CON EL ORDEN DE LOS PARÁMETROS
    
marcas = ["coca cola", "manaos", "Del valle"]
productos =["sprite","cola de manaos","cepita"]

mi_zip = list(zip(marcas, productos))

for marcas, productos in mi_zip:
    print(f"la marca {marcas} fabrica el producto {productos}")
    
zip = mi_zip[0][1]
print(zip)