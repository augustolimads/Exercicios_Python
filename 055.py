from random import uniform
maior = float(0)
menor = float(999)
for c in range(0, 5):
    peso = uniform(33.0, 100.0)
    print('peso {} = {:.2f}Kg'.format(c, peso))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O mais pesado foi {:.1f}Kg'.format(maior))
print('O mais leve foi {:.1f}Kg'.format(menor))