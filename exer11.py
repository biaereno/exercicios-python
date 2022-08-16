""""" Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. """""

num1 = int(input("Informe o primeiro número (inteiro): "))
num2 = int(input("Informe o segundo número (inteiro): "))
num3 = float(input("Informe o terceiro número (real): "))
conta1 = (num1 * 2) * (num2 / 2)
conta2 = (num1 * 3) + num3
conta3 = num3 ** 3

print(f"A = {conta1}\nB = {conta2}\nC = {conta3}")