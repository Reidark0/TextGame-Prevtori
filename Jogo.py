import random
from mob import mobs
from mob import arma

monstros = [
    mobs('Troll', 3, 10),
    mobs('Petista', 1, 5),
    mobs('Flamenguista', 4, 4),
    mobs('Goiano', 2, 7),
    mobs('Palmeirense', 3, 5),
    mobs('Pivete', 1, 3)
]
armas = [
    arma('Mão', 0),
    arma('Tijolo', 1),
    arma('Canivete', 2),
    arma('Machado', 3),
    arma('Revolver', 4),
]
caminhos = ['Rua deserta',
            'Ponte',
            'Caverna',
            'Viela escura',
            'Mata fechada',
            'Igreja']
mortes_jogador = ['Te Quebrou na porrada',
                  'Te partiu no meio',
                  'Te deu uma facada e saiu correndo',
                  'Mordeu sua virilha',
                  'Te bateu bem no ovo direito',
                  'Te deu uma saudade dela intankavel']


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


def luta_dificil(drop):
    defesa = armas[drop]
    maxi = 10 - defesa.dano
    numa = random.randint(1, maxi)
    print('Você ta entrando em uma luta Difícil!!!\n'
          'Você está lutando com ' + defesa.nome + ' que reduz o numero máximo em: ' + str(defesa.dano) +
          '\nVocê tem duas chances de acertar o número de 1 a ' + str(maxi) + '!')
    acerto = False
    chutes = 0
    while acerto == False and chutes <= 1:
        print('Você tem ' + str(2 - chutes) + ' Chutes')
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
        print('Você ganhou! Foi apertado, mas esse Corno não foi perigo nem por um segundo!')
        return 1

def luta_facil(drop):
    defesa = armas[drop]
    maxi = 10 - defesa.dano
    numa = random.randint(1, maxi)
    print('Você ta entrando em uma luta!!!\n'
          'Você está lutando com ' + defesa.nome + ' que reduz o numero máximo em: ' + str(defesa.dano) +
          '\nVocê tem duas chances de acertar o número de 1 a ' + str(maxi) + '!')
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
        print('Você ganhou! Acabou com a raça desse Viadinho.')
        return 1

def luta_impo(drop):
    defesa = armas[drop]
    maxi = 10 - defesa.dano
    numa = random.randint(1, maxi)
    print('Você ta entrando em uma luta Quase Impossível!!!\n'
          'Você está lutando com ' + defesa.nome + ' que reduz o numero máximo em: ' + str(defesa.dano) +
          '\nVocê tem duas chances de acertar o número de 1 a ' + str(maxi) + '!')
    acerto = False
    chutes = 0
    while acerto == False and chutes <= 0:
        print('Você tem ' + str(1 - chutes) + ' Chutes')
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


def tutorial():
    drop = 0
    print('*** Você acorda meio tonto...***')
    print('-Qual é a de menos? Bicho fresco... - disse um homem alto, grisalho e quem sabe afrescado'
          '\n-Tá com sono?')
    print('1- Eu estou perdido, você pode me ajudar?'
          '\n2- Eu só quero morrer...')
    dec0 = input('Digite 1 ou 2:\n ')
    if int(dec0) == 1:
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
        dec1 = int(input('Digite 1 ou 2:\n '))
        if dec1 == 1:
            print('***Você encontrou um ' + creep1 + '!!!!')
            luta = luta_facil(drop)
            if luta == 1:
                print('***Voce matou o ' + creep1 +
                      ', mas encontrou um caminho sem saída... '
                      'Você tem que voltar e continuar por outro caminho')
            elif luta == 2:
                print('Infelizmente o  ' + creep1 + '  ' + mortes_jogador[alea5()])
                morte()
        print('***Você se depara com uma ' + local_zero + ' e...')
        print('1- Seguir reto\n2- Voltar')
        dec2 = int(input('Digite 1 ou 2:\n '))
        if dec2 == 1:
            print('***Você segue em frente...')
            return nome
        if dec2 == 2:
            print('***Quando você se vira você esbarra em um ' + str(monstros[alea5()].raca) + ' que '
                  + mortes_jogador[alea5()] + '... deu nem tempo de reagir...')
            print(morte())
    elif int(dec0) == 2:
        print('-Seu desejo é uma ordem parceiro!\n'
              '***Quando você se dá conta ele ' + mortes_jogador[alea5()])
        morte()

def transicao1():
    print('***Você entra na ' + local_zero + ' e encontra quem aquele cara tinha falado '
                                          'e se da conta de q não perguntou o nome dele.')
    print('***Você decide dar um nome a ele, qual vai ser?')
    chefe = input('Nome do doido lá:\n ')
    print('-----COMEÇA SEGUNDA PARTE------')
    return chefe

