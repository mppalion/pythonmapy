hour= 16
if (hour < 13):
    print("Good Morning!")
elif (hour>=13 and hour<18 and hour>=6):
    print("Good Afternoon!")
else:
    print("Good Night!")
        
##<
##<

"""- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable
Grades:
A = 90 - 100
B = 80 - 89"""

calification = 100
if (calification <= 100):
    print("Grade:A")
elif (calification <= 89 and calification > 80):
    print("Grade:B")
else:
    print("Grade:C")
