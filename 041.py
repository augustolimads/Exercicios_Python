from datetime import date
print('Confederação nacional de natação')
print('categoria de atletas:')
nasc = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano-nasc
print('Ano atual {}'.format(ano))
if idade <= 9:
    c = 'Mirim'
elif idade <= 14:
    c = 'Infantil'
elif idade <= 19:
    c = 'Junior'
elif idade <= 20:
    c = 'Sênior'
else:
    c = 'Master'
print('sua categoria será: {}'.format(c))