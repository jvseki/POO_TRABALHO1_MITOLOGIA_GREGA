from Entidades import Entidade

class Inimigo(Entidade):
    def __init__ (self, nome:str, poder:int, defesa:int, vida_maxima:int, vida_atual, esquiva:int, tipo:str):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.tipo = tipo

Ing1=Inimigo("Servo", 8, 3, 50, 50, 10, "Ninfas")
print(f"Nome do inimigo: {Ing1.nome}")
print(f"Poder: {Ing1.poder}")
print(f"Defesa: {Ing1.defesa}")
print(f"Vida: {Ing1.vida_atual} / {Ing1.vida_maxima}")
print(f"Esquiva: {Ing1.esquiva}%")
print(f"Tipo: {Ing1.tipo}")