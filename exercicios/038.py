#CORES
r = str('\33[31m')  #red
g = str('\33[32m')  #green
y = str('\33[33m')  #yellow
b = str('\33[34m')  #blue
m = str('\33[35m')  #magenta
c = str('\33[36m')  #cian
x = str('\33[m')    #fechamento
#INICIO DO PROGRAMA
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('{} é maior.'.format(n1))
elif n2 > n1:
    print('{} é maior.'.format(n2))
else:
    print('Não existe valor maior.')