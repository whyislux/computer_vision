names = []
print(names)

#Metodo .append para agregar elementos al final de la lista
names.append("Charly")
names.append("Mar")
names.append("Alexis")
names.append("Erick")
names.append("Jona")
names.append("Arce")

print(names)
print(type(names))
print(len(names))

#Metodo .insert para agregar elementos en una posición deseada
names.insert(1, "Hector")
print(names)

#Metodo .pop sin indice para eliminar el ultimo elemento de la lista
names.pop()
print(names)

#Metodo .pop con indice para eliminar un elemento deseado con la posicion indice
names.pop(2)
print(names)

cars = ['bmw', 'bocho']
prices = [5,1]
print(cars)
print(cars[0])
print(f"Mi primer carro fue un {cars[0]}")

for car in cars:
    print(f"Mi primer carro fue un {car}")

for ind,value in enumerate(cars):
    print(ind,value)

for car,price in zip(cars,prices):
    print(car,price)