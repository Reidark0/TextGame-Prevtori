class Mobs:
    def __init__(self, raca, dano, vida):
        self.raca = raca
        self.dano = dano
        self.vida = vida


class Boss:
    def __init__(self, forma1, forma2, forma3, forma4):
        self.forma1 = forma1
        self.forma2 = forma2
        self.forma3 = forma3
        self.forma4 = forma4


class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano


class Armadura:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

