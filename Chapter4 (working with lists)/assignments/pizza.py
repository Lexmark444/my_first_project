pizzas = ['plain', 'broccoli', 'spinach']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append('pineapple')
friend_pizzas.append('pepperoni')

for pizza in pizzas:
    print(pizza)

print("\n")
for pizz in friend_pizzas:
    print(pizz)
