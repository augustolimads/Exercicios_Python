from datetime import date
#INICIO DO PROGRAMA
nasc = int(input('Ano de nascimento:'))
ano = date.today().year
idade = ano-nasc
militar = int(18)
if idade < militar:
    print('Ainda vai se alistar. Faltam {} anos.'.format(militar-idade))
elif idade == militar:
    print('{}Hora de se alistar!{}'.format(r, x))
elif idade > militar:
    print('Já passou do tempo de se alistar. Fazem {} anos.'.format(idade-militar))
