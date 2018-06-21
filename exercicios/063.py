a = int(0)
b = int(1)
termo = int(input('Digite o valor de termos para visualizar: '))
termo -= 2
print(a)
print(b)
while termo != 0:
    c = a + b
    a = b
    b = c
    print(c)
    termo -= 1

''' Minha filinha
a   b   c
0 + 1 = 1 X
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
'''