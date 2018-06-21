cinquenta = int(0)
vinte = int(0)
dez = int(0)
um = int(0)
print('='*25)
print('{:^25}'.format('BANCO CEV'))
print('='*25)
saque = float(input('Que valor deseja sacar? R$'))
#CALCULO
if saque >= 50:
    cinquenta = int(saque // 50)
    saque = saque - (50*cinquenta)
if saque >= 20:
    vinte = int(saque // 20)
    saque = saque - (20*vinte)
if saque >= 10:
    dez = int(saque // 10)
    saque = saque - (10*dez)
if saque >= 1:
    um = int(saque // 1)
    saque = saque - (1*um)
#RESULTADO
print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} moedas de R$1')
print('='*25)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
