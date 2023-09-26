# crear un programa que ralize la conversion de un valor indicado por el ususario de celcius a farenheit y viceversa
Temperatura = float(input("Ingrese Temperatura a Convertir:"))
tipoDeGrados = input("Es Fahrenheit (F) o es Celsius(C)=:").lower()
if tipoDeGrados == "c":
    fahrenheit = (Temperatura * 9/5 + 32)
    print(fahrenheit, "°F")
elif tipoDeGrados == "f":
    celsius = (Temperatura - 32) * 5/9
    print(celsius, "°C")
else:
    print("Escala incorrecta")
