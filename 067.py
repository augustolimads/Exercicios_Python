while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab >= 0:
        print('-' * 30)
        for cont in range(1,11):
            print(f'{tab} X {cont} = {tab*cont}')
        print('-' * 30)
    else:
        print('Programa tabuada encerrado, volte sempre!')
        break
