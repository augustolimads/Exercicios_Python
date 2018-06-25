sexo = str(input('Digite o seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Digite novamente...')
    sexo = str(input('Digite o seu sexo[M/F]: ')).strip().upper()[0]