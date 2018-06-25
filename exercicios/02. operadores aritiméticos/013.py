print('Aumento de salário')
nome = input('Digite o nome do funcionário:')
sal = float(input('Digite o valor atual do salário de {:.2f}:\nR$'.format(nome)))
print('Parabéns {}, você teve um aumento e seu salário agora é R${:.2f}'.format(nome, sal*1.15))