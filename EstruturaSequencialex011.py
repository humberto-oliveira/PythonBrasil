# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

ni1 = int(input('Digite o 1º número inteiro: '))
ni2 = int(input('Digite o 2º número inteiro: '))
nr = float(input('Digite um número real: '))
mult = (ni1 * 2) * (ni2 / 2)
soma = (ni1 * 3) + nr
cub = nr ** 3
print('O produto do dobro de {} com metade de {} é: {:.0f}'.format(ni1, ni2, mult))
print('A soma do triplo de {} com {} é: {:.1f} '.format(ni1, nr, soma))
print('{} elevado ao cubo é: {:.0f}'.format(nr, cub))
