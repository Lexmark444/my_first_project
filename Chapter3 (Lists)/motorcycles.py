motorcycles = ['yamaha', 'suzuki', 'honda']
# to insert do listname.inset(location, what you want to add)
motorcycles.insert(0, 'ducati')
print(motorcycles)
# to delete use del listname[location]
del motorcycles[0]
print(motorcycles)
# this pop() method removes alst item off list
# you can also do pop(1) to remove second item in a list
popped_motorcycles = motorcycles.pop()
print (motorcycles)
print(popped_motorcycles)
# if you dont know the location use listname.remove('what to remove')
motorcycles.remove('suzuki')
print(motorcycles)
