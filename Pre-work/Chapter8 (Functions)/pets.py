def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# order matters when you call the function,
# unless you define the parameter assignments

describe_pet('hamster', 'harry')
describe_pet(animal_type = 'dog', pet_name = 'willie')