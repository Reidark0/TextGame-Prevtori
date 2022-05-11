import random
import time
from mob import Mobs, Arma, Armadura, Boss
from configs import monstros_easy, monstros_medium, monstros_hard, armas, armaduras, caminhos, mortes_jogador
from funcs import morte, morte_especial, alea5, luta, luta_femi, minijogo_1, minijogo_2, final_alt


boss = Boss(Mobs('Podi', 3, 3), Mobs('Babu', 4, 4), Mobs('Lucca', 5, 5), Mobs('Gil', 6, 6))
Prevtori = Mobs('Prevtori', 2, 10)
CavernaMan = Mobs('Criatura', 2, 20)
CavernaMan_Puto = Mobs('Criatura puta da cara', 4, 25)


arma_nivel = 0
armadura_nivel = 0
print(f'Seu equipamento inicial são {armaduras[armadura_nivel].nome} e '
      f'{armas[arma_nivel].nome} que dão bonus de {armaduras[armadura_nivel].vida} de vida '
      f'e {armas[arma_nivel].dano} de dano!')
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
print('-Tô de boas, mas acho que sei quem pode te ajudar, é um tal de Prevtori... Velho pra caralho... Diz o Homem'
      '\n- A proposíto... qual seu nome?')
nome = input('Qual seu nome?\n ')
if nome == 'Prevtori':
    print('- Ha Ha Ha...  Debocha o Homem. \n'
          '-Eu já ouvi esse nome antes... quero ver como você vai fazer depois')
else:
    print('-Aaah... que nome estranho... ' + nome + '...nunca ouvi falar')
print('-Então ' + nome + ' siga pela direita eu acho... ou era esquerda?... não! era a direita mesmo!')
time.sleep(2)
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
              f'Pelo menos você conseguiu pegar o jeans do {creep1.raca}!')
        time.sleep(1.5)
        print(f'***Você tem que voltar e continuar por outro caminho')
        armadura_nivel += 1
    elif confronto1 == 2:
        print(f'Infelizmente o {creep1.raca} tinha mais oque fazer e decidiu não te matar '
              f'por que você tá no tutorial ainda!\n')
        time.sleep(1.5)
        print(f'Você se levanta e tem que voltar pois não ha saidas além de outra surra...')
time.sleep(1)
print('***Você segue por um longo corredor iluminado por velhas lâmpadas, algumas queimadas...')
time.sleep(1.5)
print('***Você se depara com uma porta e precisa decidir....')
print('1- Seguir pra fora do prédio\n2- Voltar')
dec2 = input('Digite 1 ou 2:\n ')
if dec2 == '1':
    print('***Você segue pra fora e vê que está escurecendo\n'
          '***Você segue o único caminho de pedrinhas até avistar uma velha cabana...')
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
        print('***Você da uma de Jõao sem braço e atravessa a porta')
        time.sleep(1.5)
        print('***Você segue pra fora e vê que está escurecendo\n'
              '***Você segue o único caminho de pedrinhas até avistar uma velha cabana...')
        time.sleep(1.5)
print('***Você entra na cabana e encontra um velho aquele cara tinha falado '
      'e se da conta de q não perguntou o nome dele.')
time.sleep(1.5)
print('***Você decide dar um nome a ele, qual vai ser?')
chefe = input('Nome do doido lá:\n ')
time.sleep(1.5)

# Segunda parte --------------------------------------------------------------------------------------------------------

print('-----SEGUNDA PARTE------')
time.sleep(1.5)
print('-Você ai! - Berra um velho acabado igual maracuja de gaveta\n'
      '-Onde você pensa que vai? essa é a minha cabana!')
