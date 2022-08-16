"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário 
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento 
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

peso_peixe = float(input("Insira o peso de peixes: "))
excesso = float
multa = float

if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa = excesso * 4
    print(f"O peso total foi de {peso_peixe:.2f} kg e excedeu em {excesso:.2f} kg. " 
    f"O valor da multa será de R${multa:.2f}.")
else:
    print(f"O peso total foi de {peso_peixe:.2f} kg, e não infringiu o regulamento.")