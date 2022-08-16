""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido. """

valor_hora = float(input("Informe seu valor hora: "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas por mês: "))
salario_bruto = valor_hora * horas_trabalhadas
ir = (11 / 100) * salario_bruto
inss = (8 / 100) * salario_bruto
sindicado = (5 / 100) * salario_bruto
salario_liquido = salario_bruto - ir - inss- sindicado

print(f"+ Salário Bruto: R${salario_bruto:.2f}\n"
    f"- IR (11%): R${ir:.2f}\n"
    f"- INSS (8%): R${inss:.2f}\n"
    f"- Sindicato (5%): R${sindicado:.2f}\n"
    f"= Salário Liquido: R${salario_liquido:.2f}\n" )
