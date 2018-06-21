print('Analisando triângulo')
a = float(input('Digite o lado A: '))
b = float(input('Digite o lado B: '))
c = float(input('Digite o lado C: '))
#Testando se pode ser triângulo
tri = bool((a < b+c) and (b < a+c) and (c < a+b))
if tri:
    print('É um triângulo')
    # Testando o tipo de triângulo
    if a == b == c:
        tipo = 'Equilátero'
    elif a == b and a != c or b == c and b != a:
        tipo = 'Isósceles'
    elif a != b != c != a:
        tipo = 'Escaleno'
    print('E seu tipo é: {}'.format(tipo))
else:
    print('Não é um triângulo')
