mais18 = int(0)
homens = int(0)
novinhas = int(0)
print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Qual é o sexo? [m,f]')).strip().lower()
    if idade >= 18:
        mais18 += 1
    if sexo == 'm':
        homens += 1
    if idade < 20 and sexo == 'f':
        novinhas += 1
    resp = str(input('Deseja continuar? [s/n]')).strip().lower()
    if resp == 'n':
        break
#RESULTADO
print(f'{mais18} pessoas com mais de 18 anos.')
print(f'{homens} homens cadastrados.')
print(f'{novinhas} mulheres com menos de 20 anos.')