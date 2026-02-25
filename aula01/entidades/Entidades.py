import random

class Entidade:
    def __init__(self, nome, poder, defesa, vida_maxima, vida_atual, esquiva):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_atual
        self.esquiva = esquiva

    def esta_vivo(self):
        return self.vida_atual > 0

    def atacar(self, alvo):
        if not self.esta_vivo():
            print(f"{self.nome} está derrotado e não pode atacar.")
            return

        # esquiva
        if random.randint(1, 100) <= alvo.esquiva:
            print(f"{alvo.nome} desviou do ataque!")
            return

        # crítico 10%
        critico = random.randint(1, 100) <= 10
        dano = self.poder * 2 if critico else self.poder

        print(f"{self.nome} atacou {alvo.nome}!")
        if critico:
            print("💥 ATAQUE CRÍTICO!")

        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        dano_real = max(0, dano - self.defesa)
        self.vida_atual -= dano_real

        if self.vida_atual < 0:
            self.vida_atual = 0

        print(f"{self.nome} recebeu {dano_real} de dano.")
        print(f"Vida: {self.vida_atual}/{self.vida_maxima}")

        if not self.esta_vivo():
            print(f"{self.nome} caiu em batalha!")