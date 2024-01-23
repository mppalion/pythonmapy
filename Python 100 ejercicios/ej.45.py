"""► Enunciado:Convertir una lista de caracteres en una cadena.
► Entrada:
['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t']
► Salida:
abcdefghijklmnopqrst
► Ayuda:
La función join() convierte una lista en una cadena formada por los elementos de la lista separados por comas.
Para empezar, consideremos la siguiente lista:
paises = [  'Argentina', 
            'Uruguay', 
            'Chile', 
            'Paraguay',
            'Brasil',
            'Bolivia' ]
Si deseamos convertir esta lista en una cadena de texto, utilizaremos la función join() de la siguiente manera:
‘separador‘.join(paises)
Donde separador representa el o los caracteres que deseamos utilizar como delimitadores, para separar un elemento de otro, en la cadena texto.
paises = [  'Argentina',
            'Uruguay',
            'Chile', 
            'Paraguay',
            'Brasil', 
            'Bolivia' ]
            
paisesString = ','.join(paises)
print(paisesString)"""