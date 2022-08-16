"""Faça um Programa que leia três números e mostre o maior deles."""

num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))
num3 = float(input("Insira o 3º número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número é {num1}")
elif num2 > num3:
    print(f"O maior número é {num2}")
else:
    print(f"O maior número é {num3}")