import random

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, outro):
        dano = random.randint(1, self.ataque)
        outro.vida -= dano
        print(f"{self.nome} ataca {outro.nome} e causa {dano} de dano!")

    def esta_vivo(self):
        return self.vida > 0

def main():
    print("Bem-vindo ao RPG!")
    
    # Criar personagens
    jogador = Personagem("Heroi", 30, 10)
    inimigo = Personagem("Monstro", 20, 8)

    # Loop de combate
    while jogador.esta_vivo() and inimigo.esta_vivo():
        # Jogador ataca
        jogador.atacar(inimigo)

        if inimigo.esta_vivo():
            # Inimigo ataca
            inimigo.atacar(jogador)
            print(f"{jogador.nome} tem {jogador.vida} de vida restante.")
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.")
        else:
            print(f"{inimigo.nome} foi derrotado!")

    if jogador.esta_vivo():
        print(f"{jogador.nome} venceu a batalha!")
    else:
        print(f"{jogador.nome} foi derrotado!")

if __name__ == "__main__":
    main()
