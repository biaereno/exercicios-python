"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))
num3 = float(input("Insira o 3º número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número é {num1}")
elif num3 > num2:
    print(f"O maior número é {num3}")
else:
    print(f"O maior número é {num2}")

if num1 < num2 and num1 < num3:
    print(f"O menor número é {num1}")
elif num3 < num2:
    print(f"O menor número é {num3}")
else:
    print(f"O menor número é {num2}")
