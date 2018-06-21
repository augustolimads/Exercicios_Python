print('Aluguel de carros')
dias = int(input('Digite a quantidade de dias que você passou com o carro:'))
km = int(input('Quantos quilômetros foram percorridos? Km'))
tot = float(dias*60)+(0.15*km)
print('O valor total do seu aluguel foi: R${:.2f}'.format(tot))

