#Ejercicios finales  de agregar, modificar y eliminar elementos de listas

guests = ['sebastian', 'wendy', 'edwin', 'franciso']

print(f"Hola {guests[0].title()}, te gustaria que fueramos a cenar en la semana?")
print(f"Hola {guests[2].title()}, saka!!!!")
print(f"Hola {guests[1].title()}, te gustaria que pasaramos la noche juntos e ir a cenar?")
print(f"Que tranza {guests[3].title()}, vamos a jugar COD!!!!")
print(f"Numero de invitados cenar: {len(guests)}")
print("End of the firt part. \n")

del guests[3]
new_guest = 'miguel'
guests.insert(3, new_guest)
print(f"Hola {guests[0].title()}, te gustaria que fueramos a cenar en la semana?")
print(f"Hola {guests[2].title()}, saka!!!!")
print(f"Hola {guests[1].title()}, te gustaria que pasaramos la noche juntos e ir a cenar?")
print(f"Que tranza {guests[3].title()}, vamos a jugar COD!!!!")
print(f"Numero de invitados cenar: {len(guests)}")
print("We got a bigger table for the dinner. \n")

first_guest = 'maria'
middle_guest = 'rodrigo'
last_guest = 'scarlett'
guests.insert(0, first_guest)
guests.insert(2, middle_guest)
guests.append(last_guest)
print(f"Iremos a cenar {guests[0]}")
print(f"Iremos a cenar {guests[1]}")
print(f"Iremos a cenar {guests[2]}")
print(f"Iremos a cenar {guests[3]}")
print(f"Iremos a cenar {guests[4]}")
print(f"Iremos a cenar {guests[5]}")
print(f"Iremos a cenar {guests[6]}")
print(f"Numero de invitados cenar: {len(guests)}")
print("We lost the big table so I can only invite two people\n")

uninvited_1 = guests.pop(0)
uninvited_2 = guests.pop(1)
uninvited_3 = guests.pop(1)
uninvited_4 = guests.pop(1)
uninvited_5 = guests.pop(1)
print(f"Numero de invitados cenar: {len(guests)}")

print(f"Lo siento {uninvited_1.title()} ,no podremos ir a cenar, lo dejamos para otra ocación")
print(f"Lo siento {uninvited_2.title()} ,no podremos ir a cenar, lo dejamos para otra ocación")
print(f"Lo siento {uninvited_3.title()} ,no podremos ir a cenar, lo dejamos para otra ocación")
print(f"Lo siento {uninvited_4.title()} ,no podremos ir a cenar, lo dejamos para otra ocación")
print(f"Lo siento {uninvited_5.title()} ,no podremos ir a cenar, lo dejamos para otra ocación")

print(f"Ahora si vamonos a cenar, {guests[0].title()} y {guests[1].title()}")
print(f"Numero de invitados cenar: {len(guests)}")
del guests[0]
del guests[0]
print(guests)
print(f"Numero de invitados cenar: {len(guests)}")
