print('Descobrindo se tem Silva no nome')
nome = str(input('Digite o nome de uma pessoa:')).strip()
nome2 = nome.lower()+' '
print('{} tem Silva no nome? {}'.format(nome, 'silva' in nome2.split()))
