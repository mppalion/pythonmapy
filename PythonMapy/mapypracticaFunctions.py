def my_function ():
    print("Esta es mi función, que no hace nada hasta que la llame...")
    
my_function ()
print ("y puesto a que se visualiza, la he llamado")

def print_my_name(name,message):
    print(f"Hello, my name is {name} and my message is :{message}")

print_my_name("mapy","Life has many responsabilities and I am just tired") ## llamo a la función con el parámetro que falta

## internal/local variables present only to the function (dentro de la función)
## Global variables accesible by the entire application (afuera de la función)

def print_color_red():
    color ="red" ## Variable INTERNA o LOCAL
    print(color)

color ="blue" ## variable GLOBAL
print(color)
print_color_red()

def print_numbers (highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

print_numbers(10,3)

print_numbers(highest_number=7, lowest_number=1)

def multiply_numbers(a,b):
    return a * b

a=8
b=5

solution = multiply_numbers(a,b)
print(solution)
print(f"the solution of the multiply function between a and b is {solution}")

def print_list(list_of_numebers):
    for x in list_of_numebers:
        print(x)

numbers_list=[1,2,3,4,5]

print_list(numbers_list)
###############################################################

def buy_item(cost_of_item):
    return(cost_of_item + add_tax_to_item (cost_of_item))

def add_tax_to_item (cost_of_item):
    current_tax_rate =0.03
    tax=cost_of_item*current_tax_rate
    return tax

final_cost = buy_item(10)
print(final_cost)

###############################################################

"""- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values"""

def identities(firstname,lastname,age): ### el valor se lo va a pasar despues el usuario por eso el PARÁMETRO ES VALUE que le pasamos, la KEY ES FIJA
    create_dic_identities = {
        "firstname": firstname, ## KEY es fija, valor es lo que le vamos a pasar
        "lastname":lastname, 
        "age":age}
    return create_dic_identities

soluction_dictionary = (identities(firstname="Frodo",lastname="Baggins",age=550))

for x,y in soluction_dictionary.items():
    print(x,y)

