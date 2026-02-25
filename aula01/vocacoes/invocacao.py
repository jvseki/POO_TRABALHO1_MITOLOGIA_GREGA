from entidades.Entidades import Entidade

class Invocacao(Entidade):
    def __init__(self, nome, poder, defesa, vida_maxima, vida_atual, esquiva, deus_origem):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.deus_origem = deus_origem

    def habilidade_divina(self, alvo):
        print(f"{self.nome} invoca o poder de {self.deus_origem}!")
        alvo.receber_dano(self.poder + 5)