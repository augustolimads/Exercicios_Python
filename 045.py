from random import randint
from time import sleep
#PROGRAMA
print('Jokenpo')
#Vou pegar os itens do pedra,papel tesoura e cada um representa 0,1,2 respectivamente;
#quando eu printo itens[jg ou pc] to dizendo que vai ler determinado item com indice tal;
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)

print('''jogador, escolha:
0 - pedra
1 - papel
2 - tesoura''')
jg = int(input('>'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('~^'*15)
print('O jogador escolheu {}!'.format(itens[jg]))
print('O computador escolheu {}!'.format(itens[pc]))
print('~^'*15)

#COMBATE
if jg == 0 and pc == 0 or jg == 1 and pc == 1 or jg == 2 and pc == 2:
    print('EMPATE!')
elif jg == 0 and pc == 2 or jg == 1 and pc == 0 or jg == 2 and pc == 1:
    print('JOGADOR VENCEU!!!')
elif pc == 0 and jg == 2 or pc == 1 and jg == 0 or pc == 2 and jg == 1:
    print('COMPUTADOR VENCEU!!!')
else:
    print('Comando inválido')
