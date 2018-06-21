#também não soube fazer 100%
print('Analisador de frase:')
frase = str(input('Digite uma frase qualquer:')).strip()
frase = frase.lower()
print('Quantas vezes aparece a letra A? {}'.format(frase.count('a')))
print('Em que posição ela aparece a 1º vez? {}'.format(frase.find('a')+1))
print('Em que posição ela aparece na última vez? {}'.format(frase.rfind('a')+1))
