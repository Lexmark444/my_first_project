alien_0 = {'color':'green','points' : 5 }
print (alien_0)

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print (alien_0)

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Move alien to the right
# Determine how far to move based on current speed
alien_0['speed'] = 'medium'
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# to delete a pair from dictionary just del alien_['points']
