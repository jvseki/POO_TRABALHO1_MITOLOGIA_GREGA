class VocacaoBase:
    def __init__(self, nome, poder, defesa, vida_maxima, esquiva):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.esquiva = esquiva

    def aplicar(self, jogador):
        jogador.vocacao = self.nome
        jogador.poder += self.poder
        jogador.defesa += self.defesa
        jogador.vida_maxima += self.vida_maxima
        jogador.esquiva += self.esquiva
        jogador.vida_atual = jogador.vida_maxima

class Hoplita(VocacaoBase):
    def __init__(self):
        super().__init__("Hoplita", 2, 4, 10, 0)

class Arqueiro(VocacaoBase):
    def __init__(self):
        super().__init__("Arqueiro", 4, 0, 5, 3)

class Oraculo(VocacaoBase):
    def __init__(self):
        super().__init__("Oraculo", 5, -1, 2, 2)

class Assassino(VocacaoBase):
    def __init__(self):
        super().__init__("Assassino", 6, -2, 0, 4)

class Gladiador(VocacaoBase):
    def __init__(self):
        super().__init__("Gladiador", 3, 2, 8, 1)

def obter_vocacao(escolha):
    vocacoes = {"1": Hoplita(), "2": Arqueiro(), "3": Oraculo(), "4": Assassino(), "5": Gladiador()}
    return vocacoes.get(escolha, Hoplita())