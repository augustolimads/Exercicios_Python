from random import randint
menor = int(0)
maior = int(0)
for c in range(0,7):
    ano = randint(1990, 2013)
    idade = int(2018-ano)
    print('fulano {} nasceu em {}, e tem {} anos.'.format(c, ano, idade))
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} são maiores de idade.'.format(maior))
print('{} são menores de idade.'.format(menor))