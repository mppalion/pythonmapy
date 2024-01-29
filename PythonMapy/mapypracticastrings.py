##String Assignment
"""String Assignment. (This can be tricky so feel free to watch solution so we can do it together)
- Ask the user how many days until their birthday
- Using the print()function. Print an approx. number of weeks until their birthday
- 1 week is = to 7 days."""

days= int (input("How many days are left until your bithday?")) ## 1era forma de convertir input en int
days = int(days) ## 2da forma de convertir input en int. Directamente a la variable.
weeks = int(days/7) ## así o con round: weeks = round(days/7)
print(f"there are {weeks} weeks left until your birthday")
