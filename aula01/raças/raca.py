class Raca:
    def __init__(self, nome, bonus_poder=0, bonus_defesa=0, bonus_vida=0, bonus_esquiva=0):
        self.nome = nome
        self.bonus_poder = bonus_poder
        self.bonus_defesa = bonus_defesa
        self.bonus_vida = bonus_vida
        self.bonus_esquiva = bonus_esquiva

    def aplicar_bonus(self, jogador):
        jogador.poder += self.bonus_poder
        jogador.defesa += self.bonus_defesa
        jogador.vida_maxima += self.bonus_vida
        jogador.vida_atual += self.bonus_vida
        jogador.esquiva += self.bonus_esquiva

        print(f"\n🏛 Raça escolhida: {self.nome}")

humano = Raca("Humano", bonus_defesa=2)
semideus = Raca("Semideus", bonus_poder=5, bonus_vida=20)
filho_de_ares = Raca("Filho de Ares", bonus_poder=8)
filho_de_athena = Raca("Filho de Athena", bonus_defesa=5, bonus_esquiva=5)