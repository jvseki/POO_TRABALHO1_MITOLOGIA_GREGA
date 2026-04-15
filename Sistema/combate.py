import time
from sistema.dados import rolar_d20

def combate(jogador, inimigo):
    print(f"\n Combate iniciando contra {inimigo.nome}!\n")

    while jogador.esta_vivo() and inimigo.esta_vivo():

        print(f"\nTurno de {jogador.nome}...")

        input("\nPressione Enter para atacar...")

        dado_jogador = rolar_d20()
        dado_inimigo = rolar_d20()

        print(f"\n {jogador.nome} rolou: {dado_jogador}")
        print(f"{inimigo.nome} rolou: {dado_inimigo}") 

        if dado_jogador > dado_inimigo:
            dano = jogador.poder
            inimigo.receber_dano(dano)
            print(f"Você acertou o ataque e causou {dano} de dano!")
        else:
            print(f"{inimigo.nome} esquivou do seu ataque!")
        
        print(f"A vida do {inimigo.nome} é {inimigo.vida_atual}/{inimigo.vida_maxima}")

        if not inimigo.esta_vivo():
            print(f"\nVocê derrotou {inimigo.nome}!")
            jogador.ganhar_xp(inimigo.xp_drop)
            break

        time.sleep(1)

        print(f"\nTurno do {inimigo.nome}...")

        dado_inimigo = rolar_d20()
        dado_jogador = rolar_d20()

        print(f"\n {inimigo.nome} rolou: {dado_inimigo}")
        print(f"{jogador.nome} rolou: {dado_jogador}")

        if dado_inimigo > dado_jogador:
            dano = inimigo.poder
            jogador.receber_dano(dano)
            print(f"{inimigo.nome} acertou o ataque e causou {dano} de dano!")
        else:
            print(f"Você esquivou do ataque de {inimigo.nome}!")

        print(f"A vida do {jogador.nome} é {jogador.vida_atual}/{jogador.vida_maxima}")

        if not jogador.esta_vivo():
            print(f"\nVocê foi derrotado por {inimigo.nome}...")
            break

        time.sleep(1)