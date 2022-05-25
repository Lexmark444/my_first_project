places = [item for item in range (1,10)]

for place in places:

    if place == 1:
        print(str(place) + "st")

    elif place == 2:
        print(str(place) + "nd")

    elif place == 3:
        print(str(place) + "rd")
        
    elif place > 3:
        print(str(place) + "th")

