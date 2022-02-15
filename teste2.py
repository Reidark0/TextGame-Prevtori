import random
from mob import arma

armas = [
    arma('Mão', 0),
    arma('Queijo', 1),
    arma('Espada', 2),
    arma('Machado', 3),
    arma('Revolver', 4),
]

def luta():
    maxi = 10 - drop.dano
    numa = random.randint(1, maxi)
    print('Você ta entrando em uma luta!!!\n'
          'Você está lutando com ' + drop.nome + ' que reduz o numero máximo em: ' + str(drop.dano) + '\n'
          'Você tem duas chances de acertar o número de 1 a '+ str(maxi) + '!')
    acerto = False
    chutes = 0
    while acerto == False and chutes <= 2:
        print('Você tem ' + str(3 - chutes) + ' Chutes')
        chute = int(input('Fala um número de 1 a ' + str(maxi) + ':\n'))
        if chute == numa:
            acerto = True
        elif chute > numa:
            print('Chute muito alto')
            chutes = chutes + 1
        elif chute < numa:
            print('Chute muito baixo')
            chutes = chutes + 1
    if chutes == 3:
        print('Você Perdeu!, o número era ' + str(numa))
        return 2
    else:
        print('Você ganhou!')
        return 1


qual = 5
while qual <=4:
    drop = armas[qual]
    luta()
    qual += 1
    print(qual)

print('Você vê 12 caixas, em qual delas você quer olhar?')
chute = 15
demora = 0
while chute != 0 and demora <=9:
    giro = random.randint(1, 12)
    chute = int(input('Em qual caixa vc quer procurar de 1 a 12? \n (0 para sair da casa)\n '))
    if chute == 0:
        break
    elif chute == giro:
        print('Você encontrou o diário daquele velho broxa!!!\n'
              'Você volta para a rua com o objetivo da missão em mãos')
        break
    elif chute != giro:
        print('Você NÃO encontra nada e sem querer esbarra e embaralha as caixas novamente...\n'
              'Você não tem todo o tempo do mundo...')
        demora += 1
if demora >= 9:
    print('Morreu de demora!')
print('Você volta a Rua...')