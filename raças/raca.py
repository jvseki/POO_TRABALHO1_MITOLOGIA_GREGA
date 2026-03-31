class RacaBase:
    def __init__(self, nome, poder, defesa, vida_maxima, esquiva):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.esquiva = esquiva

    def aplicar(self, jogador):
        jogador.raca = self.nome
        jogador.poder += self.poder
        jogador.defesa += self.defesa
        jogador.vida_maxima += self.vida_maxima
        jogador.esquiva += self.esquiva
        jogador.vida_atual = jogador.vida_maxima

class Humano(RacaBase):
    def __init__(self):
        super().__init__("Humano", 1, 1, 5, 1)

class Semideus(RacaBase):
    def __init__(self):
        super().__init__("Semideus", 3, 2, 10, 0)

class Satiro(RacaBase):
    def __init__(self):
        super().__init__("Satiro", 0, 0, 2, 4)

class Centauro(RacaBase):
    def __init__(self):
        super().__init__("Centauro", 2, 1, 8, 1)

class Ninfa(RacaBase):
    def __init__(self):
        super().__init__("Ninfa", 0, 3, 5, 3)

def obter_raca(escolha):
    racas = {"1": Humano(), "2": Semideus(), "3": Satiro(), "4": Centauro(), "5": Ninfa()}
    return racas.get(escolha, Humano())