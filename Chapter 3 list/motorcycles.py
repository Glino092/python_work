motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#Cambiar valor de cualquier elemento de la lista
#motorcycles[0] = 'ducati'

#agregar elemntos al final de la list
#motorcycles.append('ducati')

#agregar elementos en cualquier posición en una lista
#motorcycles.insert(0, 'ducati')

#Eliminar un  elemento de una lista
#del motorcycles[0]

#Elimiar un elemento de una lista con el metodo pop() para despues trabajar con el, se puede seleccionar el elemento a borrar.
# last_owned = motorcycles.pop()
# print(f"The last motorcycle that I owned was a {last_owned.title()}.")
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle that I owned was a {first_owned.title()}.")

#Remover unelemento de la lista por su valor .remove()
too_expensive = ('ducati')
motorcycles.remove(too_expensive)
print(f"\n The {too_expensive.title()} is too spensive for me!")

print(motorcycles)