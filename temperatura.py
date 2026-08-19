#Solicita una temperatura en grados Celsius y calcula Fahrenheit mediante F = (C * 9 / 5) + 32.

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("La temperatura en Fahrenheit es: ", fahrenheit, "°F")