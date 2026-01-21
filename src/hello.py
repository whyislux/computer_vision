name = "Hola mundo"
print(name)

#Built-in method input
user_name = input("¿Como te llamas?: ")
edad_txt = input("¡Cual es tu edad?: ")

print(user_name)
print(type(user_name))

print(edad_txt)
print(type(edad_txt))

try:
    edad = int(edad_txt)
    print(edad)
    print(type(edad))

except ValueError:
    print("Error: la conversión no se puede realizar")
    print("Debes ingresar un numero entero")

print("Fin del programa") 
