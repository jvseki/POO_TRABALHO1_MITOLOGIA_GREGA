import time

from entidades.jogador import Jogador
from racas.raca import obter_raca
from vocacoes.invocacao import obter_vocacao
from entidades.inimigo import gerar_inimigo_fraco
from sistema.combate import combate
from desafios.desafios import DesafioBau


def historia():
    frases = [
        "Muito antes do seu nome existir...",
        "Antes mesmo dos deuses temerem um mortal...",
        "Uma lenda começou a ser escrita na antiga Grécia.",
        
        "Nascido sob um presságio sombrio...",
        "Você cresceu entre guerras, monstros e deuses impiedosos.",
        
        "Dizem que seu poder rivalizava com o do próprio Zeus.",
        "E que um dia... você ousou enfrentá-lo.",
        
        "Mas nessa batalha...",
        "Algo deu errado.",
        
        "Um golpe desconhecido atingiu sua mente...",
        "E tudo foi apagado.",
        
        "Seu passado...",
        "Seu nome...",
        "Sua raça...",
        "Sua vocação...",
        "Tudo desapareceu.",
        
        "Agora você desperta, sozinho...",
        "Em um mundo que parece te conhecer...",
        "Mas que você não reconhece.",
        
        "Uma coisa, porém, ainda queima dentro de você...",
        "Vingança.",
        
        "Você não sabe quem é...",
        "Mas sabe que alguém fez isso com você.",
        
        "E não importa se terá que enfrentar monstros...",
        "Semideuses...",
        "Ou os próprios deuses do Olimpo...",
        
        "Você vai recuperar sua memória.",
        "E destruir aquele que tentou apagar sua existência."
    ]
    
    escolha = input("Deseja ouvir a historia? (s/n) ")
    if escolha.lower() == "s":
        for frase in frases:
            print(frase)
            time.sleep(2)
    else:
        print("Você ignora seu passado... por enquanto.")


def criar_personagem():
    nome = input("\nDigite o nome do seu personagem: ")
    jogador = Jogador(nome)

    print("\nEscolha sua raça:")
    print("1. Humano")
    print("2. Ciclopes")
    print("3. Satiro")
    print("4. Centauro")
    print("5. Ninfa")

    escolha_raca = input(">> ")
    raca = obter_raca(escolha_raca)
    raca.aplicar(jogador)

    print("\nEscolha sua vocação:")
    print("1. Hoplita")
    print("2. Arqueiro")
    print("3. Oráculo")
    print("4. Assassino")
    print("5. Gladiador")

    escolha_vocacao = input(">> ")
    vocacao = obter_vocacao(escolha_vocacao)
    vocacao.aplicar(jogador)

    print(f"\n{jogador.nome} criado com sucesso!")
    print(f"\nRaça: {jogador.raca} | Vocação: {jogador.vocacao}")
    print(f"\nPoder: {jogador.poder} | Vida: {jogador.vida_maxima}")
    
    return jogador


def menu_acoes(jogador):
    while jogador.esta_vivo():
        print("\n===== O que deseja fazer? =====")
        print("1 - Procurar Inimigo")
        print("2 - Procurar Baú")
        print("3 - Descansar (cura 25%)")
        print("4 - Sair do jogo")

        escolha = input("Escolha: ")

        if escolha == "1":
            inimigo = gerar_inimigo_fraco()
            combate(jogador, inimigo)
        
        elif escolha == "2":
            evento = DesafioBau()
            evento.executar(jogador)

        elif escolha == "3":
            jogador.curar(int(jogador.vida_maxima * 0.25))
            print(f"\nVocê descansou e recuperou parte da sua vida.")
        
        elif escolha == "4":
            print("\nObrigado por jogar! Até a próxima aventura!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")
        
        print(f"\nVida atual: {jogador.vida_atual}/{jogador.vida_maxima}")

    if not jogador.esta_vivo():
        print("\nVocê morreu... Mas a lenda continua viva. Tente novamente!")


def menu():
    while True:
        print("\n===== Bem-Vindo ao RPG Mitologia Grega! =====")
        print("1 - Iniciar jogo")
        print("2 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            historia()
            jogador = criar_personagem()
            menu_acoes(jogador)

        elif escolha == "2":
            print("\nSaindo do jogo...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()