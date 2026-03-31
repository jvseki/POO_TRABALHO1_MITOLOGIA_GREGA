class Entidade:
    def __init__(self, nome, poder, defesa, vida_maxima, esquiva):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.esquiva = esquiva

    def receber_dano(self, dano):
        self.vida_atual = self.vida_atual - dano
        self.vida_atual = max(0, self.vida_atual)

    def esta_vivo(self):
        return self.vida_atual > 0