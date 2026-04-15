from random import randint
from entidades.entidades import Entidade

class Inimigo(Entidade):
    def __init__(self, nome, poder, defesa, vida_maxima, esquiva, xp_drop):
        super().__init__(nome, poder, defesa, vida_maxima, esquiva)
        self.xp_drop = xp_drop

def gerar_inimigo_fraco():
    inimigos = [
        Inimigo("Harpia", 4, 2, 12, 4, 15),
        Inimigo("Esqueleto Espartano", 5, 4, 15, 1, 20),
        Inimigo("Javali de Erimanto", 6, 3, 18, 0, 25),
        Inimigo("Aranha Gigante", 3, 5, 20, 2, 20),
        Inimigo("Soldado Corrompido", 4, 3, 14, 3, 15)
    ]
    indice = randint(0, 4)
    return inimigos[indice]