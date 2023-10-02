##Desarrollo de programa que calcule el indice de masa Corporal

def input_altura():
    try:
        altura = float(input("ingresa tu estatura en metros: "))
        return altura, print(altura)
    except ValueError: 
        print("Los valores ingresados no son números intentelo nuevamente.")
        return input_altura()

def input_peso():
    try:
        peso = float(input("ingresa tu peso en Kilogramos: "))
        return peso, print(peso)
    except ValueError: 
        print("Los valores ingresados no son números intentelo nuevamente.")
        return input_peso()


def ingreso_de_datos():
##Ingresa la estatura y el peso del usuario.
##Returns:
##Una tupla con la estatura y el peso del usuario.
    altura=input_altura()[0]
    peso=input_peso()[0]
    return altura, peso, 

def calcular_imc():
  altura , peso = ingreso_de_datos()
  try:
    indice_masa_corporal = round(((peso/pow(altura,2))),2)
    mensaje_peso= get_mensaje_peso(indice_masa_corporal)
    return indice_masa_corporal, mensaje_peso, 
  except ValueError: 
    print("Los valores ingresados no son números.")
    return

def get_mensaje_peso(indice_masa_corporal):
  """Genera un mensaje de acuerdo al valor arrojado por la variable indice_masa_corporal
  
  :param _float_ indice_masa_corporal: _description_
  :return _string_: mensaje de acuerdo al valor recibido de la funcion 
  """

  if indice_masa_corporal < 18.5:
    return "Delgadez"
  elif indice_masa_corporal < 25:
    return "Normal"
  elif indice_masa_corporal < 30:
    return "Sobrepeso"
  elif indice_masa_corporal < 35:
    return "Obesidad grado I"
  elif indice_masa_corporal < 40:
    return "Obesidad grado II"
  else:
    return "Obesidad grado III"

def mensaje_final(indice_masa_corporal,mensaje_peso):
  """
  Purpose: mensaje final al calcular todo
  """
  print(f"Tu indice de masa corporal es:{indice_masa_corporal} esto esta categorizado como {mensaje_peso}")

indice_masa_corporal,mensaje_peso = calcular_imc()
mensaje_final(indice_masa_corporal,mensaje_peso)