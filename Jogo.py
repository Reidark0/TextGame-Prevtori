import random
import time
from mob import Mobs
from mob import Arma
from mob import Armadura
from mob import Boss
boss = Boss(Mobs('Podi', 3, 3), Mobs('Babu', 4, 4), Mobs('Lucca', 5, 5), Mobs('Gil', 6, 6))
Prevtori = Mobs('Prevtori', 4, 15)
monstros_easy = [
    Mobs('Babuíno', 2, 10),
    Mobs('Petista', 1, 8),
    Mobs('Tirulipa', 2, 7),
    Mobs('Pé de bota', 1, 7),
    Mobs('Palhaço do Vasco', 2, 6),
    Mobs('Peba', 1, 6)
]
monstros_medium = [
    Mobs('Felipe Neto', 3, 15),
    Mobs('Dava Jonas', 1, 20),
    Mobs('Pitbull', 4, 12),
    Mobs('Petista', 3, 13),
    Mobs('Bolsominion', 3, 17),
    Mobs('Jessica', 3, 16),

]
monstros_hard = [
    Mobs('o Negão da Piroca', 8, 20),
    Mobs('o Menino Porco', 7, 25),
    Mobs('a Lady Gaga', 6, 22),
    Mobs('a Rainha Elizabeth', 5, 35),
    Mobs('o Bolso-Lula', 13, 17),
    Mobs('o Famoso', 5, 26)
]
armas = [
    Arma('Mão', 1),
    Arma('Tijolo', 2),
    Arma('Canivete', 3),
    Arma('Machado', 4),
    Arma('Revolver', 5),
    Arma('Espingarda', 6)
]
armaduras = [
    Armadura('Trapos', 0),
    Armadura('jeans', 3),
    Armadura('Jaqueta', 5),
    Armadura('Colete', 7),
    Armadura('Armdura tática', 10),
    Armadura('Cueca de couro', 15)
]
caminhos = ['Rua deserta',
            'Ponte',
            'Caverna',
            'Viela escura',
            'Mata fechada',
            'Igreja'
]
mortes_jogador = ['Te Quebrou na porrada',
                  'Te partiu no meio',
                  'Te deu uma facada e saiu correndo',
                  'Mordeu sua virilha',
                  'Te bateu bem no ovo direito',
                  'Te deu um olhar 43 intankavél'
]


def morte():
    tipos_morte_player = ['O cara foi solado q nem clickou kkkkkk',
                          'Foi de base, F no chat',
                          'Infelizmente não tankou e foi de berço...',
                          'Capotou o corsa...',
                          'Você foi escalado pro Vasco...',
                          'Você foi de Jackson five...',
                          'Infelizmente você não tankou a cirurgia e foi de base as 19:35',
                          'Você deu o peido mestre...']
    print(tipos_morte_player[random.randint(0, 7)])
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
    monstro_vida = minion.vida
    dano = minion.dano
    monstro_raca = minion.raca
    player_vida = armadura.vida + 5
    print(f'Seu oponente é um {monstro_raca} que merece morrer!\n'
          f'Ele possui {monstro_vida} de vida e {dano} de ataque!')
    print(f'Seu equipamento é:\nArma: {arma.nome} com dano de {arma.dano}\n'
          f'Armadura: {armadura.nome} com vida de {armadura.vida}, sua vida total é: {player_vida}')
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
                print(f"Foi efetivo pra caralho!! {1 * arma.dano * 2} de dano! Ele não esperava nunca isso")
                time.sleep(2)
            elif hit >= 100:
                monstro_vida -= 1 * arma.dano
                print(f"Você causou {1 * arma.dano} de dano!!")
                time.sleep(1)
            else:
                print(f'Você errou!!')
        if atk == "2":
            print(f'Você tentou dar um {hit_medio[alea5()]}...')
            time.sleep(1.5)
            hit = random.randint(0, 1000)
            if hit >= 900:
                monstro_vida -= 2 * arma.dano * 2
                print(f"Acabou o brinquedo pow, da não... deu {2 * arma.dano * 2} de dano nesse viado... F")
                time.sleep(2)
            elif hit >= 300:
                monstro_vida -= 2 * arma.dano
                print(f"Você causou {2 * arma.dano} de dano!!")
                time.sleep(1)
            else:
                print(f'Você errou!!')
        if atk == "3":
            print(f'Você tentou dar um {hit_forte[alea5()]}...')
            time.sleep(1.5)
            hit = random.randint(0, 1000)
            if hit >= 900:
                monstro_vida -= 3 * arma.dano * 2
                print(f"Eita porra... É valendo fazenda?? \n"
                      f"Tu só meteu {3 * arma.dano * 2} de dano na bunda desse viado... precisava disso?")
                time.sleep(3)
            elif hit >= 500:
                monstro_vida -= 3 * arma.dano
                print(f"Você causou {3 * arma.dano} de dano!!")
                time.sleep(1)
            else:
                print(f'Você errou!!')
                time.sleep(1)
        if atk == "4":
            hit_monstro = 100
            print("Vôce se defendeu igual um covarde e fez o inimigo errar!")
        print(f'O {monstro_raca} avança...')
        time.sleep(1.5)
        if hit_monstro >= 900:
            player_vida -= dano * 2
            print(f'Tá maluco!!!! o {monstro_raca} meteu um CRITÃO KKKKKK\n'
                  f'O Inimigo te jantou com {dano * 2} de dano!')
            time.sleep(2.5)
        elif hit_monstro >= 400:
            player_vida -= dano
            print(f'O Inimigo te causou {dano} de dano!')
            time.sleep(1.5)
        elif hit_monstro < 400:
            print('O Inimigo errou o ataque!')
            time.sleep(1.5)
        print(f'--Sua vida restante é: {player_vida}\n--Vida restante do {monstro_raca} é: {monstro_vida}')
    if player_vida > 0:
        print(f"Você conseguiu!! solou o {monstro_raca}")
        return 1
    else:
        print("Você foi solado e o resto é história")
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
        chute = [c1, c2, c3, c4, c5]
        resposta_final = ''
        a = 0
        for chutes in chute:
            if chutes == resposta[a]:
                resposta_final = resposta_final + 'V '
                a += 1
            elif chutes != resposta[a]:
                resposta_final = resposta_final + 'x '
                a += 1
        print(resposta_final)
        if chute == resposta:
            print('Parabéns!!')
            acertou = True


