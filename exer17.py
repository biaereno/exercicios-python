""" Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta 
a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
        Acrescente 10% de folga e sempre arredonde os valores para cima,
        isto é, considere latas cheias. """

from math import ceil, floor


metragem = float(input("Informe o tamanho, em m², da área a ser pintada: "))
qtde_tinta = metragem / 6

qtde_sit1 = ceil(qtde_tinta / 18)
valor_sit1 = qtde_sit1 * 80

qtde_sit2 = ceil(qtde_tinta / 3.6)
valor_sit2 = qtde_sit2 * 25

sobra = ceil(qtde_tinta % 18)

qtde_sit3_18 = floor(qtde_tinta / 18)
qtde_sit3_3 = ceil(sobra / 3.6)
valor_sit3 = (qtde_sit3_18 * 80) + (qtde_sit3_3 * 25)


print(f"A quantidade de tinta a ser utilizada é de {qtde_tinta} litros.\n"
    f"Com apenas latas de 18L, seria preciso {qtde_sit1} latas, totalizando R${valor_sit1:.2f}\n"
    f"Com apenas galões de 3,6L, seria preciso {qtde_sit2} galões, totalizando R${valor_sit2:.2f}")

if sobra == 0:
    print(f"O ideal para o menor preço seria comprar {qtde_sit3_18} latas de 18L, num valor de R${valor_sit3:.2f}")
else: 
    print(f"O ideal para o menor preço seria comprar {qtde_sit3_18} latas de 18L e"
        f" {qtde_sit3_3} galões de 3,6L, totalizando R${valor_sit3:.2f}")