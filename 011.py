print('Quantidade de tinta necessária para pintar uma parede.')
a = float(input('Qual a altura da parede?'))
l = float(input('Qual a largura da parede?'))
area = a*l
tin = float(area/2)
print('É necessário {:.4f}L de tinta para preencher {:.4f}m² de parede.'.format(tin, area))
