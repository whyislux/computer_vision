print("Este programa captura importes")
info = """
        Este programa lleva el conteo de cuantos importes ha introducido
        el usuario.

        Va acumulando todos los importes que el usuario ingresa

        Si el usuario desea terminar el programa puede escribir cualquier
        momento la palabra exit, quit, terminar.

"""

print(info)
conteo = 0
suma = 0.0
minimo = None
maximo = None

while True:
    user_message = """
    Ingresa tu importe (MXN)
    Si quieres dejar de capturar importes
    puedes ingresar en cualquier momento
    exit, quit, terminar:

    """
    line = input(user_message).lower()
    if line == "exit" or line == "quite" or line == "terminar":
        break

    try:
        value = float(line)
    except ValueError:
        print(" Valor invalido. Intenta de nuevo")
        continue

    conteo += 1
    suma += value

    if minimo is None or value < minimo:
        minimo = value

    if maximo is None or value > maximo:
        maximo = value

if conteo == 0:
     print("No se capturaron importes")

else: 
    print("="*32)
    print(f"La cantida de importes ingresados fue: {conteo}")
    print(f"La sumatoria de los importes fue: {suma}")
    print(f"El importe minimo fue: {minimo}")
    print(f"El importe maximo fue: {maximo}")

print("Programa finalizado")
