# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

alt = (float(input('Digite a sua altura: ')))
pesh = (72.7 * alt) - 58
pesm = (62.1 * alt) - 44.7
print('Como a sua altura é de {}, se você for um homem, seu peso ideal será de {}! Caso seja uma mulher, o seu peso ideal será de {}!'.format(alt, pesh, pesm))

