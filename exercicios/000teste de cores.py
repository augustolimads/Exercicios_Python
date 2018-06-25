#CORES
r = str('\33[31m')  #red
g = str('\33[32m')  #green
y = str('\33[33m')  #yellow
b = str('\33[34m')  #blue
m = str('\33[35m')  #magenta
c = str('\33[36m')  #cian
x = str('\33[m')    #fechamento

#EXIBIÇÃO CORES
print('^-'*5)
print(f'{r}vermelho{x}')
print(f'{g}verde{x}')
print(f'{y}amarelo{x}')
print(f'{b}azul{x}')
print(f'{m}magenta{x}')
print(f'{c}cian{x}')
print(f'^-'*5)
#INICIO DO PROGRAMA
nome = str(input('Digite seu nome: '))
print('Olá {}{}{}, é um prazer te conhecer!'.format(m, nome, x))
grana = float(20.0)
print('Você possui no seu bolso: {}R${}{}, {}ECONOMIZE{}'.format(g, grana, x, r, x,))
