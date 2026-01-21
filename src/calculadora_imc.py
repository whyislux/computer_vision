weight_txt = input("Peso (kg): ")
heigth_txt = input("Altura (m): ")

try:
    weight = float(weight_txt)
    height = float(heigth_txt)
    imc = weight / height**2
    print(f"Tu IMC es {imc}")

except (ValueError, ZeroDivisionError):
    print("Datos invalidos. Ej: Peso 70.5; altura 1.75")