def segunda_parte():
    drop = 0
    print('-Você ai! - Berra um velho acabado igual maracuja de gaveta\n'
          '-Onde você pensa que vai? essa é a minha ' + local_zero + '!')
    print('***Você encara o velho e decide se parte pra cima dele ou se conversa...')
    dec1 = int(input('1- Partir pra cima e arrebentar esse velho broxa\n'
                     '2- tentar acalmar o corno manso\n'))
    if dec1 == 1:
        luta = luta_dificil(drop)
        if luta == 1:
            print('***Voce matou um dos contrutores da Arca de Noé...')
            return False
        elif luta == 2:
            print(morte_especial())
        print('***Você avança como um raio pra cima do vovô, mas... ')
        print(morte_especial())
    if dec1 == 2:
        print('Você se apresenta como ' + nome +
              ' e conta que não lembra de nada e nem sabe como foi parar ali\n'
              'E conta que se encontrou com o ' + chefe + ' que disse que ele te ajudaria.')
        if nome == 'Prevtori':
            print('-Além de não fazer ideia de quem é ' + chefe + ' Que merda é essa?? Você tá brincando '
                                                                 'com a minha cara né?\n'
                  '-Ninguém tem o mesmo nome que eu... Seu Impostor!!!')
            resul = luta_dificil(drop)
            if resul == 1:
                print('***Voce matou um dos contrutores da Arca de Noé...')
                return False
            elif resul == 2:
                print(morte_especial())
            morte_especial()
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
                morte_especial()
        print('-Hmmmm... Pelo menos não é surdo... Mas como você '
              'invadiu minha ' + local_zero + ' ou você me faz um favor ou você vai tomar um reset')
        print('***Eai meu parceiro? vai deixar esse porra de Prevtori falar assim contigo???\n'
              '1- Tá maluco? esse velho tem cara de doido, melhor fazer oque ele quer...\n'
              '2- Eu não nasci um Corno pra levar desaforo pra casa, vou partir esse velho no meio\n')
        prevtori = int(input('Digite 1 ou 2:\n '))
        if prevtori == 1:
            print('Você fala calmamente: \n'
                  '-Éoque doido do caralho, para com essa porra ai, oque que tu quer que eu faça?')
            return True
        elif prevtori == 2:
            print('Bora vê então aki seu velho goiaba do caralho!!')
            resul = luta_dificil(drop)
            if resul == 1:
                print('***Voce matou um dos contrutores da Arca de Noé...')
                return False
            elif resul == 2:
                print(morte_especial())

def final_alt():
    new_nome1 = 'Pr' + nome[3:]
    new_nome2 = nome[:-3] + 'tori'
    nome_final ='Prev' + nome[2:-3] + 'tori'
    print('Prevtori está morto...')
    print('Agora sem saber pra que direção seguir nem oque fazer você está perdido...')
    print('Você vaga pela ' + local_zero + ' a procura de alguma pista ou algo útil')
    andadas = 0
    esquerda = 0
    while andadas <=5 and esquerda <=1:
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
        print('parece até um nome.... Prevtori.... e isso lá é um nome? e por falar nisso qual era o meu?')
        print('Você pensa e pensa.... qual era mesmo? ' + new_nome1 +'?.. ou era ' + nome + '?... quem sabe '
              + new_nome2 + '....')
        print('Quase certeza que era ' + nome_final + '... \n'
                                                      'Não... na verdade acho que era só Prevtori mesmo...')
        print('Após oque parecem decadas você vê um jovem correndo em sua direção e você berra: \n'
             '-Você ai!'
             '\n-Onde você pensa que vai? essa é a minha ' + local_zero + '!')

