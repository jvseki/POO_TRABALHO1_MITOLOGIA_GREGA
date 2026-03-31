from entidades.jogador import Jogador
from entidades.inimigo import gerar_inimigo_fraco
from raças.raca import obter_raca
from vocacoes.invocacao import obter_vocacao
from Sistema.combate import combate
from desafios.desafios import DesafioBau

def criar_personagem():
    print("CRIACAO DE PERSONAGEM")
    nome = input("Nome do heroi: ")
    if not nome:
        nome = "Perseu"
    jogador = Jogador(nome)

    print("\nRacas: 1.Humano 2.Semideus 3.Satiro 4.Centauro 5.Ninfa")
    raca_escolha = input("Escolha a raca (1-5): ")
    raca = obter_raca(raca_escolha)
    raca.aplicar(jogador)

    print("\nVocacoes: 1.Hoplita 2.Arqueiro 3.Oraculo 4.Assassino 5.Gladiador")
    vocacao_escolha = input("Escolha a vocacao (1-5): ")
    vocacao = obter_vocacao(vocacao_escolha)
    vocacao.aplicar(jogador)

    return jogador

def main():
    jogador = criar_personagem()
    jogando = True

    while jogando and jogador.esta_vivo():
        print(f"\n{jogador.nome} | Nvl: {jogador.nivel} | {jogador.raca} {jogador.vocacao}")
        print(f"Vida: {jogador.vida_atual}/{jogador.vida_maxima} | XP: {jogador.xp}/{jogador.xp_proximo_nivel}")
        print("1. Explorar (Combate)")
        print("2. Procurar Baus")
        print("3. Descansar")
        print("4. Sair")
        escolha = input("Acao: ")

        if escolha == "1":
            inimigo = gerar_inimigo_fraco()
            combate(jogador, inimigo)
            jogador.ganhar_xp(12)
        elif escolha == "2":
            bau = DesafioBau()
            bau.executar(jogador)
        elif escolha == "3":
            cura = int(jogador.vida_atual * 0.3)
            jogador.curar(cura)
            print(f"Voce descansou. Vida atual: {jogador.vida_atual}/{jogador.vida_maxima}")
        elif escolha == "4":
            jogando = False

if __name__ == "__main__":
    main()