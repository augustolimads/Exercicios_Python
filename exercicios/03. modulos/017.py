import math
print('Hipotenusa')
c1 = float(input('Digite o valor do cateto adjacente:'))
c2 = float(input('Digite o valor do cateto oposto:'))
print('O comprimento da hipotenusa é: {:.4f}'.format(math.hypot(c1,c2)))