from random import randint
print('Joguinho de adivinhação melhorado')
num = randint(0, 10)
test = int(-1)
tentativas = int(0)
while test != num:
    test = int(input('Escolha um número entre 0 e 10: '))
    tentativas += 1
    if test == num:
        print('{}. Isso mesmo, você adivinhou!!!'.format(num))
    elif test > num:
        print('Menos... Tente outra vez...')
    elif test < num:
        print('Mais... Tente outra vez...')
print('Em {} tentativas.'.format(tentativas))