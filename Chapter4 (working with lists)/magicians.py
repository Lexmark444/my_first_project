magicians = ['alice', 'david', 'carolina', 'krishna', 'zammam']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

print('The first three magicians are:')
for magician in magicians[0:3]:
    print(magician.title())

print('The middle three magicians are:')
for magician in magicians[1:4]:
    print(magician.title())

print('The last three magicians are:')
for magician in magicians[-3:]:
    print(magician.title())    