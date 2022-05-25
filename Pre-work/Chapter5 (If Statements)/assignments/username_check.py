current_users = ['admin', 'adam', 'will', 'josh', 'ethan']
for user in current_users:
    user = user.lower()

new_users = ['joely','adam','alyse', 'will','mit']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("You cannot use " + new_user.title() + ". Please try again.")
    else:
        print(new_user.title() + ", is available for use.")