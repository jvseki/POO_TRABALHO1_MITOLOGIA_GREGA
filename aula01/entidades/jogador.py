from Entidades import Entidade

class Jogador(Entidade):
    def __init__(self, nome:str, poder:int, defesa:int, vida_maxima:int, vida_atual, esquiva:int, nivel:int, xp:int):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.nivel = nivel
        self.xp = xp

player=Jogador("Lukinha", 10, 5, 100, 100, 20, 1, 0)

print(f"Nome do jogador: {player.nome}")
print(f"Poder: {player.poder}")
print(f"Defesa: {player.defesa}")
print(f"Vida: {player.vida_atual} / {player.vida_maxima}")
print(f"Esquiva: {player.esquiva}%")
print(f"Nível: {player.nivel}")
print(f"XP: {player.xp}")

