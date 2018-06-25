print('Leitor de preços e descontos')
prod = float(input('Digite o valor do produto atual:\nR$'))
print('O preço atual é R${:.2f}, com 5% de desconto fica R%{:.2f}.\nUma economia de R${:.2f}!'.format(prod, prod*0.95, prod-prod*0.95))