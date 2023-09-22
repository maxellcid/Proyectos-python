# escribir un programa que adivine un numero sugerido por el jugador

import random


def adivina_el_numero_computadora(x):

    print("¡Bienvenido(a) al juego! ")
    print(
        f"selecciona un numero entre 1 y {x} para  adivinarlo.")

    limite_inferior = 1
    limite_superior = x
    respuesta = ""

    while respuesta != "c":
        # Generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
            # tambien podria ser el limite superior
            # obtener respuestas del ususario
        respuesta = input(
            f"mi prediccion es {prediccion}. Si es muy alta,ingresa (A). Si es muy baja, Ingresa (B). si es correcta, ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(
        f"Felicitaciones la computadora adivino tu numero correctamente: {prediccion}")


adivina_el_numero_computadora(100)
