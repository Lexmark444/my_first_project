name = "ada lovelace"

# useful methods lower and upper for taking user generated
# data and making it not case sensitive

print(name.title())
print(name.upper())
print(name.lower())

# concatenation A = B + C
first_name ="ada"
last_name ="lovelace"
full_name = first_name + " " + last_name
print(full_name)

# this is how games and forms add a personal touch :)
print("Hello, " + full_name.title() + "!")

greeting = "Hello, " + full_name.title() + "!"
print(greeting)

# \t = tab in text outputs
print("Python")
print("\tPython")

# \n = enter in text outputs
print("oranges\n\tare\n\t\tgreat!")

# you can remove whitespace wiht x.rstrip() and reassign the data as x = x.rstrip()
# x.lstrip() removes from left and x.strip() removes from both sides
fav_language = "python "
print(fav_language + "!")
print(fav_language.rstrip() + "!")
fav_language = fav_language.rstrip()
print(fav_language + "!")

