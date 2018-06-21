print('Qual é o maior e qual é o menor?')
a = int(input('valor 1:'))
b = int(input('valor 2:'))
c = int(input('valor 3:'))
#TESTANDO O MAIOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#MENOR
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O número maior foi: {}'.format(maior))
print('O número menor foi: {}'.format(menor))