def minijogo_2():
    numa = random.randint(1, 10)
    print('Você ta entrando em uma luta!!!'
          '\nVocê tem Três chances de acertar o número de 1 a 10!')
    acerto = False
    chutes = 0
    while acerto is False and chutes <= 2:
        print('Você tem ' + str(3 - chutes) + ' Chutes')
        chute = int(input('Fala um número de 1 a 10:\n'))
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


def final_alt():
    new_nome1 = 'Pr' + nome[3:]
    new_nome2 = nome[:-3] + 'tori'
    nome_final = 'Prev' + nome[2:-3] + 'tori'
    print('Prevtori está morto...')
    print('Agora sem saber pra que direção seguir nem oque fazer você está perdido...')
    print('Você vaga revira a cabana a procura de alguma pista ou algo útil')
    andadas = 0
    esquerda = 0
    while andadas <= 5 and esquerda <= 1:
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
        return
    else:
        print('O tempo passa e tudo oque você encotra é um grande estoque de comida que parece ilimitado\n'
              'Você vê o tempo passar e suas mãos se enrugarem...\n'
              'a unica coisa que te chama atenção é o barulho do vento nessa ' + local_zero + '...')
        time.sleep(1.5)
        print('parece até um nome.... Prevtori.... e isso lá é um nome? e por falar nisso qual era o meu?')
        time.sleep(1.5)
        print('Você pensa e pensa.... qual era mesmo? ' + new_nome1 + '?.. ou era ' + nome + '?... quem sabe '
              + new_nome2 + '....')
        time.sleep(1.5)
        print('Quase certeza que era ' + nome_final + '... \n'
                                                      'Não... na verdade acho que era só Prevtori mesmo...')
        time.sleep(1.5)
        print('Após oque parecem decadas você vê um jovem correndo em sua direção e você berra: \n'
              '-Você ai!'
              '\n-Onde você pensa que vai? essa é a minha cabana!')

3
arma_nivel = 1
armadura_nivel = 2
print(f'Seu equipamento inicial são {armaduras[armadura_nivel].nome} e '
      f'{armas[arma_nivel].nome} que não dão nenhuma vantagem!')
print('Digite apenas o número desejado pra evitar quebrar o jogo e ter q recomeçar :)')
time.sleep(2.5)

# Primeira parte -------------------------------------------------------------------------------------------------------

print('-----PRIMEIRA PARTE------')
print('*** Você acorda meio tonto...***')
time.sleep(1.5)
print('-Qual é a de menos? Bicho fresco - disse um homem alto, grisalho e quem sabe afrescado'
      '\n-Tá com sono?')
print('1- Eu estou perdido, você pode me ajudar?'
      '\n2- Eu só quero morrer...')
dec0 = input('Digite 1 ou 2:\n ')
if dec0 == '2':
    print('-Seu desejo é uma ordem parceiro!\n'
          '***Quando você se dá conta ele ' + mortes_jogador[alea5()])
    morte()
print('-Tô de boas, mas acho que sei quem pode te ajudar, é um tal de Prevtori... Diz o Homem'
      '\n- A proposíto... qual seu nome?')
