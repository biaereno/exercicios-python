""" As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe 
o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento."""

salario = float(input("Informe o seu salário: "))
aumento = float
novo_salario = float

if salario <= 280.00:
    aumento = salario * 0.2
    novo_salario = aumento + salario
    

    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print(f"Percentual de aumento: 20%")
    print(f"Valor do aumento: {aumento:.2f}")
    print(f"Novo salário após aumento: R$ {novo_salario:.2f}")

elif salario > 280.00 and salario <= 700.00:
    aumento = salario * 0.15
    novo_salario = aumento + salario
   

    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print(f"Percentual de aumento: 15%")
    print(f"Valor do aumento: {aumento:.2f}")
    print(f"Novo salário após aumento: R$ {novo_salario:.2f}")

elif salario > 700.00 and salario <= 1500.00:
    aumento = salario * 0.1
    novo_salario = aumento + salario

    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print(f"Percentual de aumento: 10%")
    print(f"Valor do aumento: {aumento:.2f}")
    print(f"Novo salário após aumento: R$ {novo_salario:.2f}")

else:
    aumento = salario * 0.05
    novo_salario = aumento + salario

    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print(f"Percentual de aumento: 5%")
    print(f"Valor do aumento: {aumento:.2f}")
    print(f"Novo salário após aumento: R$ {novo_salario:.2f}")