# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Informe a temperatura em graus celsius: "))
fahrenheit = ((celsius * 9) / 5) + 32
print(f"{celsius:.2f} graus celsius equivalem a {fahrenheit:.2f} graus fahrenheit")