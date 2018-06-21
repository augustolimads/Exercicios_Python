#CORES
r = str('\33[31m')  #red
g = str('\33[32m')  #green
y = str('\33[33m')  #yellow
b = str('\33[34m')  #blue
m = str('\33[35m')  #magenta
c = str('\33[36m')  #cian
x = str('\33[m')    #fechamento
#INICIO DO PROGRAMA
#JUROS E DESCONTO DE PRODUTO
prod = float(input('Digite o preço do produto: '))
d10 = prod*0.9
d5 = prod*0.95
j20 = prod*1.2

print('Qual a forma de pagamento? ')
print('{}1 - dinheiro{}'.format(c, x))
print('{}2 - cheque{}'.format(c, x))
print('{}3 - cartão{}'.format(c, x))
pag = int(input('>'))
if pag == 1 or pag == 2: #a vista dinheiro/cartao
    print('Ficará por: {}R${:.2f}{}'.format(g, d10, x))
elif pag == 3: #cartao
    print('Em quantas vezes?')
    print('{}1 - à vista{}'.format(c, x))
    print('{}2 - até 2x{}'.format(c, x))
    print('{}3 - até 6x{}'.format(c, x))
    vzs = int(input('>'))
    if vzs == 1:
        print('Ficará por: {}R${:.2f}{}'.format(g, d5, x))
    elif vzs == 2:
        print('2x de R${}'.format(prod/2))
        print('Ficará por: {}R${:.2f}{}'.format(g, prod, x))
    elif vzs == 3:
        print('6x de R${:.2f}'.format(prod/6))
        print('Ficará por: {}R${:.2f}{}'.format(g, j20, x))
    else:
        print('{}Escolha inválida{}'.format(r, x))
else:
    print('{}Escolha inválida.{}'.format(r, x))