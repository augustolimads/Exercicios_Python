casas = int(10) #quantidade de repetições
prim = int(input('Digite o primeiro termo da PA: '))
prim1 = prim
raz = int(input('Digite a razão: '))
while casas > 0:
    print(prim)
    prim += raz
    casas -= 1
casas = int(10) #quantidade de repetições
mais = int(input('quantos termos a mais deseja visualizar? '))
casas += mais
while mais != 0:
    while casas > 0:
        print(prim1)
        prim1 += raz
        casas -= 1
    mais = int(input('quantos termos a mais deseja visualizar? '))
    casas += mais