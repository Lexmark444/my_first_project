cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)


# compression is easier and faster yo
cubes = [value**3 for value in range (1,11)]
print(cubes)
