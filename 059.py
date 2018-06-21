a = int(input('Digite o valor do primeiro número: '))
b = int(input('Digite o valor do segundo número: '))
escolha = int(0)
maior = int(0)
while escolha != 5: #laço geral quando ele acabar encerra o programa
    print('''O que deseja fazer? 
    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    escolha = int(input('>'))
    if escolha == 1:
        print('{} + {} = {}'.format(a, b, a+b))
    if escolha == 2:
        print('{} x {} = {}'.format(a, b, a*b))
    if escolha == 3:
        if a > b:
            print('O maior número é {}'.format(a))
        else:
            print('O maior número é {}'.format(b))
    if escolha == 4:
        a = int(input('Digite o valor do primeiro número: '))
        b = int(input('Digite o valor do segundo número: '))