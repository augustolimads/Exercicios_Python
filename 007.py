nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a 1º nota do aluno {}:'.format(nome)))
n2 = float(input('Digite a 2º nota do aluno {}:'.format(nome)))
media = (n1+n2)/2
print('A média do aluno {} foi {:.2f}'.format(nome, media))
