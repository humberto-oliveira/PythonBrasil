# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input('Digite o valor do lado do quadrado: '))
area = lado * lado
dobro = area * 2
print('Como o lado possui {}, sua área tem {} e o dobro dela é {}'.format(lado, area, dobro))

