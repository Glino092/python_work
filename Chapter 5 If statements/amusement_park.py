age = 16
if age < 4:
    price = 0
    #print("Your admision cost is: $0")
elif age < 18:
    price = 25
    #print("Your admision cost is: $25")
elif age < 65:
    price = 40
else:
    price = 20
    #print("Your admision cost is: $40")

print(f"Your admision cost is: {price}.")