# concatenar cadenas de texto
# supongamos que queremos crear una cadena que diga:
# Aprende a programr con ____________.

organizacion = "freeCodeCamp"

# codigo mas limpio
print("Aprende a programar con " + organizacion + ".")

# codigo utiliza un metodo llamado .format
print("Aprende a programar con {}.".format(organizacion))

# codigo no tan funcional
print("Aprende a programar con ", organizacion, ".")


# f.string
print(f"Aprende a programar con {organizacion}.")

# Mad Libs

adj = input("Adjetivo: ")
verbo1 = input("verbo: ")
verbo2 = input("verbo: ")
sustantivo_plural = input("Sustantivo plural: ")


madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas.¡aprende a {verbo2} con Freecodecamp y alcanza tus {sustantivo_plural}!"

print(madlib)