nome = input('Qual seu nome?\n ')
if nome == 'Prevtori':
    print('- Ha Ha Ha...  Debocha o Homem. \n'
          '-Eu já ouvi esse nome antes... quero ver como você vai fazer depois')
else:
    print('-Aaah... que nome estranho... ' + nome + '...nunca ouvi falar')
print('-Então ' + nome + ' siga pela direita eu acho... ou era esquerda?... não! era a direita mesmo!')
print('-Agora vaza!')
print('***Qual direção seguir?*** \n1- Esquerda\n2- Direita\n ')
dec1 = input('Digite 1 ou 2:\n ')
if dec1 == '1':
    creep1 = monstros_easy[alea5()]
    print(f'***Você encontrou um {creep1.raca}!!!!')
    confronto1 = luta(creep1, armas[arma_nivel], armaduras[armadura_nivel])
    if confronto1 == 1:
        print(f'***Voce matou o {creep1.raca}'
              f', mas encontrou um caminho sem saída... '
              f'Pelo menos você conseguiu pegar o jeans do {creep1.raca}!'
              f'Você tem que voltar e continuar por outro caminho')
        armadura_nivel += 1
    elif confronto1 == 2:
        print(f'Infelizmente o {creep1.raca} tinha mais oque fazer e decidiu não te matar '
              f'por que você tá no tutorial ainda!\n'
              f'Você se levanta e tem que voltar pois não ha saidas além de outra surra...')
print('***Você segue por um longo corredor iluminado por velhas lâmpadas, algumas queimadas...')
time.sleep(1.5)
print('***Você se depara com uma porta e precisa decidir....')
print('1- Seguir pra fora do prédio\n2- Voltar')
dec2 = input('Digite 1 ou 2:\n ')
if dec2 == '1':
    print('***Você segue pra fora e vê que está escurecendo\n'
          '***Você segue o unico caminho de pedrinhas até avistar uma velha cabana...')
    time.sleep(1.5)
if dec2 == '2':
    matador1 = monstros_hard[alea5()]
    print(f'***Quando você se vira você esbarra em n{matador1.raca}... Melhor meter o pé ein\n'
          f'{matador1.raca} tem vida de {matador1.vida} e dano de {matador1.dano}...')
    time.sleep(1.5)
    print(f'Quer tentar meter a mão na cara d{matador1.raca}?\n'
          f'1 - Sim, eu tô maluco biruta crazy alucinado!\n'
          f'2 - Tô tranquileba meu parceiro, vou ralar peito!')
    perigo1 = input('Digite 1 ou 2:\n')
    if perigo1 == '1':
        confronto_impo1 = luta(matador1, armas[arma_nivel], armaduras[armadura_nivel])
        if confronto_impo1 == 1:
            print('Caralho, eu acho que tu tá de hack, mas como esse jogo não tem segurança nenhuma pega ai:\n'
                  'VOCÊ ENCONTROU UM FUCKING REVOLVER!')
            arma_nivel += 4
        elif confronto_impo1 == 2:
            print('Eu te avisei... vai tomar um reset de trouxa tbm')
            morte()
    else:
        print('***Você da uma de Jõao sem braço e segue seu caminho')
print('***Você entra na cabana e encontra quem aquele cara tinha falado '
      'e se da conta de q não perguntou o nome dele.')
print('***Você decide dar um nome a ele, qual vai ser?')
chefe = input('Nome do doido lá:\n ')

# Segunda parte --------------------------------------------------------------------------------------------------------

print('-----SEGUNDA PARTE------')
time.sleep(1.5)
print('-Você ai! - Berra um velho acabado igual maracuja de gaveta\n'
      '-Onde você pensa que vai? essa é a minha cabana!')
print('***Você encara a múmia velha e decide se parte pra cima dele ou se conversa...')
dec3 = input('1- Partir pra cima e arrebentar esse velho broxa\n'
             '2- tentar acalmar o corno manso\n')
