import random

class DesafioBase:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class DesafioBau(DesafioBase):
    def __init__(self):
        super().__init__("Bau do Olimpo", "Um bau misterioso com escritas gregas.")

    def executar(self, jogador):
        print(f"\nVoce encontrou: {self.nome}")
        print(self.descricao)
        print("1. Tentar abrir")
        print("2. Ignorar")
        escolha = input("Escolha: ")
        
        if escolha == "1":
            sorte = random.randint(1, 20)
            if sorte > 10:
                cura = 10
                jogador.curar(cura)
                print(f"O bau continha Ambrosia! Voce recuperou {cura} de vida.")
            else:
                dano = 5
                jogador.receber_dano(dano)
                print(f"Era uma armadilha de Hades! Voce sofreu {dano} de dano.")
        return True