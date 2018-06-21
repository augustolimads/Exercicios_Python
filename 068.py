from random import randint
parimpar = ['P', 'I']
parimpar2 = ['Par', 'Ímpar']
vitorias = int(0)
def resultado():
    print(f'Você jogou {jg} e o computador {pc}. A soma é {soma}, deu {result2}.')

print('=-'*40)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-'*40)
while True:
    pc = randint(0,10)
    jg = int(input('Digite um valor: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()
    print('-'*40)
    soma = int(pc + jg)
    if soma % 2 == 0:
        result = parimpar[0]
        result2 = parimpar2[0]
    else:
        result = parimpar[1]
        result2 = parimpar2[1]
    if escolha == result:
        resultado()
        print('Você venceu!')
        vitorias += 1
    else:
        resultado()
        print('Você perdeu!')
        break
print('=-'*40)
print(f'GAME OVER. Ganhou {vitorias} vezes consecutivas.')
