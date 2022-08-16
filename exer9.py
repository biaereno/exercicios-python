#Faça um Programa que peça a temperatura em graus Fahrenheit,
#transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit-32) / 1.8

print(f"{fahrenheit:.2f} graus fahrenheit equivalem a {celsius:.2f} graus celsius")