velho_vivo = True
while velho_vivo is True:
    if dec3 == '1':
        luta_prev = luta(Prevtori, armas[arma_nivel], armaduras[armadura_nivel])
        if luta_prev == 1:
            print('***Voce matou um dos contrutores da Arca de Noé...')
            velho_vivo = False
            final_alt()
            break
        elif luta_prev == 2:
            print(morte_especial())
    print('Você se apresenta como ' + nome +
          ' e conta que não lembra de nada e nem sabe como foi parar ali\n'
          'E conta que se encontrou com o ' + chefe + ' que disse que ele te ajudaria.')
    time.sleep(1.5)
    if nome == 'Prevtori':
        print('-Além de não fazer ideia de quem é ' + chefe + ' Que merda é essa?? Você tá brincando '
                                                              'com a minha cara né?\n'
              '-Ninguém tem o mesmo nome que eu... Seu Impostor!!!')
        luta_prev = luta(Prevtori, armas[arma_nivel], armaduras[armadura_nivel])
        if luta_prev == 1:
            print('***Voce matou um dos contrutores da Arca de Noé...')
            velho_vivo = False
            final_alt()
            break
        elif luta_prev == 2:
            print(morte_especial())
    print('O velho te encara por um tempo e te pergunta:\n'
          '-E quem porra é ' + chefe + '? e que nome de bicho é esse? ' + nome + '.... nunca ouvi falar')
    print('-O meu Nome é Prevtori, mas pode me chamar de Prevtori')
    esp = input('Tá me entendendo?\n'
                'qual é o meu nome?\n ')
    tentativas = 0
    while esp != 'Prevtori':
        esp = input('Escreve direito Viado!!:\n')
        tentativas += 1
        if tentativas == 3:
            print('Não tenho tempo pra isso não... Tá fudido na minha mão parceiro!')
            luta_prev = luta(Prevtori, armas[arma_nivel], armaduras[armadura_nivel])
            if luta_prev == 1:
                print('***Voce matou um dos contrutores da Arca de Noé...')
                velho_vivo = False
                final_alt()
                break
            elif luta_prev == 2:
                print(morte_especial())
    print('-Hmmmm... Pelo menos não é surdo... Mas como você '
          'invadiu minha ' + local_zero + ' ou você me faz um favor ou você vai tomar um reset')
    print('***Eai meu parceiro? vai deixar esse porra de Prevtori falar assim contigo???\n'
          '1- Tá maluco? esse velho tem cara de doido, melhor fazer oque ele quer...\n'
          '2- Eu não nasci um Corno pra levar desaforo pra casa, vou partir esse velho baitola no meio\n')
    dec4 = input('Digite 1 ou 2:\n ')
    if dec4 == '1':
        print('***Você fala calmamente: \n'
              '-Éoque doido do caralho, para com essa porra ai, oque que tu quer que eu faça?')
    elif dec4 == '2':
        print('Bora vê então aki seu velho goiaba do caralho!!')
        luta_prev = luta(Prevtori, armas[arma_nivel], armaduras[armadura_nivel])
        if luta_prev == 1:
            print('***Voce matou um dos contrutores da Arca de Noé...')
            velho_vivo = False
            final_alt()
            break
        elif luta_prev == 2:
            print(morte_especial())


        # Terceira parte -------------------------------------------------------------------------------------------------------

        # Rua Deserta
    completo = False
    repetir_predio1 = False
    repetir_predio2 = False
    repetir_predio3 = False
    print('***Você recebe a missão de Prevtori que te pede para procurar nos predios ao redor o seu velho diario...')
    time.sleep(1.5)
    print('***Você entra na Rua Deserta')
    print('***Você vê 3 prédios que batem com a descrição do Velho goiaba, um na esquerda e dois na direita.')
    time.sleep(1.5)
    print('Qual deles você quer entrar primeiro?')
    indecisao = 0
    while indecisao <= 8 and completo is False:
        print('1- Prédio da Esquerda\n2- Prédio da Direita perto\n3- Prédio da direita longe')
        dec5 = input('Digite 1, 2 ou 3:\n ')
        if dec5 == '1' and repetir_predio1 is True:
            print('Não há mais nada aqui que possa me interessar.')
        if dec5 == '2' and repetir_predio2 is True:
            print('***Você decide Voltar e Entregar o diário!***')
            completo = True
        if dec5 == '3' and repetir_predio3 is True:
            print('Não há mais nada aqui que possa me interessar.')
        if dec5 == '1' and repetir_predio1 is False:
            print('O prédio parece abandonado... apenas mobilia velha e empoeirada, '
                  'você entra em uma sala e vê um vulto num canto.')
            time.sleep(1.5)
            print('Você quer se aproximar?\n1- Sim, qualquer coisa eu mato ele na porrada oush\n'
                  '2- Não, tá maluco,doido, biluteteia??? imagina chegar até aki e morrer de bobeira pra um Flamenguista??')
            predio_1 = input('Digite 1 ou 2:\n ')
            if predio_1 == '1':
                creep2 = monstros_easy[alea5()]
                print('Você se aproxima e percebe que é um ' + creep2.raca + ' puto da cara!')
                time.sleep(1.5)
                confronto2 = luta(creep2, armas[arma_nivel], armaduras[armadura_nivel])
                if confronto2 == 1:
                    print('Você vê o corpo dele sem vida e Pensa sozinho:\n'
                          'Como foi fácil acabar com ele...\n')
                    time.sleep(1.5)
                    print('*** Você encontra um... ' + armas[1].nome + '!!!, sua nova arma!!')
                    print('Você não vê mais nada de útil nesse prédio e volta para a rua...')
                    arma_nivel += 1
                    indecisao -= 1
                    repetir_predio1 = True
                else:
                    morte()
            if predio_1 == '2':
                indecisao += 1
                print('Você volta pra rua e tem que decidir pra onde vai...')
        elif dec5 == '2' and repetir_predio2 is False:
            print('Você anda pela direita e entra no primeiro prédio, dentro dele você encontra varias caixas.\n'
                  'A Velha gagá do Prevtori tinhe lhe falado dessas caixas!! o diario deve estar aqui!!\n'
                  'Você decide dar uma olhada nas caixas...')
            time.sleep(1.5)
            print('Você vê 12 caixas, em qual delas você quer olhar?')
            chute = 15
            demora = 0
            while chute != 0 and demora <= 11:
                giro = random.randint(1, 12)
                chute = int(input('Em qual caixa vc quer procurar de 1 a 12? \n (0 para sair da casa)\n '))
                if chute == 0:
                    break
                elif chute == giro:
                    print('CARALHO!!! Você encontrou o diário daquele velho broxa!!!\n'
                          'Você volta para a rua com o objetivo da missão em mãos\n'
                          '***Ir novamente para o Prédio 2 completará a missão***')
                    repetir_predio2 = True
                    indecisao -= 4
                    time.sleep(1.5)
                    completo = True
                    break
                elif chute != giro:
                    print('Você NÃO encontra nada e quando levanta os olhos vc sente que '
                          'alguém embaralhou as caixas novamente...\n'
                          'Você não tem todo o tempo do mundo...')
                    demora += 1
            if demora >= 11:
                creep3 = monstros_easy[alea5()]
                print(f'Você está tão concentrado em tentar achar um padrão que não nota um {creep3.raca} que chegou '
                      f'\n por trás e está te atacando!')
                time.sleep(1.5)
                confronto3 = (creep3, armas[arma_nivel], armaduras[armadura_nivel])
                if confronto3 == 1 :
                    print(f'Você consegue se livrar do {creep3.raca} e pode voltar a procurar em paz....')
                    time.sleep(1.5)
                    print('Mas por quanto tempo?')
                    indecisao -= random.randint(5, 11)
                elif confronto3 == 2:
                    morte()
            print('Você volta a Rua...')
            indecisao += 1
        elif dec5 == '3' and repetir_predio3 is False:
            print('Você anda sozinho em direção ao Prédio na esquina e se sente observado...\n'
                  'Você chega na sua porta e vê que ela está trancada...\n'
                  'Você quer:\n'
                  '1- Tentar arrombar a porta.\n'
                  '2- Voltar pra trás.')
            dec3 = input('Digite 1 ou 2:\n ')
            if dec3 == '1':
                print('Você se prepara... Toma distância e corre com tudo contra a porta...')
                time.sleep(1.5)
                print('Você escuta um CRACK\n\nA porta parece inteira e quando você olha pra baixo a última'
                      ' coisa que você nota antes de tudo ficar escuro\né o seu ombro fora do lugar')
                time.sleep(2.5)
                guerreiro1 = monstros_medium[alea5()]
                print(f'\nQuando você acorda você vê um {guerreiro1.raca} te olhando de cima e não tem escolha.')
                time.sleep(0.5)
                print('Você precisa se defender!')
                confronto_med1 = luta(guerreiro1, armas[arma_nivel], armaduras[armadura_nivel])
                if confronto_med1 == 1:
                    print(f'Mesmo ferido acabou com o {guerreiro1.raca} e como todo bom aventureiro\n'
                          f'você vai saquear o cadaver sem se importar no quanto imoral e antiético isso é!')
                    time.sleep(1.5)
                    print('Você encontrou uma armadura melhor!!')
                    armadura_nivel += 1
                    print(f'Agora você está vestindo: {armaduras[armadura_nivel].nome} '
                          f'com um bônus de {armaduras[armadura_nivel].vida} de vida! ')
                    time.sleep(2.5)
                    print('Você volta a porta e perceb que ela na verdade é apenas uma pintura na parede...\n'
                          'Burrão ein?')
                    time.sleep(1.5)
                    print('Ainda bem que a unica testemunha está sendo devorada por ratos neste exato momento XD!\n'
                          '***Você volta para a Rua pra procurar em outo lugar!')
                    repetir_predio3 = True
                elif confronto_med1 == 2:
                    morte()
            if dec3 == '2':
                print('Você sente um frio na espinha e olha ao redor...\nTá maluco que eu vou ficar aki!'
                      '\nVocê volta num pique que deixaria o Usain comendo poeira!'
                      '\n Se eu voltar ali eu sou um corno! Tá maluco boy.')
                time.sleep(1.5)
                indecisao += 2
    if indecisao >= 8:
        print('Você se sente perdido e quando se da conta você acorda morto')
        morte()
    elif completo is True:
        print('Você volta correndo pra devolver aquela merda pro velho broxa!!\n'
              'mas Lembra que ele te pediu para não ler o diario... eai meu parceiro?\n')
        time.sleep(2)
        print('Vai escutar aquela quenga velha ou vai ser um pau no cu?\n'
              '1- Amarelar igual uma bicha, escutar o Velho Corno e ficar na curiosidade\n'
              '2- Ser um Pau no cu do Caralho e ler os segredos obscuros do Prev "Rola-murcha" tori?')
        diario = int(input('Digite 1 ou 2:\n '))
        if diario == 1:
            print('Você decide ser uma boa moça e seguir com a missão à risca! (com crase ein)')
            time.sleep(2)
            print('Você chega ao Prevtori e lhe entrega o diário!')
        elif diario == 2:
            print('-Aquele Velho baitola não manda nem na biscate da mulher dele vai mandar em mim?')
            time.sleep(2)
            print('Você descobre que o Velho era um cara que apareceu perdido aqui muito tempo atrás\n'
                  'e que com o tempo foi perdendo a memoria e do nada decidiu que iria se chamar Prevtori!!\n')
            time.sleep(2)
            print('Que parada zoada ein... quem inventou essa merda de roteiro?')
            time.sleep(1)
            print('Pelo seu olhar o Velho viado já sabe oque você fez\n'
                  'Ele não nasceu ontem e da pra saber só de olhar!\n'
                  'Quando você abre a boca pra falar o Prevtori avança em sua direção!')
            luta_prev = luta(Prevtori, armas[arma_nivel], armaduras[armadura_nivel])
            if luta_prev == 1:
                print('***Voce matou um dos contrutores da Arca de Noé...')
                velho_vivo = False
                final_alt()
                break
            elif luta_prev == 2:
                print(morte_especial())
