# range(starting value, ending value, adds 2)
even_numbers = list(range(2,11,2))
print(even_numbers)

mylist = ["1", "1", "0", "3"]
for food in mylist:
    if food == "1":
        break
    print(food, end=" ")
