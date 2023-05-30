foods = ("hotcakes", "chilaquiles", "scrambled eggs", "oatmeal", "waffles")
print("This is the original menu: ")
#Tuples ar unmutabble so you can not modify them unless you reassigne the 
# complete tuple
#plates[1] = "enchiladas"
for food in foods:
    print(food)

foods = ("hotcakes", "waffles", "chilaquiles", "scrambled eggs", "quesadillas")
print("\nThis is the new buffet menu:")
for food in foods:
    print(food)