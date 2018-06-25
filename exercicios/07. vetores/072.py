#consegui incompleto
contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

cont = int(input('Digite um número entre 0 e 20:'))

if cont < 0 or cont > 20:
    cont = int(input('Tente novamente. Digite um número entre 0 e 20:'))
else:
    print(f'Você digitou o número {contagem[cont]}.')