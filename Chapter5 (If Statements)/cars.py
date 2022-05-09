cars = [ 'audi','bmw', 'subaru','toyota']

for car in cars:
    # if case doesn't matter do car.lower() == 'bmw":
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
