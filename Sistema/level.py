import math

def calculo_nivel(nivel_atual):
    return math.floor(100 * (1.4 ** (nivel_atual - 1)))

def upando_status(jogador):
    jogador.poder = math.floor(jogador.poder * 1.5)
    jogador.defesa = math.floor(jogador.defesa * 1.5)
    jogador.vida_maxima = math.floor(jogador.vida_maxima * 1.5)
    jogador.esquiva = math.floor(jogador.esquiva * 1.5)
    
    print(f"\nLEVEL UP!")
    print(f"Nível Atual: {jogador.nivel}")
    print(f"Novos Status -> Poder: {jogador.poder} | Vida: {jogador.vida_maxima}")