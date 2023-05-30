my_foods = ["pizza", "fried chicken", "donuts", "Chocolate cake", "doritos"]

#This doesn't works it doesn't makes individual list
#friend_foods = my_foods

friend_foods = my_foods[:]

my_foods.append("coke")
friend_foods.append("hamburger")

print("My favourite food is:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favourite food is:")
for food in friend_foods:
    print(food.title())

print("\nThe first three items in the list: ")
print(my_foods[:3])

print("The three items from the middle of the list:")
print(my_foods[1:4])

print("The last three items from the list:")
print(my_foods[-3:])