num = int(input('Digite um número: '))
sprimo = int(0)
for c in range(1, num+1):
    if num % c == 0:
        sprimo += 1
if sprimo == 2:
    print('{} é primo'.format(num))
else:
    print('{} não é primo'.format(num))
