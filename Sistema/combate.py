from Sistema.dados import jogar_d20, jogar_d6

def combate(jogador, inimigo):
    print(f"\nCombate: {jogador.nome} vs {inimigo.nome}")
    
    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"\n{jogador.nome}: Vida {jogador.vida_atual}/{jogador.vida_maxima}")
        print(f"{inimigo.nome}: Vida {inimigo.vida_atual}/{inimigo.vida_maxima}")
        print("1. Atacar")
        print("2. Fugir")
        acao = input("Escolha: ")
        dado20 = jogar_d20()
        dado6 = jogar_d6()

        if acao == "1":
            ataque_jogador = dado20 + jogador.poder
            defesa_inimigo = inimigo.defesa + 10
            
            if ataque_jogador >= defesa_inimigo:
                dano = dado6 + jogador.poder - inimigo.defesa
                dano = max(1, dano)
                inimigo.receber_dano(dano)
                print(f"Voce acertou e causou {dano} de dano!")
            else:
                print("Voce errou o ataque!")

            if inimigo.esta_vivo():
                ataque_inimigo = dado20 + inimigo.poder
                defesa_jogador = jogador.defesa + 10
                
                if ataque_inimigo >= defesa_jogador:
                    dano_ini = dado6 + inimigo.poder - jogador.defesa
                    dano_ini = max(1, dano_ini)
                    jogador.receber_dano(dano_ini)
                    print(f"O {inimigo.nome} acertou e causou {dano_ini} de dano!")
                else:
                    print(f"O {inimigo.nome} errou o ataque!")
                    
        elif acao == "2":
            fuga = dado20 + jogador.esquiva
            if fuga >= 15:
                print("Voce fugiu com sucesso!")
                return False
            else:
                print("Falha ao fugir!")
                dano_ini = dado6 + inimigo.poder - jogador.defesa
                dano_ini = max(1, dano_ini)
                jogador.receber_dano(dano_ini)
                print(f"O {inimigo.nome} te atacou enquanto fugia e causou {dano_ini} de dano!")

    if jogador.esta_vivo() and not inimigo.esta_vivo():
        print("Você venceu o combate!")
        jogador.ganhar_xp(inimigo.xp_drop)
        print(f"Você ganhou {inimigo.xp_drop} pontos de experiência!")
    elif not jogador.esta_vivo():
        print("Você foi derrotado no combate.")