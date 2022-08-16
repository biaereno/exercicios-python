"""Faça um programa que pergunte o preço de três produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

produto1 = float(input("Informe o valor do 1º produto: "))
produto2 = float(input("Informe o valor do 2º produto: "))
produto3 = float(input("Informe o valor do 3º produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"O valor do produto mais barato é de {produto1:.2f} reais")
elif produto2 < produto3:
    print(f"O valor do produto mais barato é de {produto2:.2f} reais")
else:
    print(f"O valor do produto mais barato é de {produto3:.2f} reais")