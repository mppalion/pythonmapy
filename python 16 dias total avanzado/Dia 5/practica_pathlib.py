from pathlib import Path #Acá estamos importando el objeto Path
from pathlib import PureWindowsPath


carpeta = Path("C:/Users/27369041881/Documents/Repo-git-Mapi/Python/python 16 dias total avanzado/prueba1.txt")
#Este es un objeto

"""como se si es un método? ctrl+space despues del punto y aparece como una llave de tuercas (francesa)"""

"""como se si es un objeto? ctrl+space despues del punto y aparece como un cubito"""

print(carpeta.name) #al ser un método lo podes llamar sin (),
#.name te dice el nombre del archivo en forma completa

print(carpeta.suffix) 
#te dice la extensión en este caso .txt

print(carpeta.is_dir)
#Este te dice si es directorio y cual es el directorio. y directorio de que sistema operativo

print(carpeta.stem) #Este te dice nombre del archivo SIN EXTENSIÓN

print(carpeta.anchor) #Este te tira cual es la carpeta RAIZ, en este caso "C:\" barra invertida por que es WINDOWS

print(carpeta.drive) #Este te tira cual es la carpeta RAIZ, sin BARRA para cualquier OS (Sistema Operativo)

print(carpeta.parent)
print(carpeta.suffixes) # Extensión como elemento de una LISTA

print(carpeta.parts) # tupla con los elementos de todo el Path

print(carpeta.parts.__class__) #clase del elemento carpeta.parts (TUPLA)

print(carpeta.root) # este método te tira con que barra opera, en este caso, barra invertida de WINDOWS

if not carpeta.exists:
    print(f"La carpeta {carpeta.stem} NO existe")
else:
    print(f"Genial! El archivo {carpeta.name} existe y está en el directorio {carpeta.parent}")
    
ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)