if velho_vivo is False:
    print('merda! talvez já pule a proxima parte? ou pule as proximas duas e continue igual')





def missao(local_zero):
    drop = 0
    completo = False

    if local_zero == caminhos[1]:
        # Ponte
        print('Você recebe a missão de Prevtori que te pede para procurar nos Carros o seu velho diario...')
        print('Você entra na ' + local_zero)
        print('Você começa a caminhar entre os carros que parecem abandonados a décadas.'
              'Alguns deles te chamam a atenção! Qual deles você quer olhar primeiro?')
        carro1 = False
        carro2 = False
        carro3 = False
        carro4 = False
        carro5 = False
        while completo is False:
            car = input('1- Marea preto\n'
                        '2- Pegeout prata\n'
                        '3- Fusca Azul\n'
                        '4- Camaro Vermelha\n'
                        '5- Brasília Amarela\n:  ')
            if car == '4' and carro4 is True:
                completo = True
                break
            elif car == '1' and carro1 is True:
                print('Não tem mais o que ver ali além de um marea sendo um marea.')
            elif car == '2' and carro2 is True:
                print('Não tem mais o que ver ali, vai que você realmente adquire um pegeout?')
            elif car == '3' and carro3 is True:
                print('Não tem mais o que ver ali, o Fusca Azul gera agressão involuntaria')
            elif car == '5' and carro5 is True:
                print('Não tem mais o que ver ali.')
            if car == '1' and carro1 is False:
                print('Você se aproxima do Marea com cuidado, ele parece estranho e o risco '
                      'de combustão espontanêa é real!')
                car1 = input('Você quer correr o risco?\n1- Sim, eu tô maluco biluteteia biruta da cabeça\n'
                             '2- não comi merda não meu parceiro, perto de um Marea eu só chego depois de morto!\n ')
                if car1 == '1':
                    print('Parece que você comeu merda meu amigo, vc se aproxima e escuta um barulho alto vindo '
                          'dele antes de vê a bola de fogo!\nVocê deu sorte, mais um passo '
                          'pra frente e você tinha perdido mais do que só as sombrancelhas!')
                    carro1 = True
                if car1 == '2':
                    print('Você decide seguir a razão e recua, após o segundo passo você vê a bola de fogo!\n'
                          'o Marea explodiu como de costume e você agradece por esta a uma distancia segura!')
                    carro1 = True
            if car == '2' and carro2 is False:
                print('Você se aproxima do Pegeout e começa a sentir o perigo de adquirir um deles\n'
                      'Você agradece por não ter a sua carteira com você pra nem correr o risco de comprar.')
                print('Dentro dele você vê o que uma alma penada, talvez condenada a ficar aqui até vender o carro!')
                ajud = input('Você quer tentar ajudar a alma artomentada?\n1- Sim, ninguém merece um carro assim, '
                             'vamos tentar da a segunda alegria do dono de pegeout\n'
                             '2- Melhor não, se ele me empurra esse monstro eu vou ficar preso aqui também....\n ')
                if ajud == '1':
                    print('Você se aproxima e o Fantasma ja lhe pergunta se '
                          'você tem interesse no Pegeout 206 prata, 2 portas,\n'
                          'tudo funcionando, só o ar q tá meio fraco, mas nada que uma janela aberta não resolva!\n'
                          'Você diz que quer dar uma olhada e ele te olha com os olhos marejados.\n- Obrigado... '
                          'Você é um Héroi! - ele diz e desaparece!\n'
                          'Ele só precisava que alguem com noção demonstrasse interesse no carro...\n'
                          'Essa foi fácil, apesar de arriscadíssimo!')
                    print('***Você encontrou um ' + armas[1].nome + ' em baixo de um dos Pneus***')
                    drop += 1
                    carro2 = True
                if ajud == '2':
                    print('Você é um homem sensato e não deixou que um fantasma que caiu na arapuca te puxasse junto!\n'
                          'Você vai conseguir dormir em paz sabendo que não tem um pegeout na garagem.')
            if car == '3' and carro3 is False:
                print('Você se aproxima do fusca azul e um ' + monstros[alea5()].raca +
                      ' Aparece do nada e vem te agredir gritando "Fusca Azul!", '
                      'você não tem alternativa além de se defender!')
                car3 = luta_facil(drop)
                carro3 = True
                if car3 == 1:
                    print('Você acabou com a raça daquele corno infantil!, mas não encontra \n'
                          'nada além de um belo fusca azul!')
                    carro3 = True
                if car3 == 2:
                    print('Ele acerta o seu braço com uma força jamais vista...')
                    morte()
            if car == '4' and carro4 is False:
                print('Você se aproxima do Camaro e pensa quem era o Playboy q dirigia ese Bumblebee vermelho...\n'
                      'ao olhar no banco de trás você encontra um livro, mas a porta está trancada!\n'
                      'Você precisa de alguma coisa para quebrar o vidro! ')
                if drop >= 1:
                    print('***Você usa o tijolo para Arrebentar o vidro do '
                          'Camaro e consegue o Diário do velho broxa!***\n'
                          'Vir novamente ao Camaro completará a missão!')
                    carro4 = True
                else:
                    print('***Você tem que procurar em outros lugares!***')
            if car == '5' and carro5 is False:
                print('Você se aproxima da Brasília amarela e observa que suas portas estão abertas!\n'
                      'Apesar dessa cena lhe parecer familiar você não encontra nada de útil nela...')
                carro5 = True
    if local_zero == caminhos[2]:
        # Caverna
        print('Você recebe a missão de Prevtori que te pede para procurar ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
        print('Você está num breu que não consegue nem ver oque está a sua frente!\n'
              'Suas opções são limitadas! o máximo que você pode fazer é sair tateando!\n'
              'para que lado você quer tatear?\n'
              '1- Esquerda\n2- Direita\n3- Frente')
        while completo is False:
            input('Digite 1, 2 ou 3:\n ')
            print('Você adentra na escuridão e no segundo passo sem vê a entrada da caverna você se perde...')
            print('Você não sabe nem pra que lado fica o teto... agora é tudo sorte!\nAdivinhe um número de 1 a 15!')
            saida = random.randint(0, 15)
            acerto = False
            desculpa = False
            tempo = 0
            while acerto is False:
                while desculpa is False:
                    chute = int(input('Qual seu chute de 1  a 15?\n  '))
                    if chute == saida:
                        desculpa = True
                    elif chute < 7:
                        print('Não consigo ver nada, mas parece ser um beco sem saída.')
                        tempo += 1
                    elif chute >= 7:
                        print('Droga... não pode ser por aqui... apenas pedras.')
                        tempo += 1
                    if tempo == 3:
                        print('Droga... eu não sei se escutei alguma coisa ou se foi algo da minha cabeça...')
                    if tempo == 5:
                        print('Eu tenho certeza que ouvi alguma coisa!! que merda é essa?')
                    if tempo == 7:
                        print('PORRRA! esse bicho tá do meu lado... eu posso sentir o seu cheiro Podre!')
                    if tempo == 8:
                        print('Uma criatura te ataca e te derruba no chão, apesar do breu você precisa se defender!')
                        resu = luta_facil(drop)
                        if resu == 1:
                            print('Você consegue se desvencilhar e correr!\n'
                                  'Ainda está perdido, pelo menos consegue um pouco mais de tempo!')
                            tempo -= 5
                        elif resu == 2:
                            print('A Criatura finca seus dentes na sua garganta...')
                            print(morte())
                print('***Você encontrou o Diario do Velho viado Prevtori!!!\n'
                      '*** Você encontra um... ' + armas[1].nome + '!!!, sua nova arma!!\n'
                      'Mas agora você precisa achar a saída!! e a Criatura se aproxima\n'
                      '1- Derrotar a Criatura e sair sem pressa\n'
                      '2- Fugir e tentar a sorte encontrando a sáida')
                drop += 1
                lut = int(input('Digite 1 ou 2:\n '))
                if lut == 1:
                    luta = luta_facil(drop)
                    if luta == 1:
                        print('Você consegue vencer a criatura que agora você examina e descobre que era\n'
                              'apenas uma capivara enorme... bem, antes ela do que eu!\n'
                              'Você vaga pela caverna sem pressa até encontrar a luz que vem de sua entrada.')
                        acerto = True
                        completo = True
                    if luta == 2:
                        print('A Criatura é mais forte do que você imaginava... Você é obrigado a fugir!')
                        lut = 2
                if lut == 2:
                    print('Você está correndo no escuro... 50% de chance de dar merda...')
                    bola = random.randint(1, 2)
                    chut = int(input('Digite 1 ou 2:\n '))
                    if chut == bola:
                        print('Você corre no breu aos tropeços até que comeca a ver a luz da entrada da caverna!\n'
                              'Ainda bem que está de dia!! apesar de você não saber se ainda é do mesmo dia...')
                        acerto = True
                        completo = True
                    else:
                        print('Você corre para uma beco sem saída... pelo menos você não '
                              'consegue ver oque vai acontecer com você...'
                              '\nA ultima coisa que você sente é o Bafo da criatura na sua nuca')
                        print(morte())
    if local_zero == caminhos[3]:
        # Viela Escura
        drop = 0
        print('Você recebe a missão de Prevtori que te pede para procurar nos predios ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
        time.sleep(1.5)
        print('Você não se sente seguro andando sozinho por uma viela assim.... o sentimento de ser observado não sai '
              'da sua cabeça...')
        time.sleep(1.5)
        print('Não há muito oque ver aqui também... Você só nota oque parece ser um abrigo de um '
              'mendigo que parece abandonado\n'
              'Você não tem muito oque fazer se não investigar')
        time.sleep(1.5)
        print('- O QUE PORRA VOCÊ TA FAZENDO AI???')
        time.sleep(0.5)
        print('Você toma um susto gigante e quando olha pra trás não vê ninguém...\n'
              'Que merda é essa...')
        time.sleep(1)
        print('Você volta a procurar e acha uma caixa com um cadeado de uma senha numerica\n'
              'A tecnologia dela é convenientemente fácil de ser arrombada, já que ele da dicas da senha!!\n'
              'A senha possui 5 Digitos!')
        mini_jogo_1()
        print('a Caixa se abre e você encontra um velho diário do velho viado Prevtori dentro dela e '
              'uma arma!!!\n'
              '***Você encontrou o Diario do Velho viado Prevtori!!!\n'
              '*** Você encontra um... ' + armas[1].nome + '!!!, sua nova arma!!\n')
        drop += 1
        completo = True

    if local_zero == caminhos[4]:
        # Mata Fechada
        drop = 0
        print('Você recebe a missão de Prevtori que te pede para procurar nos arbustos ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
    if local_zero == caminhos[5]:
        # Igreja
        drop = 0
        print('Você recebe a missão de Prevtori que te pede para procurar ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)


# Próxima parte do jogo



'''
local_zero = caminhos[alea5()]
creep1 = monstros[alea5()].raca
creep2 = monstros[alea5()].raca
nome = tutorial()
chefe = transicao1()
prevtori = segunda_parte()
if prevtori == False:
    final_alt()
elif prevtori == True:
   print('Prevtori te da uma missão...')
r_missao = missao(local_zero)
if r_missao == 1:
    print('Você chega ao Prevtori e lhe entrega o diário!')
if r_missao == 2:
    print('Pelo seu olhar o Velho viado já sabe oque você fez\n'
          'Apesar dele parecer uma múmia ele não nasceu ontem!!'
          '\nQuando você abre a boca pra falar o Prevtori avança em sua direção!!')
    resul = luta_dificil(drop)
    if resul == 1:
        print('***Voce matou um dos contrutores da Arca de Noé...')
    elif resul == 2:
        print(morte_especial())
'''
# Coisas que faltam fazer...
# Caminhos 4 e 5
# Final alternativo voltar para o final verdadeiro
# Final verdadeiro
# Quantas missões antes do Final verdadeiro?
# Prevtori ajuda você na batalha final?
