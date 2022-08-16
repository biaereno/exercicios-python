"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))
num3 = float(input("Insira o 3º número: "))

if num1 > num2 and num1 > num3 and num2 > num3:
    print(f"{num1}, {num2}, {num3}")
elif num1 > num2 and num1 > num3 and num3 > num2:
    print(f"{num1}, {num3}, {num2}")
elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f"{num2}, {num1}, {num3}")
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f"{num2}, {num3}, {num1}")
elif num3 > num1 and num3 > num2 and num1 > num2:
    print(f"{num3}, {num1}, {num2}")
else:
    print(f"{num3}, {num2}, {num1}")