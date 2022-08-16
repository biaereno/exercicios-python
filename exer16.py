""""Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

from math import ceil


tamanho = float(input("Informe qual a área a ser pintada, em m²: "))
qtde_tinta = tamanho / 3
latas_comprar = ceil(qtde_tinta / 18)
valor_total = latas_comprar * 80

print(f"Quantidade de latas de tinta a serem compradas: {latas_comprar}\n"
    f"Valor a ser pago: R${valor_total:.2f}")