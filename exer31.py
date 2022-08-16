"""Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""

numero_dia = int(input("Insira o número corresponte ao dia da semana (1 - Domingo, 2 - Segunda, ...): "))

if numero_dia == 1:
    print("O dia da semana é Domingo")
elif numero_dia == 2:
    print("O dia da semana é Segunda")
elif numero_dia == 3:
    print("O dia da semana é Terça")
elif numero_dia == 4:
    print("O dia da semana é Quarta")
elif numero_dia == 5:
    print("O dia da semana é Quinta")
elif numero_dia == 6:
    print("O dia da semana é Sexta")
elif numero_dia == 7:
    print("O dia da semana é Sábado")
else:
    print("Valor inválido")