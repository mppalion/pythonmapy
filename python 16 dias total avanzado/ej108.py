def describir_persona (nombre,**kwargs):
    print(f"características de {nombre}:")
    for key, values in kwargs.items():
        print(f"{key}:{values}")
        
describir_persona("maria",color_de_cabello="castaño",color_de_ojos="marrones")


