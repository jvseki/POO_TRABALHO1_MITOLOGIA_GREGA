class Deus:
    def __init__(self, nome, bonus_poder):
        self.nome = nome
        self.bonus_poder = bonus_poder

    def abencoar(self, jogador):
        jogador.poder += self.bonus_poder
        print(f"{self.nome} abençoou {jogador.nome}!")

zeus = Deus("Zeus", 10)
hades = Deus("Hades", 8)
poseidon = Deus("Poseidon", 7)