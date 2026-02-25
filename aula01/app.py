from entidades.jogador import Jogador
from entidades.inimigo import Inimigo
from raças.raca import semideus
from deuses.deus import zeus
from vocacoes.invocacao import Invocacao

if __name__ == "__main__":

    player = Jogador("Tabeli")

    semideus.aplicar_bonus(player)
    zeus.abencoar(player)

    minotauro = Inimigo("Minotauro", 20, 8, 150, 150, 5, "Monstro")

    ciclope = Invocacao("Ciclope", 18, 6, 80, 80, 10, "Poseidon")

    print("\n⚔️ BATALHA COMEÇA ⚔️\n")

    player.atacar(minotauro)
    minotauro.atacar(player)
    ciclope.habilidade_divina(minotauro)

    if not minotauro.esta_vivo():
        player.ganhar_xp(100)