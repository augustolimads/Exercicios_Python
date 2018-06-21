resp = str('S')
cont = int(0)
soma = int(0)
maior = int(0)
menor = int(0)
while resp != 'N': #resposta diferente de não
    num = int(input('Digite um valor: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    while cont == 0:
        menor = num
        cont += 1
    resp = str(input('Quer continuar? ')).strip().upper()
    soma += num
media = float(soma / cont)
print('Media = {:.2f}'.format(media))
print('Maior = {}'.format(maior))
print('Menor = {}'.format(menor))
