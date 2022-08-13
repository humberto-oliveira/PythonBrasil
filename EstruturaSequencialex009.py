# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fah = float(input('Informa a temperatura em Fahrenheit: '))
cel = 5 * ((fah-32) / 9)
print('Como a temperatura em fahrenheit é de {}, em celsius ela será de {:.2f}'.format(fah, cel))
