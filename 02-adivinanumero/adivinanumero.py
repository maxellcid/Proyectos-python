# crear un programa que arroje un numero al azar para que el jugador lo adivine

import random


def adivina_el_numero(x):
    print("¡Bienvenido al Juego Adivina el Numero!")
    print("tu meta es adivinar el numero generado por la computadora.")
    # numero aleatorio entre 1 y x
    numero_aleatorio = random.randint(1, x)
    prediccion = 0

    while prediccion != numero_aleatorio:
        # El usuario ingresa numero
        # f-string el numero recibido es convertido a entero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}:"))
        if prediccion < numero_aleatorio:
            print("intenta nuevamente, este numero es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("intenta nuevamente, este numero es muy grande.")

    print(
        f"¡Felicitaciones Adivinaste el numero {numero_aleatorio} correctamente!")


adivina_el_numero(10)
# pendiente correcion en caso de que el jugador escriba letras o no escriba nada
