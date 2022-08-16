# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

cel = float(input('Digite a temperatura em graus celsius: '))
fah = (cel * 1.8) + 32
print('Como a temperatura em celsius é de {:.2f}, em fahhnheit ela será de {:.2f}!'.format(cel, fah))