def missao(local_zero):
    drop = 0
    if local_zero == caminhos[0]:
 # Rua Deserta
        completo = False
        repetir_predio1 = False
        repetir_predio2 = False
        repetir_predio3 = False
        print('Você recebe a missão de Prevtori que te pede para procurar nos predios ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
        print('Você vê 3 prédios que batem com a descrição do Velho goiaba, um na esquerda e dois na direita.')
        print('Qual deles você quer entrar primeiro?')
        indecisao = 0
        while indecisao <= 4 and completo == False:
            dec0 = int(input(
                '1- Prédio da Esquerda\n2- Prédio da Direita perto\n3- Prédio da direita longe\nDigite 1, 2 ou 3:\n '))
            if dec0 == 1 and repetir_predio1 == True:
                print('Não há mais nada aqui que possa me interessar.')
            if dec0 == 2 and repetir_predio2 == True:
                print('***Você decide Voltar e Entregar o diário!***')
                completo = True
            if dec0 == 3 and repetir_predio3 == True:
                print('Não há mais nada aqui que possa me interessar.')
            if dec0 == 1 and repetir_predio1 == False:
                print(
                    'O prédio parece abandonado... apenas mobilia velha e empoeirada, '
                    'você entra em uma sala e vê um vulto num canto\n'
                    'Você quer se aproximar?\n'
                    '1- Sim, qualquer coisa eu mato ele na porrada oush\n'
                    '2- Não, tá maluco, doido, biluteteia??? imagina chegar até aki e '
                    'morrer de bobeira pra um Flamenguista??')
                comb0 = int(input('Digite 1 ou 2:\n '))
                if comb0 == 1:
                    print('Você se aproxima e percebe que é um ' + monstros[alea5()].raca + ' puto da cara!')
                    luta = luta_facil(drop)
                    if luta == 1:
                        print('Você vê o corpo dele sem vida e Pensa sozinho:\n'
                              'Como foi fácil acabar com ele... ainda mais com 3 chutes\n\n'
                              '*** Você encontra um... ' + armas[1].nome + '!!!, sua nova arma!!')
                        print('Você não vê mais nada de útil nesse prédio e volta para a rua...')
                        drop += 1
                        indecisao -= 1
                        repetir_predio1 = True
                    else:
                        morte()
                if comb0 == 2:
                    indecisao += 1
                    print('Você volta pra rua e tem que decidir pra onde vai...')
            elif dec0 == 2 and repetir_predio2 == False:
                print('Você anda pela direita e entra no primeiro prédio, dentro dele você encontra varias caixas.\n'
                      'A Velha gagá do Prevtori tinhe lhe falado dessas caixas!! o diario deve estar aqui!!\n'
                      'Você decide dar uma olhada nas caixas...')
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
                        break
                    elif chute != giro:
                        print('Você NÃO encontra nada e quando levanta os olhos vc sente que '
                              'alguém embaralhou as caixas novamente...\n'
                              'Você não tem todo o tempo do mundo...')
                        demora += 1
                if demora >= 11:
                    print('Você está tão concentrado em tentar achar um padrão que não nota um ' + monstros[alea5()].raca +
                          ' que chegou \n por trás e ' + mortes_jogador[alea5()])
                    morte()
                print('Você volta a Rua...')
                indecisao += 1
            elif dec0 == 3 and repetir_predio3 == False:
                print('Você anda sozinho em direção ao Prédio na esquina e se sente observado...\n'
                      'Você chega na sua porta e vê que ela está trancada...\n'
                      'Você quer:\n'
                      '1- Tentar arrombar a porta.\n'
                      '2- Voltar pra trás.')
                dec3 = int(input('Digite 1 ou 2:\n '))
                if dec3 == 1:
                    print('Você se prepara... Toma distância e corre com tudo contra a porta...')
                    print('Você escuta um CRACK\n\nA porta parece inteira e quando você olha pra baixo a última'
                          ' coisa que você nota antes de tudo ficar escuro\né o seu ombro fora do lugar')
                    print('\nQuando você acorda você vê um ' + monstros[alea5()].raca +
                          ' te olhando de cima\n quando você pensa em se levantar e correr ele já ' + mortes_jogador[alea5()])
                    morte()

                if dec3 == 2:
                    print('Você sente um frio na espinha e olha ao redor...\nTá maluco que eu vou ficar aki!'
                          '\nVocê volta num pique que deixaria o Usain comendo poeira!'
                          '\n Se eu voltar ali eu sou um corno! Tá maluco boy.')
                    indecisao += 2
        if indecisao >= 4:
            print('Você se sente perdido e quando se da conta você acorda morto')
            morte()
        elif completo == True:
            print('Você volta correndo pra devolver aquela merda pro velho broxa!!\n'
                  'mas Lembra que ele te pediu para não ler o diario... eai meu parceiro?\n'
                  'Vai escutar aquela quenga velha ou vai ser um pau no cu?\n'
                  '1- Amarelar igual uma bicha, escutar o Velho Corno e ficar na curiosidade\n'
                  '2- Ser um Pau no cu do Caralho e ler os segredos obscuros do Prev "Rola-murcha" tori?')
            diario = int(input('Digite 1 ou 2:\n '))
            if diario == 1:
                print('Você decide ser uma boa moça e seguir com a missão à risca! (com crase ein)')
                return 1
            elif diario == 2:
                print('-Aquele Velho baitola não manda nem na mulher dele vai mandar em mim?\n'
                      'Você descobre que o Velho era um cara que apareceu perdido aqui muito tempo atrás\n'
                      'e que com o tempo foi perdendo a memoria e do nada decidiu que iria se chamar Prevtori!!\n\n'
                      'Que parada zoada ein... quem inventou essa merda??')
                return 2
    if local_zero == caminhos[1]:
# Ponte
        print('Você recebe a missão de Prevtori que te pede para procurar nos Carros o seu velho diario...')
        print('Você entra na ' + local_zero)
        print('Você começa a caminhar entre os carros que parecem abandonados a décadas.'
              'Alguns deles te chamam a atenção! Qual deles você quer olhar primeiro?')
        completo = False
        carro1 = False
        carro2 = False
        carro3 = False
        carro4 = False
        carro5 = False
        while completo == False:
            car = int(input('1- Marea preto\n'
                            '2- Pegeout prata\n'
                            '3- Fusca Azul\n'
                            '4- Hilux Vermelha\n'
                            '5- Brasília Amarela\n:  '))

            if carro1 == True or carro2 == True or carro3 == True or carro4 == True or carro5 == True:
               print('Não tem mais o que ver ali.')
            if car == 1 and carro1 == False:
                print('Você se aproxima do Marea com cuidado, ele parece estranho e o risco de combustão espontanêa é real!')
                car1 = int(input('Você quer correr o risco?\n1- Sim, eu tô maluco biluteteia biruta da cabeça\n'
                             '2- não comi merda não meu parceiro, perto de um Marea eu só chego depois de morto!\n '))
                if car1 == 1:
                    print('Parece que você comeu merda meu amigo, vc se aproxima e escuta um barulho alto vindo '
                          'dele antes de vê a bola de fogo!\nVocê deu sorte, mais um passo pra frente e você tinha perdido mais'
                          ' do que só as sombrancelhas!')
                    carro1 = True
                if car1 == 2:
                    print('Você decide seguir a razão e recua, após o segundo passo você vê a bola de fogo!\n'
                          'o Marea explodiu como de costume e você agradece por esta a uma distancia segura!')
                    carro1 = True
            if car == 2 and carro2 == False:
                print('Você se aproxima do Pegeout e começa a sentir o perigo de adquirir um deles'
                      'Você agradece por não ter a sua carteira com você pra nem correr o risco.')
                print('Dentro dele você vê o que uma alma penada, talvez condenada a ficar aqui até vender o carro!')
                ajud = int(input('Você quer tentar ajudar a alma artomentada?\n1- Sim, ninguém merece um carro assim, '
                      'vamos tentar da a segunda alegria do dono de pegeout\n'
                      '2- Melhor não, se ele me empurra esse monstro eu vou ficar preso aqui também....\n '))
                if ajud == 1:
                    print('Você se aproxima e o Fantasma ja lhe pergunta se você tem interesse no Pegeout 206 prata, 2 portas,\n'
                          'tudo funcionando, só o ar q tá meio fraco, mas nada que uma janela aberta não resolva!\n'
                          'Você diz que quer dar uma olhada e ele te olha com os olhos marejados.\n- Obrigado ele diz e desaparece!'
                          'Ele só precisava que alguem com noção demonstrasse interesse no carro...\n'
                          'Essa foi fácil, apesar de arriscadíssimo!')
                    print('***Você encontrou uma' + armas[1].nome + ' em baixo de um dos Pneus***')
                    carro2 = True
                if ajud == 2:
                    print('Você é um homem sensato e não deixou que um fantasma que caiu na arapuca te puxasse junto!'
                          'você vai conseguir dormir em paz sabendo que não tem um pegeout na garagem.')
                    carro2 = True
            if car == 3 and carro3 == False:
                print('3')
            if car == 4 and carro4 == False:
                print('4')
            if car == 5 and carro5 == False:
                print('5')

    if local_zero == caminhos[2]:
# Caverna
        print('Você recebe a missão de Prevtori que te pede para procurar ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
    if local_zero == caminhos[3]:
# Viela Escura
        print('Você recebe a missão de Prevtori que te pede para procurar nos predios ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
    if local_zero == caminhos[4]:
# Mata Fechada
        print('Você recebe a missão de Prevtori que te pede para procurar nos arbustos ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
    if local_zero == caminhos[5]:
# Igreja
        print('Você recebe a missão de Prevtori que te pede para procurar ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)



local_zero = caminhos[1]
'''creep1 = monstros[alea5()].raca
creep2 = monstros[alea5()].raca
nome = tutorial()
chefe = transicao1()
prevtori = segunda_parte()
if prevtori == False:
    final_alt()
elif prevtori == True:
   print('Prevtori te da uma missão...\n'
         'TO BE CONTINUED')
r_missao = missao(local_zero)
if r_missao == 1:
    print('Você chega ao Prevtori e lhe entrega o diário!')
if r_missao == 2:
    print('Pelo seu olhar o Velho viado já sabe oque você fez\n'
          'Apesar dele parecer uma múmia ele não nasceu ontem!!'
          '\nQuando você abre a boca pra falar o Prevtori avança em sua direção!!')'''
missao(local_zero)

