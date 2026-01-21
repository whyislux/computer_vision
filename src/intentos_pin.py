"""
    Este programa va a pedir al usuario su pin de acceso.

    1) Si el pin es correcto entonces el programa debe decirle
    autenticacion exitosa, acceso concedido.

    2)Si el pin es incorrecto, entonces el programa debe decirle
    pin incorrecto y el numero de intentos que le quedan.

    3)Si el usuario supera el numero de intentos permitidos
    el programa le va a decir numero de intentos superados y 
    cuenta bloqueada.
"""

PIN_CORRECTO = "1234"
INTENTOS_MAX = 3
intentos = 0

while intentos < INTENTOS_MAX:
    entrada = input("Ingresa tu pin (4 digitos): ")
    if entrada == PIN_CORRECTO:
        print("Autenticación exitosa, acceso concedido.")
        break

    else:
        intentos += 1
        restantes = INTENTOS_MAX-intentos
        if restantes > 0:
            print(f"Pin incorrecto, te quedan {restantes} intentos")

        else:
            print("PIN INCORRECTO. CUENTA BLOQUEADA")