time.sleep(1.5)
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
    time.sleep(1.5)
    print('-O meu Nome é Prevtori, mas pode me chamar de Prevtori')
    time.sleep(1.5)
    esp = input('Tá me entendendo?\n'
                'qual é o meu nome?\n ')
    tentativas = 0
    while esp != 'Prevtori':
        esp = input('Escreve direito Viado!!:\n')
        time.sleep(1)
        tentativas += 1
        if tentativas == 3:
            print('- Não tenho tempo pra isso não... Tá fudido na minha mão parceiro!')
            luta_prev = luta(Prevtori, armas[arma_nivel], armaduras[armadura_nivel])
            if luta_prev == 1:
                print('***Voce matou um dos contrutores da Arca de Noé...')
                velho_vivo = False
                final_alt()
                break
            elif luta_prev == 2:
                print(morte_especial())
    print('- Hmmmm... Pelo menos não é surdo... Mas como você '
          'invadiu minha cabana ou você me faz um favor ou você vai tomar um reset')
    time.sleep(1.5)
    print('***Eai meu parceiro? vai deixar esse porra de Prevtori falar assim contigo???')
    time.sleep(1.5)
    print('1 - Tá maluco? esse velho tem cara de doido, melhor fazer oque ele quer...\n'
          '2 - Eu não nasci um Corno pra levar desaforo pra casa, vou partir esse velho baitola no meio\n')
    dec4 = input('Digite 1 ou 2:\n ')
    if dec4 == '1':
        print('***Você fala calmamente: \n'
              '- Éoque doido do caralho, para com essa porra ai, oque que tu quer que eu faça?')
        time.sleep(1.5)
    elif dec4 == '2':
        print('Bora vê então aki seu velho goiaba do caralho!!')
        time.sleep(1.5)
        luta_prev = luta(Prevtori, armas[arma_nivel], armaduras[armadura_nivel])
        if luta_prev == 1:
            print('***Voce matou um dos contrutores da Arca de Noé...')
            velho_vivo = False
            final_alt()
            break
        elif luta_prev == 2:
            print(morte_especial())
    print('***Prevtor te diz que você precisa produrar seu diário em uns prédios abandonados ali perto\n'
          'e aconteça oque acontecer não olhe dentro dele!')

# Terceira parte -------------------------------------------------------------------------------------------------------
    time.sleep(1)
    print('-----TERCEIRA PARTE------')
    time.sleep(2)
# Rua Deserta
    completo = False
    repetir_predio1 = False
    repetir_predio2 = False
    repetir_predio3 = False
    print('***Você segue andando pelo caminho indicado e encontra a rua que o Velhiado te indicou...')
    time.sleep(1.5)
    print('***Você entra numa Rua Deserta')
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
                  '2- Não, tá maluco,doido, biluteteia??? imagina chegar até '
                  'aki e morrer de bobeira pra um Flamenguista??')
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
                if confronto3 == 1:
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
            time.sleep(1)
            print('O Velho fresco vê o seu valor e decide frescar com você!\n'
                  'Ele diz que vai te contar aonde é a saída, mas você vai ter que fazer um favor pra ele...')
            time.sleep(1.5)
            print('-Você parece ser tão... Forte...- diz o Velho não tão broxa ao se aproximar...\n'
                  '-Eu só quero ver o quão forte você realmente é... e eu te conto tudo! <3')
            time.sleep(2)
            print('Que porra é essa??\n'
                  '1 - Esse velho viado tá ficando demente... melhor tirar ele dessa miséria slk\n'
                  '2 - Caralho... mas tudo bem, oque é o pior que pode acontecer? ele não encostando tá safe!')
            prev_final = input('Digite 1 ou 2\n')
            if prev_final == '2':
                print('Você começa se despir e o velho começa a falar de uma ponte\n')
                time.sleep(1.5)
                print('Quando você termina de tirar a roupa o velho avança pega a sua roupa e desaparece!\n'
                      'Você consegiu descobrir o próximo passo, mas agora está sem armadura :(\n'
                      'VELHO FILHA DA PUTA!')
                time.sleep(2)
                print('Você segue o caminho que aquele corno do caralho falou e encontra uma ponte.')
                armadura_nivel = 0
            if prev_final == '1':
                luta_prev = luta(Prevtori, armas[arma_nivel], armaduras[armadura_nivel])
                if luta_prev == 1:
                    print('***Voce matou um dos contrutores da Arca de Noé...')
                    velho_vivo = False
                    final_alt()
                    break
                elif luta_prev == 2:
                    print(morte_especial())
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
    print('Você consegue ler algumas coisas no caderno que falam sobre uma ponte que leva até uma caverna...')
    time.sleep(1.5)
    arma_nivel += 1
    armadura_nivel += 1
    print(f'***E você encontrou {armas[arma_nivel].nome} e {armaduras[armadura_nivel].nome}!\n'
          f'Valeu a pena passar o Velho! ')
    time.sleep(1.5)
    print('Bom, hora de ir! É melhor do que ficar aqui parado e virar um velho louco!\n'
          ' Você segue as intruções no caderno e encontra um atalho para a ponte')
    time.sleep(1.5)
    
