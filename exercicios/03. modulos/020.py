import random
print('Ordem de sorteio dos alunos')
a1 = input('Digite o nome do aluno 1:')
a2 = input('Digite o nome do aluno 2:')
a3 = input('Digite o nome do aluno 3:')
a4 = input('Digite o nome do aluno 4:')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem escolhida foi:')
print(lista)