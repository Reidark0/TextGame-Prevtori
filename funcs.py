import random
import time
from mob import Mobs, Arma, Armadura, Boss
from configs import monstros_easy, monstros_medium, monstros_hard, armas, armaduras, caminhos, mortes_jogador


def morte():
    time.sleep(1)
    tipos_morte_player = ['O cara foi solado q nem clickou kkkkkk',
                          'Foi de base, F no chat',
                          'Infelizmente não tankou e foi de berço...',
                          'Capotou o corsa...',
                          'Você foi escalado pro Vasco...',
                          'Você foi de Jackson five...',
                          'Infelizmente você não tankou a cirurgia e foi de base as 19:35',
                          'Você deu o peido mestre...']
    print(tipos_morte_player[random.randint(0, 7)])
    time.sleep(2)
    print('Você morreu!')
    exit()


def morte_especial():
    print('Previtori não ta pra brincadeira... ele está atento aos seu movimentos e \n'
          'quando você se da conta ele já ' + mortes_jogador[random.randint(0, 5)])
    print(morte())


def alea5():
    num_a = random.randint(0, 5)
    return num_a


def luta(minion, arma, armadura):
    hit_fraco = [
        'peteleco',
        'tapinha',
        'beijo de esquimó',
        'aperto de mão',
        'carrinho sem intenção',
        'vácuo no wpp'
    ]
    hit_medio = [
        'cheiro no cangote',
        'murro na boca',
        'carrinho na maldade',
        'trava no zap',
        'chute no ovo esquerdo',
        'tapa a lá Will Smith'
    ]
    hit_forte = [
        'Uma chave de piroca',
        'Uma voadora nos peito',
        'Uma sequencia 1,2, cruzado',
        'Uma mordida no ovo',
        'Um murro no cu',
        'Um beijão de cinema daqueles....'

    ]
    azul = '\033[34m'
    vermelho = '\033[31m'
    miss = '\033[37m'
    fim = '\033[m'
    monstro_vida = minion.vida
    dano = minion.dano
    monstro_raca = minion.raca
    player_vida = armadura.vida + 5
    print(f'Seu oponente é um {monstro_raca} Louco pra meter a mão na tua cara!\n'
          f'Ele possui {monstro_vida} de vida e {dano} de ataque!')
    time.sleep(1.5)
    print(f'Seu equipamento é:\nArma: \033[30;43m{arma.nome}\033[m com dano de {arma.dano}\n'
          f'Armadura: \033[30;43m{armadura.nome}\033[m com vida de {armadura.vida}, sua vida total é: {player_vida}')
    time.sleep(1.5)
    while player_vida > 0 and monstro_vida > 0:
        atk = input("Qual ataque você quer usar?\n"
                    "1 - fraco = 90%\n"
                    "2 - médio = 70%\n"
                    "3 - forte = 50%\n"
                    "4 - Defender-se\n")
        hit_monstro = random.randint(0, 1000)
        if atk == "1":
            print(f'Você tentou dar um {hit_fraco[alea5()]}...')
            time.sleep(1.5)
            hit = random.randint(0, 1000)
            if hit >= 900:
                monstro_vida -= 1 * arma.dano * 2
                print(f"\033[100;91mFoi efetivo pra caralho!!\033[m {1 * arma.dano * 2} de dano! "
                      f"Ele não esperava nunca isso")
                time.sleep(2)
            elif hit >= 100:
                monstro_vida -= 1 * arma.dano
                print(f"{azul}Você causou {1 * arma.dano} de dano!!{fim}")
                time.sleep(1)
            else:
                print(f'{miss}Você errou!!{fim}')
        if atk == "2":
            print(f'Você tentou dar um {hit_medio[alea5()]}...')
            time.sleep(1.5)
            hit = random.randint(0, 1000)
            if hit >= 900:
                monstro_vida -= 2 * arma.dano * 2
                print(f"\033[100;91mAcabou o brinquedo pow\033[m da não... deu {2 * arma.dano * 2} de dano "
                      f"nesse viado... F")
                time.sleep(2)
            elif hit >= 300:
                monstro_vida -= 2 * arma.dano
                print(f"{azul}Você causou {2 * arma.dano} de dano!!{fim}")
                time.sleep(1)
            else:
                print(f'{miss}Você errou!!{fim}')
        if atk == "3":
            print(f'Você tentou dar um {hit_forte[alea5()]}...')
            time.sleep(1.5)
            hit = random.randint(0, 1000)
            if hit >= 900:
                monstro_vida -= 3 * arma.dano * 2
                print(f"\033[40;31mEita porra... É valendo fazenda??\033[m \n"
                      f"Tu só meteu {3 * arma.dano * 2} de dano na bunda desse viado... precisava disso?")
                time.sleep(3)
            elif hit >= 500:
                monstro_vida -= 3 * arma.dano
                print(f"{azul}Você causou {3 * arma.dano} de dano!!{fim}")
                time.sleep(1)
            else:
                print(f'{miss}Você errou!!{fim}')
                time.sleep(1)
        if atk == "4":
            hit_monstro = 100
            print("Vôce se defendeu igual um covarde e fez o inimigo errar!")
        print(f'O {monstro_raca} avança...')
        time.sleep(1.5)
        if monstro_vida <= 0:
            print('E tropeça desfalecido...')
            time.sleep(2)
        elif hit_monstro >= 900:
            player_vida -= dano * 2
            print(f'\033[30;41mTá maluco!!!!\033[m {vermelho}o {monstro_raca} meteu um CRITÃO KKKKKK\n'
                  f'O Inimigo te jantou com {dano * 2} de dano!{fim}')
            time.sleep(2.5)
        elif hit_monstro >= 400:
            player_vida -= dano
            print(f'{vermelho}O Inimigo te causou {dano} de dano!{fim}')
            time.sleep(1.5)
        elif hit_monstro < 400:
            print(f'{miss}O Inimigo errou o ataque!{fim}')
            time.sleep(1.5)
        print(f'\033[92m--Sua vida restante é: {player_vida}\033[m\n'
              f'\033[91m--Vida restante do {monstro_raca} é: {monstro_vida}\033[m')
    if player_vida > 0:
        print(f"\033[30;102mVocê conseguiu!! solou o {monstro_raca}\033[m")
        return 1
    else:
        print("\033[30;41mVocê foi solado e o resto é história\033[m")
        return 2