# Quarta parte ---------------------------------------------------------------------------------------------------------

print('-----QUARTA PARTE------')
time.sleep(2)
# Ponte
print('Você entra na Ponte')
time.sleep(1.5)
print('Você começa a caminhar entre os carros que parecem abandonados a décadas.'
      'Alguns deles te chamam a atenção.. Qual deles você quer olhar primeiro?')
time.sleep(2)
carro1 = False
carro2 = False
carro3 = False
carro4 = False
carro5 = False
completo1 = False
while completo1 is False:
    car = input('1- Marea preto\n'
                '2- Pegeout prata\n'
                '3- Fusca Azul\n'
                '4- Camaro Vermelha\n'
                '5- Brasília Amarela\n  ')
    if car == '4' and carro4 is True:
        print('Você decide dar mais uma olhada no camaro e nota uma multidão se aproximando!')
        time.sleep(1.5)
        print('Você se desespera e procura uma saída urgentemente!')
        time.sleep(2)
        print('alguma coisa perto do volante lhe chama atenção! é a chave ma maquina!')
        time.sleep(1.5)
        print('Nao há tempo para decisões! voc~e só acelera e deixa aquele bando pra trás...')
        time.sleep(3)
        print('Mas qm era eles?')
        completo1 = True
        break
    elif car == '1' and carro1 is True:
        print('Não tem mais o que ver ali além de um marea sendo um marea.')
        time.sleep(1.5)
    elif car == '2' and carro2 is True:
        print('Não tem mais o que ver ali, vai que você realmente adquire um pegeout?')
        time.sleep(1.5)
    elif car == '3' and carro3 is True:
        print('Não tem mais o que ver ali, o Fusca Azul gera agressão involuntaria')
        time.sleep(1.5)
    elif car == '5' and carro5 is True:
        print('Não tem mais o que ver ali.')
        time.sleep(1.5)
    if car == '1' and carro1 is False:
        print('Você se aproxima do Marea com cuidado, ele parece estranho e o risco '
              'de combustão espontanêa é real!')
        time.sleep(1.5)
        print('Você quer correr o risco?\n1 - Sim, eu tô maluco biluteteia biruta da cabeça\n'
              '2 - não comi merda não meu parceiro, perto de um Marea eu só chego depois de morto!')
        car1 = input('Digite 1 ou 2\n')
        if car1 == '1':
            print('Parece que você comeu merda meu amigo, vc se aproxima e escuta um barulho alto vindo '
                  'dele antes de vê a bola de fogo!')
            time.sleep(1.5)
            print('Você deu sorte, mais um passo pra frente e você tinha perdido mais do que só as sombrancelhas!')
            carro1 = True
            time.sleep(1.5)
        if car1 == '2':
            print('Você decide seguir a razão e recua, após o segundo passo você vê a bola de fogo!')
            time.sleep(1.5)
            print('o Marea explodiu como de costume e você agradece por esta a uma distancia segura!')
            carro1 = True
            time.sleep(1.5)
    if car == '2' and carro2 is False:
        print('Você se aproxima do Pegeout e começa a sentir o perigo de adquirir um deles\n'
              'Você agradece por não ter a sua carteira com você pra nem correr o risco de comprar.')
        time.sleep(1.5)
        print('Dentro dele você vê o que uma alma penada, talvez condenada a ficar aqui até vender o carro!')
        time.sleep(1.5)
        print('Você quer tentar ajudar a alma artomentada?\n1- Sim, ninguém merece um carro assim, '
              'vamos tentar da a segunda alegria do dono de pegeout\n'
              '2- Melhor não, se ele me empurra esse monstro eu vou ficar preso aqui também....\n ')
        ajud = input('Digite 1 ou 2\n')
        if ajud == '1':
            print('Você se aproxima e o Fantasma ja lhe pergunta se '
                  'você tem interesse no Pegeout 206 prata, 2 portas,\n'
                  'tudo funcionando, só o ar q tá meio fraco, mas nada que uma janela aberta não resolva!')
            time.sleep(3)
            print('Você diz que quer dar uma olhada e ele te olha com os olhos marejados.\n- Obrigado... '
                  'Você é um Héroi! - ele diz e desaparece!\n')
            time.sleep(3)
            print('Ele só precisava que alguem com noção demonstrasse interesse no carro...\n'
                  'Essa foi fácil, apesar de arriscadíssimo!')
            time.sleep(2)
            arma_nivel += 1
            print(f'***Você encontrou uma {armas[arma_nivel].nome} em baixo de um dos Pneus, que Sorte')
            carro2 = True
            time.sleep(1.5)
        if ajud == '2':
            print('Você é um homem sensato e não deixou que um fantasma que caiu na arapuca te puxasse junto!\n'
                  'Você vai conseguir dormir em paz sabendo que não tem um pegeout na garagem.')
            time.sleep(1.5)
    if car == '3' and carro3 is False:
        creep4 = monstros_easy[alea5()]
        print('Você se aproxima do fusca azul e um ' + creep4.raca +
              ' Aparece do nada e vem te agredir gritando "Fusca Azul!", '
              'você não tem alternativa além de se defender!')
        time.sleep(2)
        car3 = luta(creep4, armas[arma_nivel], armaduras[armadura_nivel])
        carro3 = True
        if car3 == 1:
            print('Você acabou com a raça daquele corno infantil!, mas não encontra \n'
                  'nada além de um belo fusca azul!')
            time.sleep(1.5)
            carro3 = True
        if car3 == 2:
            print('Ele acerta o seu braço com uma força jamais vista...')
            morte()
    if car == '4' and carro4 is False:
        print('Você se aproxima do Camaro e pensa quem era o Playboy q dirigia ese Bumblebee vermelho...')
        time.sleep(1.5)
        print('ao olhar no banco de trás você encontra uma caixa, mas a porta está trancada!\n'
              'Você precisa de alguma coisa para quebrar o vidro! ')
        time.sleep(1.5)
        if arma_nivel >= 1:
            print(f'***Você usa sua {armas[arma_nivel].nome} para arrebentar o vidro sem enrolação e recupera...')
            time.sleep(1.5)
            print('Um amuleto? oque será que ele faz?')
            time.sleep(2)
            print('<> Para prosseguir vá novamente ao camaro! <>')
            
            carro4 = True
        else:
            print('***Você tem que procurar em outros lugares!***')
            time.sleep(1.5)
    if car == '5' and carro5 is False:
        print('Você se aproxima da Brasília amarela e observa que suas portas estão abertas!\n')
        time.sleep(1.5)
        guerreiro2 = monstros_medium[alea5()]
        print('1 - Entrar nela?\n'
              '2 - Não entendi, flws bença')
        dec6 = input('Digite 1 ou 2\n')
        if dec6 == '1':
            print(f'Apesar de querer os mamonas a única coisa que você encontra é um {guerreiro2.raca}!')
            time.sleep(1.5)
            confronto_med2 = (guerreiro2, arma_nivel, armadura_nivel)
            if confronto_med2 == 2:
                morte()
            else:
                print(f'Você acabou com o {guerreiro2.raca} e encontrou uma armadura!!')
                armadura_nivel += 1
                print(f'Sua armadura agora é uma {armaduras[armadura_nivel].nome}!')
                time.sleep(1.5)
                carro5 = True
        if dec6 == '2':
            print(f'Quando você se vira você nota o {guerreiro2.raca} dentro da van...')
            time.sleep(1)
