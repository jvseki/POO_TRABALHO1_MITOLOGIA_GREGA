class Entidade:
    def __init__(self, nome:str, poder:int, defesa:int, vida_maxima:int, vida_atual, esquiva:int):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_atual
        self.esquiva = esquiva

    def esta_vivo(self):
        return self.vida_atual > 0
    
    def receber_dano(self, dano:int):
        dano_real = max(0, dano - self.defesa)
        self.vida_atual -= dano_real
        if self.vida_atual < 0:
            self.vida_atual = 0
        print(f"vida atual {self.vida_atual} / {self.vida_maxima}")

        if not self.esta_vivo():
            print(f"{self.nome} foi derrotado!")
    
    def curar(self, valor:int):
        if not self.esta_vivo():
            print(f"{self.nome} não pode ser curado, pois está derrotado.")
            return
        self.vida_atual += valor
        if self.vida_atual > self.vida_maxima:
            self.vida_atual = self.vida_maxima
        print(f"{self.nome} foi curado em {valor} pontos de vida.")
        print(f"vida atual {self.vida_atual} / {self.vida_maxima}")

        

   