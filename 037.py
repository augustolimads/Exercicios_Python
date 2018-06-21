#INICIO DO PROGRAMA
num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases de conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
esc = int(input('>'))
if esc == 1:
    print('{} convertido para binário = {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('{} convertido para octal = {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('{} convertido para hexadecimal = {}'.format(num, hex(num)[2:]))
else:
    print('Inválido')
