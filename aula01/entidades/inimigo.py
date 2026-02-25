from entidades.Entidades import Entidade

class Inimigo(Entidade):
    def __init__(self, nome, poder, defesa, vida_maxima, vida_atual, esquiva, tipo):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.tipo = tipo