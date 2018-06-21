print('Programa de viagens')
dist = float(input('Digite a distância para o local destino:'))
if dist <= 200:
    passagem = dist*0.5
else:
    passagem = dist*0.45
print('O valor total da passagem será: R${:.2f}'.format(passagem))
