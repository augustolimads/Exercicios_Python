#CORES
r = str('\33[31m')  #red
g = str('\33[32m')  #green
y = str('\33[33m')  #yellow
b = str('\33[34m')  #blue
m = str('\33[35m')  #magenta
c = str('\33[36m')  #cian
x = str('\33[m')    #fechamento
#PROGRAMA
print('=~'*12)
print('Minha casa minha vida')
print('=~'*12)
casa = float(input('Qual o valor da casa que você pretende comprar? R$'))
sal = float(input('Qual é o seu salário? R$'))
anos = int(input('Pretende comprar em quantos anos? '))
prestações = anos * 12
parcela = casa/prestações
print('O valor total da casa é {}R${:.2f}{}, dividido em {}{}{} vezes de {}R${:.2f}{}.'
      .format(g, casa, x, c, prestações, x, g, parcela, x))
if parcela >= sal*0.7:
    print('Empréstimo {}não liberado{}.'.format(r,x))
else:
    print('Parabéns, empréstimo {}liberado{}!'.format(b,x))
