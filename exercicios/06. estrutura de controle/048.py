simpar = int(0)
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        simpar += c
print('Total de ímpares multiplos de 3: {}'.format(simpar))
