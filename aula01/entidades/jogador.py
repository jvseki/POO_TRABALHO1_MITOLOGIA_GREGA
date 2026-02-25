from entidades.Entidades import Entidade

class Jogador(Entidade):
    def __init__(
        self,
        nome,
        poder=10,
        defesa=5,
        vida_maxima=100,
        vida_atual=100,
        esquiva=10,
        nivel=1,
        xp=0
    ):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.nivel = nivel
        self.xp = xp

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"{self.nome} ganhou {quantidade} XP!")

        if self.xp >= 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.xp = 0
        self.poder += 5
        self.defesa += 3
        self.vida_maxima += 20
        self.vida_atual = self.vida_maxima

        print(f"⭐ {self.nome} subiu para o nível {self.nivel}!")