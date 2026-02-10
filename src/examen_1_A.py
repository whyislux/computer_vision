##Problema 2
weight_kg = float(input("Introduce tu peso en kg: "))
height_m = float(input("Introduce tu estatura en metros: "))
underweight = False
normal = False
overweight = False
try:
    # Indice de masa corporal
    bmi = weight_kg / (height_m * height_m)
    
    if weight_kg == 0: print("No se puede calcular, valor de peso invalido")

    if bmi <18.5 : underweight = True 
    if 18.5 <= bmi < 25 : normal = True
    if bmi >= 25 : overweight = True
    
    print(f'BMI : {bmi}')
    print(f'Underweight: {underweight}')
    print(f'Normal: {normal}')
    print(f'Overweight: {overweight}')

except ZeroDivisionError:
    print("Error: Invalid input")

#Problema 5
def calculate_area (width, heigth):
    area_rectangle = width * heigth
    print(f'El área del rectangulo es: {area_rectangle}')

def perimeter(width, heigth):
    perimeter_rectangle = (heigth * 2) + (width * 2)
    print(f'El perimetro del rectangulo es: {perimeter_rectangle}')

width_t = float(input('Da el ancho de tu rectangulo: '))
heigth_t = float(input('Da el largo de tu rectangulo: '))

if width_t or heigth_t != 0:
    calculate_area(width_t, heigth_t)
    perimeter(width_t, heigth_t)

if width_t == 0 or heigth_t == 0:
    print('Error: invalid input')
