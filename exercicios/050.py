from random import randint
s = int(0)
for c in range(0,6):
    num = randint(0,9)
    print('{} --> {}'.format(c, num))
    if num % 2 == 0:
        s += num
print('Soma = {}'.format(s))
