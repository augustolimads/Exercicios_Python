print('Média do aluno')
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
print(media)
if media >= 7.0:
    print('APROVADO')
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO')
elif media < 5.0:
    print('REPROVADO')