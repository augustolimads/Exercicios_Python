num = int(input('Digite o valor: '))
num2 = num
fat = int(1)
while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat = fat * num
    num -= 1
print('O fatorial de {}! é {}'.format(num2, fat))