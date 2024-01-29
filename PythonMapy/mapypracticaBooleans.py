## COMPARISON OPERATORS
favorite_food ="pizza"
Do_I_like_pizza = True
number_of_pizza_slices_I_could_eat = 7

print(type(favorite_food)) ## type string
print(type(Do_I_like_pizza)) ## type Boolean
print(type(number_of_pizza_slices_I_could_eat)) ## type Integer

print(favorite_food == "olives") ##False
print(favorite_food != "olives") ##True
print(1<2) ##True
print(1<0.5) ##False

## LOGICAL OPERATORS

print(1<2 and 10<20) #TRUE
print(10<2 or 100<20) #FALSE
print(not(1==1)) #FALSE