from random import choice
print('Sorteio de alunos')
a1 = input('Digite o nome do aluno 1:')
a2 = input('Digite o nome do aluno 2:')
a3 = input('Digite o nome do aluno 3:')
a4 = input('Digite o nome do aluno 4:')
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
