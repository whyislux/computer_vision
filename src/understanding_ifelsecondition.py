user_age = int(input("Ingresa tu edad: "))

if user_age < 0:
    print("Edad invalida")

elif user_age < 18:
    print("Eres menor de edad")

elif 18 <= user_age < 60:
    print("Eres un adulto")

elif 60 <= user_age < 100:
    print("Estás potencialmente muerto")

else:
    print("Es probable que RIP")