def luta_femi(minion, arma, armadura):
    hit_fraco = [
        'peteleco',
        'tapinha',
        'beijo de esquimó',
        'aperto de mão',
        'carrinho sem intenção',
        'vácuo no wpp'
    ]
    hit_medio = [
        'cheiro no cangote',
        'murro na boca',
        'carrinho na maldade',
        'trava no zap',
        'chute no ovo esquerdo',
        'tapa a lá Will Smith'
    ]
    hit_forte = [
        'Uma chave de piroca',
        'Uma voadora nos peito',
        'Uma sequencia 1,2, cruzado',
        'Uma mordida no ovo',
        'Um murro no cu',
        'Um beijão de cinema daqueles....'

    ]
    azul = '\033[34m'
    vermelho = '\033[31m'
    miss = '\033[37m'
    fim = '\033[m'
    monstro_vida = minion.vida
    dano = minion.dano
    monstro_raca = minion.raca
    player_vida = armadura.vida + 5
    print(f'Seu oponente é uma {monstro_raca} louca pra meter a mão na tua cara!\n'
          f'Ela possui {monstro_vida} de vida e {dano} de ataque!')
    time.sleep(1.5)
    print(f'Seu equipamento é:\nArma: \033[30;43m{arma.nome}\033[m com dano de {arma.dano}\n'
          f'Armadura: \033[30;43m{armadura.nome}\033[m com vida de {armadura.vida}, sua vida total é: {player_vida}')
    time.sleep(1.5)
    while player_vida > 0 and monstro_vida > 0:
        atk = input("Qual ataque você quer usar?\n"
                    "1 - fraco = 90%\n"
                    "2 - médio = 70%\n"
                    "3 - forte = 50%\n"
                    "4 - Defender-se\n")
        hit_monstro = random.randint(0, 1000)
        if atk == "1":
            print(f'Você tentou dar um {hit_fraco[alea5()]}...')
            time.sleep(1.5)
            hit = random.randint(0, 1000)
            if hit >= 900:
                monstro_vida -= 1 * arma.dano * 2
                print(f"\033[100;91mFoi efetivo pra caralho!!\033[m {1 * arma.dano * 2} de dano! "
                      f"Ele não esperava nunca isso")
                time.sleep(2)
            elif hit >= 100:
                monstro_vida -= 1 * arma.dano
                print(f"{azul}Você causou {1 * arma.dano} de dano!!{fim}")
                time.sleep(1)
            else:
                print(f'{miss}Você errou!!{fim}')
        if atk == "2":
            print(f'Você tentou dar um {hit_medio[alea5()]}...')
            time.sleep(1.5)
            hit = random.randint(0, 1000)
            if hit >= 900:
                monstro_vida -= 2 * arma.dano * 2
                print(f"\033[100;91mAcabou o brinquedo pow\033[m da não... deu {2 * arma.dano * 2} de dano "
                      f"nesse viado... F")
                time.sleep(2)
            elif hit >= 300:
                monstro_vida -= 2 * arma.dano
                print(f"{azul}Você causou {2 * arma.dano} de dano!!{fim}")
                time.sleep(1)
            else:
                print(f'{miss}Você errou!!{fim}')
        if atk == "3":
            print(f'Você tentou dar um {hit_forte[alea5()]}...')
            time.sleep(1.5)
            hit = random.randint(0, 1000)
            if hit >= 900:
                monstro_vida -= 3 * arma.dano * 2
                print(f"\033[40;31mEita porra... É valendo fazenda??\033[m \n"
                      f"Tu só meteu {3 * arma.dano * 2} de dano na bunda desse viado... precisava disso?")
                time.sleep(3)
            elif hit >= 500:
                monstro_vida -= 3 * arma.dano
                print(f"{azul}Você causou {3 * arma.dano} de dano!!{fim}")
                time.sleep(1)
            else:
                print(f'{miss}Você errou!!{fim}')
                time.sleep(1)
        if atk == "4":
            hit_monstro = 100
            print(f"Vôce se defendeu igual um covarde e fez a {monstro_raca} errar!")
        print(f'O {monstro_raca} avança...')
        time.sleep(1.5)
        if monstro_vida <= 0:
            print('E tropeça desfalecida...')
            time.sleep(2)
        elif hit_monstro >= 900:
            player_vida -= dano * 2
            print(f'\033[30;41mTá maluco!!!!\033[m {vermelho}A {monstro_raca} meteu um CRITÃO KKKKKK\n'
                  f'A {monstro_raca} te jantou com {dano * 2} de dano!{fim}')
            time.sleep(2.5)
        elif hit_monstro >= 400:
            player_vida -= dano
            print(f'{vermelho}A {monstro_raca} te causou {dano} de dano!{fim}')
            time.sleep(1.5)
        elif hit_monstro < 400:
            print(f'{miss}A {monstro_raca} errou o ataque!{fim}')
            time.sleep(1.5)
        print(f'\033[93m--Sua vida restante é: {player_vida}\033[m\n'
              f'\033[91m--Vida restante da {monstro_raca} é: {monstro_vida}\033[m')
        time.sleep(2)
    if player_vida > 0:
        print(f"\033[30;102mVocê conseguiu!! solou a {monstro_raca}\033[m")
        time.sleep(2)
        return 1
    else:
        print("\033[30;41mVocê foi solado e o resto é história\033[m")
        time.sleep(2)
        return 2


