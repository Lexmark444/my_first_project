users = ['admin', 'adam', 'will', 'josh', 'ethan']

if users:
       for user in users:
            if user == 'admin':
                print("Hello " + user.title() + ', would you like to see a status report?')
            else:
                print("Hello " + user.title() + ', thank you for logging in again.')
else:
    print("We need more users!")    