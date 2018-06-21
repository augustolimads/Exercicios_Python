#Dificuldades também
nome = str(input('Digite o nome completo:')).strip()
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print(len(nome))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
