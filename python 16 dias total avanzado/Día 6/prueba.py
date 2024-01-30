from pathlib import Path
from os import system

archivo= Path.home()

ruta = Path(Path.home(), "Documents", "PythonMapy", "pythonmapy", "python 16 dias total avanzado","Día 6","Recetas")
print(archivo)
print(type(ruta))
print(ruta)

for txt in ruta.glob("**/*.txt"):
    print(txt.stem)
    
print("__")
    
for txt in ruta.glob("*/**"):
    print(txt.stem)
    
hola="carnes"
ruta_mas_profunda = Path(ruta,hola)
print(ruta_mas_profunda)
ruta_mas_mas_profunda = Path(ruta_mas_profunda,"Entrecot al Malbec.txt")
print(ruta_mas_mas_profunda.open().read())

def listar_categorias (ruta):
    lista=[]
    for child in ruta.iterdir():
        lista.append(child.name)
    return lista

print(listar_categorias(ruta))

"""def listar_recetas (ruta):
    for txt in ruta.glob("**/.txt"):
        print(txt.stem)
        
def listar_categorias (ruta):
    for txt in ruta.glob("*/**"):
        print(txt.stem)
"""