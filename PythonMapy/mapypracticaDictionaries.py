user_dictionary = {"username":"mapy", "name":"Maria Paula", "age": "31"}
print(user_dictionary)

print(user_dictionary.get("age")) ##Get the value of the key

user_dictionary ["Apellido"] = "Palilon" ## agregar claves y valores al diccionario

print(len(user_dictionary))#len te tira la cantidad de claves

user_dictionary.pop("username") #borrar key y value del diccionario, solo con pop y solo con la key

print(user_dictionary)

user_dictionary.clear() ##ELIMINAR EL DICCIONARIO, es igual que hacer del user_dictionary
##del user_dictionary ni siquiera te lo muestra vacio, si querés imprimirlo re va a tirar error
print(user_dictionary)

user_dictionary = {"username":"mapy", "name":"Maria Paula", "age": "31"}
for i in user_dictionary:
    print(i) ## solo te imprime KEYs
for x,y in user_dictionary.items():
    print(x,y) ## solo te imprime KEYs
## SI TOCAS UNA VARIABLE CON EL CONTENIDO DE UN DICCIONARIO MODIFICA TODOS LOS DICCIONARIOS ORIGINALES
## Por eso tenés que hacer 
user_dictionary2= user_dictionary.copy() ##SHALLOW COPY OJO siempre ASÍ
user_dictionary.pop("age")
print(user_dictionary2)

"""Based on the dictionary:
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values
- Create a new variable vehicle2, which is a copy of my_vehicle
- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- Delete the mileage key and value from vehicle2
- Print just the keys from vehicle2"""

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x,y in my_vehicle.items():
    print(x,y)

vehicle2= my_vehicle.copy()

vehicle2["number_of_tires"] = 4

vehicle2.pop("mileage")
print(vehicle2)

for x in vehicle2: ##imprime solo la llave
    print(x)
    
for x,y in vehicle2.items(): ## imprime llave y valor
    print(x,y)