players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 0:3 denotes vlaues 0-2, :2 denotes 0-1, 2: denotes 3-end of list
# -3: denotes last three items in list

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
