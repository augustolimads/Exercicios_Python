from random import randint
sidade = int(0)   # a soma da idade do grupo
vidade = int(0) # idade do mais velho
snovinhas = int(0)  #quantidade de menores de 20 no grupo
sexo = ['m', 'f']
# ENTRADA DE DADOS
for c in range(0,4):
    print('=~'*20)
    nome = str(input('Nome {}: '.format(c)))
    idade = randint(14, 35)
    print('Sua idade: {} anos'.format(idade))
    r = randint(0, 1)
    sexo1 = sexo[r]
    print('sexo [M/F]: {}'.format(sexo1))
    print('=~'*20)
    sidade += idade
    if idade > vidade:
        vidade = idade
        velho = nome
    if sexo1 == 'f':
        if idade < 20:
            snovinhas += 1
# RESULTADO
media = float(sidade/4)
print('A média da idade do grupo é {}'.format(media))
print('O nome do homem mais velho é {}, com {} anos.'
      .format(velho, vidade))
print('A quantidade de mulheres com menos de 20 anos é {}'
      .format(snovinhas))