print("Você acelera pela ponte desviando dos carros abandonados e nem percebe que ela acabou em um buraco!")
time.sleep(3)

# Quinta parte ---------------------------------------------------------------------------------------------------------

print('-----QUINTA PARTE------')

# Caverna
print('Você acorda em uma Caverna e não sabe nem pra que lado tá o teto...')
time.sleep(1.5)
print('Você se rasteja para fora do carro e não tem ideia de onder ir')
time.sleep(1.5)
print('Suas opções são limitadas! o máximo que você pode fazer é sair tateando!\n'
      'para que lado você quer tatear?\n'
      '1- Esquerda\n2- Direita\n3- Frente')

input('Digite 1, 2 ou 3:\n ')
print('Zoas fiquei cansado e agora é tudo sorte! XD\nAdivinhe um número de 1 a 15!')
saida = random.randint(1, 15)
acerto = False
desculpa = False
caverna = False
tempo = 0
while caverna is False:
    while desculpa is False:
        chute = int(input('Qual seu chute de 1  a 15?\n  '))
        if chute == saida:
            desculpa = True
        elif chute < 7:
            print('Não consigo ver nada, mas parece ser um beco sem saída.')
            time.sleep(1)
            tempo += 1
        elif chute >= 7:
            print('Droga... não pode ser por aqui... apenas pedras.')
            time.sleep(1)
            tempo += 1
        if tempo == 3:
            print('Droga... eu não sei se escutei alguma coisa ou se foi algo da minha cabeça...')
            time.sleep(1)
        if tempo == 5:
            print('Eu tenho certeza que ouvi alguma coisa!! que merda é essa?')
            time.sleep(1)
        if tempo == 7:
            print('PORRRA! esse bicho tá do meu lado... eu posso sentir o seu cheiro Podre!')
            time.sleep(1)
        if tempo == 8:
            print('Uma criatura te ataca e te derruba no chão, apesar do breu você precisa se defender!')
            time.sleep(1)
            resu = luta_femi(CavernaMan, armas[arma_nivel], armaduras[armadura_nivel])
            if resu == 1:
                print('Você consegue se desvencilhar e correr!\n'
                      'Ainda está perdido, pelo menos consegue um pouco mais de tempo!')
                tempo -= 5
            elif resu == 2:
                print('A Criatura finca seus dentes na sua garganta...')
                print(morte())
    print('***Você consegue ver uma luz!!!\n')
    time.sleep(2)
    print('A saída está próxima, mas a Criatura se aproxima\n'
          '1- Derrotar a Criatura e sair sem pressa\n'
          '2- Fugir e tentar a sorte na corrida!')
    time.sleep(1)
    lut = int(input('Digite 1 ou 2:\n '))
    if lut == 1:
        luta = luta_femi(CavernaMan_Puto, armas[arma_nivel], armaduras[armadura_nivel])
        if luta == 1:
            print('Você consegue vencer a criatura que agora você examina e...')
            time.sleep(2)
            print('E vê que é uma capivara enorme... bem, antes ela do que eu!')
            time.sleep(2)
            print(f'Você que ela é estilosa e decide surrupiar a {armaduras[armadura_nivel].nome} '
                  f'que ela está vestindo!')
            armadura_nivel += 1
            time.sleep(2)
            print('Você vaga pela caverna sem pressa até encontrar a luz que vem de sua entrada.')
            acerto = True
        if luta == 2:
            print('A Criatura é mais forte do que você imaginava... Você é obrigado a fugir!')
            lut = 2
    if lut == 2:
        print('Você está correndo no escuro... 50% de chance de dar merda.')
        bola = random.randint(1, 2)
        chut = int(input('Chute 1 ou 2:\n '))
        if chut == bola:
            print('Parabéns! você corre no breu aos tropeços até que comeca a ver a luz da entrada da caverna!')
            time.sleep(2)
            print('Ainda bem que está de dia!! apesar de você não saber se ainda é do mesmo dia...')
            caverna = True
        else:
            print('Você corre para uma beco sem saída... pelo menos você não '
                  'consegue ver oque vai acontecer com você...'
                  '\nA ultima coisa que você sente é o Bafo da criatura na sua nuca')
            print(morte())

print('***Você está fora da caverna!')
print('To be continue')


def missao(local_zero):
    drop = 0

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
# Caminhos 4 e 5
# Final alternativo voltar para o final verdadeiro
# Final verdadeiro
# Quantas missões antes do Final verdadeiro?
# Prevtori ajuda você na batalha final?
