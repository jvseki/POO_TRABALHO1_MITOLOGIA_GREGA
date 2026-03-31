from entidades.Entidades import Entidade
from Sistema.level import calculo_nivel, upando_status

class Jogador(Entidade):
    def __init__(self, nome):
        super().__init__(nome, 5, 5, 20, 2)
        self.raca = ""
        self.vocacao = ""
        self.xp = 0
        self.nivel = 1
        self.xp_proximo_nivel = calculo_nivel(self.nivel)

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        self.verificar_level_up()

    def verificar_level_up(self):
        xp_necessario = calculo_nivel(self.nivel)
        while self.xp >= xp_necessario:
            self.xp -= xp_necessario
            self.subir_de_nivel()
            xp_necessario = calculo_nivel(self.nivel)

    def subir_de_nivel(self):
        self.nivel += 1
        upando_status(self)

    def curar(self, valor):
        self.vida_atual += valor
        if self.vida_atual > self.vida_maxima:
            self.vida_atual = self.vida_maxima