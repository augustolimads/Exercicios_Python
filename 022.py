print('Analisador de nome')
nome = str(input('Digite seu nome:')).strip() #Esse strip tira os espaços da esquerda e direita
print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' '))) #aqui ta cortando da contagem os espaços
pnome = (nome.split()) #aqui fatiei o nome completo
print('Seu primeiro nome tem {} letras.'.format(len(pnome[0]))) #aqui contei o primeiro nome
