#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Informe quanto você ganha por hora trabalhada: "))
horas_trabalhadas = int(input("Informe quantas horas você trabalha por mês: "))
salario_mes = horas_trabalhadas * valor_hora
print(f"Ganhando R${valor_hora:.2f} a hora, tendo trabalhado {horas_trabalhadas} horas no mês, "
    f"o seu salário do mês será de R${salario_mes:.2f}")