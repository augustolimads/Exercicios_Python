num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = num + 10 * razao
for c in range(num, ultimo, razao):
    print(c)
