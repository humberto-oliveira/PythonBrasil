# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salhora = float(input('Quanto você ganha por hora ? '))
numhora = int(input('Quantas horas você trabalha no mês ? '))
totalsal = salhora * numhora
print('Como você ganha {:.2f} por hora e trabalha {} horas no mês, seu salário é de {:.2f}'.format(salhora, numhora, totalsal))
