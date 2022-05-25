user = 'Lexmark'

print(user == 'Lexmark')
print(user != 'Lexmark')
print(user.lower() == 'lexmark')

bob = 18
will = 29

if will and bob >= 21:
    print("The boys can drink!")
else:
        print("The boys cannot go to the bar.")

if will or bob >= 21:
    print("Alcohol can be purchased for a house party.")

menu = [1,2,3,4]
if 2 in menu:
    print('yes')

if 5 not in menu:
    print("no")    

name = "bob"
if name == "bob":
    print ("Say my name, say my name", end=" ")
print("If no one is around you", end=" ")
if name:
    print("Say baby I love you", end=" ")
else:
    print("If oyu ain't runnin' game", end=" ")    

x = 5
if x == 5:
    print('yes')
elif x>=4:
    print('yesss')