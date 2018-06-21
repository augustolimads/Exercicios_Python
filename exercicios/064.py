num = int(0)
cont = int(0)
soma = int(0)
while num != 999:
    num = int(input('Digite um valor [até 999]: '))
    if num != 999:
        cont += 1
        soma += num
print('A quantidade contagens foi: {}'.format(cont))
print('A soma de todos os termos foi: {}'.format(soma))
