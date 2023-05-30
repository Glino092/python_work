#how to acces to a part of the list
players = ['charles', 'marina', 'florence', 'eli']
#print(players[-3:])
print("Here are the three first players on my team")
for player in players[:3]:
    print(player.title())