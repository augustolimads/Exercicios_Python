print('Um programa que analisa um número')
#UTILIZANDO STRING
#num = str(input('Digite um número de 1 até 9999:')).strip()
#print('Unidade:{}'.format(num[3]))
#print('Dezena:{}'.format(num[2]))
#print('Centena:{}'.format(num[1]))
#print('Milhar:{}'.format(num[0]))

#UTILIZANDO INTEGER
num2 = int(input('Digite um número de 1 até 9999:'))
u = num2 // 1 % 10
d = num2 // 10 % 10
c = num2 // 100 % 10
m = num2 // 1000 % 10
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
