print('Aumento de salário')
sal = float(input('Digite o valor do salário: R$'))
if sal > 1250.00:
    sal = sal*1.10
else:
    sal = sal*1.15
print('O salário agora será de R${}.'.format(sal))