def minijogo_1():
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)
    n5 = random.randint(0, 9)
    resposta = [n1, n2, n3, n4, n5]
    acertou = False
    while acertou is False:
        c1, c2, c3, c4, c5 = input('5 numeros de 0 a 9 separados por um espaço!\n').split()
        c1, c2, c3, c4, c5 = int(c1), int(c2), int(c3), int(c4), int(c5)
        chute_jogo = [c1, c2, c3, c4, c5]
        resposta_final = ''
        a = 0
        for chutes in chute_jogo:
            if chutes == resposta[a]:
                resposta_final = resposta_final + 'V '
                a += 1
            elif chutes != resposta[a]:
                resposta_final = resposta_final + 'x '
                a += 1
        print(resposta_final)
        if chute_jogo == resposta:
            print('Parabéns!!')
            acertou = True


def minijogo_2():
    numa = random.randint(1, 10)
    print('Você ta entrando em uma luta!!!'
          '\nVocê tem Três chances de acertar o número de 1 a 10!')
    min2 = False
    chutes = 0
    while min2 is False and chutes <= 2:
        print('Você tem ' + str(3 - chutes) + ' Chutes')
        chute_jogo2 = int(input('Fala um número de 1 a 10:\n'))
        if chute_jogo2 == numa:
            min2 = True
        elif chute_jogo2 > numa:
            print('Chute muito alto')
            chutes = chutes + 1
        elif chute_jogo2 < numa:
            print('Chute muito baixo')
            chutes = chutes + 1
    if chutes == 3:
        print('Você Perdeu!, o número era ' + str(numa))
        return 2
    else:
        print('Você ganhou!')
        return 1


