my_pizzas = ['suprema', 'hawaiian', 'meat lovers', 'mexican']
friend_pizzas = my_pizzas[:]

my_pizzas.append("hawaiian chicken")
friend_pizzas.append("veggie")

print("This are my favourites pizzas: ")
for pizza in my_pizzas:
    print(pizza.title())

print("This are the favourite pizzas of my friend: ")
for pizza in friend_pizzas:
    print(pizza.title())
