favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() + 
    ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
    language.title() + ".")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

if 'eren' not in favorite_languages:
    print("Erin, please take our poll!")

# to loop in order do:  for name in sorted(dictionary_name.keys()):
#set(dictionary_name) makes the list print without repeats
for language in set(favorite_languages.values()):
    print(language.title())

# You can store multiple values for one key as a list
# ex:
# favorite_languages = { 'jen': ['python', 'ruby']}