def final_alt():
    new_nome1 = 'Pr' + nome[3:]
    new_nome2 = nome[:-3] + 'tori'
    nome_final = 'Prev' + nome[2:-3] + 'tori'
    print('Prevtori está morto...')
    time.sleep(2)
    print('Agora sem saber pra que direção seguir nem oque fazer você está perdido...')
    time.sleep(1.5)
    print('Você vaga revira a cabana a procura de alguma pista ou algo útil')
    time.sleep(1.5)
    andadas = 0
    esquerda = 0
    while andadas <= 10 and esquerda <= 3:
        print('***Aonde procurar?\n'
              '1- Esquerda\n'
              '2- Direita')
        procu = input('Digite 1 ou 2:\n ')
        andadas += 1
        if procu == '1':
            print('Não acho que vá ter nada pra esse lado...')
            esquerda += 1
        else:
            print('Creio que aquele velho não tem nada por aqui,')
            esquerda -= 1
    if esquerda >= 1:
        print('Você encontra um velho caderno com algumas instruções meio apagadas,'
              ' mas é o suficiente pra você continuar a sua jornada!')
    else:
        print('O tempo passa e tudo oque você encotra é um grande estoque de comida que parece ilimitado\n'
              'Você vê o tempo passar e suas mãos se enrugarem...\n'
              'a unica coisa que te chama atenção é o barulho do vento nessa cabana...')
        time.sleep(1.5)
        print('parece até um nome.... Prevtori.... e isso lá é um nome? e por falar nisso qual era o meu?')
        time.sleep(1.5)
        print('Você pensa e pensa.... qual era mesmo? ' + new_nome1 + '?.. ou era ' + nome + '?... quem sabe '
              + new_nome2 + '....')
        time.sleep(1.5)
        print('Quase certeza que era ' + nome_final + '... \nNão... na verdade acho que era só Prevtori mesmo...')
        time.sleep(1.5)
        print('Após oque parecem decadas você vê um jovem correndo em sua direção e você berra: \n'
              '-Você ai!\n-Onde você pensa que vai? essa é a minha cabana!')
        exit()
