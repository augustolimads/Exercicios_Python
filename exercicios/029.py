print('Velocimetro eletrônico')
vel = float(input('Velocidade do carro nesse trecho [km/h]: '))
if vel>80:
    print('MULTADO!')
    multa = float(7*(vel-80))
    print('Valor total da multa: R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')
