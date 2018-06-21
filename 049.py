#TABUADA AAUTOMATIZADA
num = int(input('Qual tabuada você quer? '))
for c in range(0, 11):
    print('{} X {} = {}'.format(num, c, num*c))
print('FIM')