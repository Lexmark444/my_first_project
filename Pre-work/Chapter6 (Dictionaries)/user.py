user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


my_dict = {"age":14}
my_dict.update({"age":54})
print(my_dict["age"])