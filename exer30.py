""" Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de
Renda, que depende do salário bruto (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
 os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00 """

valor_hora = float(input("Informe o valor da sua hora de trabalho: "))
qtde_horas_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))
salario_bruto = valor_hora * qtde_horas_mes
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11

if salario_bruto <= 900.00:
    imposto_renda = 0
    descontos = imposto_renda + inss
    salario_liquido = salario_bruto - descontos

    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
    print(f"INSS: R$: {inss:.2f}")
    print(f"FGTS: R$ {fgts:.2f}")
    print(f"Total de descontos: R$ {descontos:.2f}")
    print(f"Salário Liquido: R${salario_liquido:.2f}")

elif salario_bruto <= 1500.00:
    imposto_renda = salario_bruto * 0.05
    descontos = imposto_renda + inss
    salario_liquido = salario_bruto - descontos

    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
    print(f"INSS: R$: {inss:.2f}")
    print(f"FGTS: R$ {fgts:.2f}")
    print(f"Total de descontos: R$ {descontos:.2f}")
    print(f"Salário Liquido: R${salario_liquido:.2f}")

elif salario_bruto <= 2500.00:
    imposto_renda = salario_bruto * 0.1
    descontos = imposto_renda + inss
    salario_liquido = salario_bruto - descontos

    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
    print(f"INSS: R$: {inss:.2f}")
    print(f"FGTS: R$ {fgts:.2f}")
    print(f"Total de descontos: R$ {descontos:.2f}")
    print(f"Salário Liquido: R${salario_liquido:.2f}")

else:
    imposto_renda = salario_bruto * 0.2
    descontos = imposto_renda + inss
    salario_liquido = salario_bruto - descontos

    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
    print(f"INSS: R$: {inss:.2f}")
    print(f"FGTS: R$ {fgts:.2f}")
    print(f"Total de descontos: R$ {descontos:.2f}")
    print(f"Salário Liquido: R${salario_liquido:.2f}")