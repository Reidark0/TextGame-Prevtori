#lugares
import random
caminhos = [
'Rua deserta',
'Ponte',
'Caverna',
'Viela escura',
'Mata fechada',
'Igreja'        ]
'''
armas diminuem o numero da luta


local rua deserta
entra na rua - corredor - predios do lado (entrar neles?)
final da rua encontra o objetivo, q é o nome original?

local ponte
entra na ponte, só pode seguir reto, carros abandonados
cair da ponte = morte?

local caverna
uma entrada , tudo muito escuro, tatear até esbarrar em um baú
e dificuldade de achar a saída e sair em algum lugar diferente?

viela escura
lutar contra algum bicho e tirar informação dele

mata fechada
explora ela até achar a caverna

local igreja
vai fuçar dentro da igreja e encontra documentos que talvez 
fale quem é o Prevtori

print('Após oque parecem decadas você vê um jovem correndo em sua direção e você berra: \n'
          '-Você ai!'
          '\n-Onde você pensa que vai? essa é a minha ' + local_zero + '!'')'

local_zero = caminhos[random.randint(0, 5)]
if local_zero == caminhos[0]:
    print('Você recebe a missão de Prevtori que te pede para procurar nos predios ao redor o seu velho diario...')
    print('Você vê 3 prédios que batem com a descrição do Velho goiaba, um na esquerda e dois na direita.')
    print('Qual deles você quer entrar primeiro?')
    indecisao = 0
    while indecisao <=4:
        dec0 = int(input('1- Prédio da Esquerda\n2- Prédio da Direita perto\n3- Prédio da direita longe\nDigite 1, 2 ou 3:\n '))
        if dec0 == 1:
                print('O prédio parece abandonado... apenas mobilia velha e empoeirada, você entra em uma sala e vê um vulto num canto\n'
                      'Você quer se aproximar?\n'
                      '1- Sim, qualquer coisa eu mato ele na porrada oush\n'
                      '2- Não, tá maluco, doido, biluteteia??? imagina chegar até aki e morrer de bobeira pra um Flamenguista??')
                comb0 = int(input('Digite 1 ou 2:\n '))
                if comb0 == 1:

                if comb0 == 2:
                    indecisao += 1
                    print('Você volta pra rua e tem que decidir pra onde vai...')
        elif dec0 == 2:

        elif dec0 ==3:
    if indecisao >=4:
        print('Você se sente perdido e quando se da conta você acorda morto')
#  Rua deserta

if local_zero == caminhos[1]:
    print(caminhos[1])
#   Ponte
if local_zero == caminhos[2]:
    print(caminhos[2])
#   Caverna
if local_zero == caminhos[3]:
    print(caminhos[3])
#   Viela Escura
if local_zero == caminhos[4]:
    print(caminhos[4])
#   Mata Fechada
if local_zero == caminhos[5]:
    print(caminhos[5])
#   Igreja
'''

def ex(lix):
    lix = lix +3
    return lix

print('Hello World!')
print('')
print('Queijo')
