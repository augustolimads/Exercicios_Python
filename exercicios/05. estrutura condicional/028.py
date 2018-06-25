from random import randint
print('JOGUINHO DE ADIVINHAÇÃO')
num = randint(0, 5)
test = int(input('Escolha um número entre 0 e 5: '))
if test==num:
    print('{}. Isso mesmo, você adivinhou!!! :0 '.format(num))
else:
    print('Tente outra vez...')
