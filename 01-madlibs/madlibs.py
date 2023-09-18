# concatenar cadenas de texto
# supongamos que queremos crear una cadena que diga:
# Aprende a programr con ____________.

organizacion = "freeCodeCamp"

# codigo mas limpio
print("Aprende a programr con " + organizacion + ".")

# codigo utiliza un metodo llamado .format
print("Aprende a programr con {}.".format(organizacion))

# codigo no tan funcional
print("Aprende a programr con ", organizacion, ".")


# f.string
print(f"Aprende a programr con {organizacion}.")
