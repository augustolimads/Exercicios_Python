total = float(0)
cont = int(0)
c = int(0) #só para contagem inicial
barato = total
produto = str('')
while True:
    c += 1
    nome = str(input('Digite o nome do produto: '))
    preco = float(input(f'O preço do {nome}: R$'))
    if c == 1:
        barato = preco
        produto = nome
    total += preco
    if preco >= 1000:
        cont += 1
    if preco < barato:
        barato = preco
        produto = nome
    resp = str(input('Pretende continuar? [s/n]: ')).strip().lower()
    if resp == 'n':
        break

#RESULTADO
print(f'Total gasto na compra: R${total}.')
print(f'{cont} produtos custam mais de R$1000.0')
print(f'{produto} é o nome do produto mais barato, custando R${barato}.')