import random

class CampoMinado:
    def __init__(self, largura, altura, minas):
        self.largura = largura
        self.altura = altura
        self.minas = minas
        self.tabuleiro = [[' ' for _ in range(largura)] for _ in range(altura)]
        self.minas_pos = set()
        self.revelado = [[False for _ in range(largura)] for _ in range(altura)]
        self.gerar_minhas()

    def gerar_minhas(self):
        while len(self.minas_pos) < self.minas:
            x = random.randint(0, self.largura - 1)
            y = random.randint(0, self.altura - 1)
            if (x, y) not in self.minas_pos:
                self.minas_pos.add((x, y))
                self.tabuleiro[y][x] = '*'
                self.atualizar_contadores(x, y)

    def atualizar_contadores(self, x, y):
        for i in range(max(0, y - 1), min(self.altura, y + 2)):
            for j in range(max(0, x - 1), min(self.largura, x + 2)):
                if self.tabuleiro[i][j] != '*':
                    if self.tabuleiro[i][j] == ' ':
                        self.tabuleiro[i][j] = '1'
                    else:
                        self.tabuleiro[i][j] = str(int(self.tabuleiro[i][j]) + 1)

    def revelar(self, x, y):
        if (x, y) in self.minas_pos:
            return True  # Jogador perdeu
        self.revelado[y][x] = True
        return False  # Jogador continua

    def exibir_tabuleiro(self):
        for y in range(self.altura):
            for x in range(self.largura):
                if self.revelado[y][x]:
                    print(self.tabuleiro[y][x], end=' ')
                else:
                    print('.', end=' ')
            print()

def main():
    largura = 5
    altura = 5
    minas = 3
    jogo = CampoMinado(largura, altura, minas)

    while True:
        jogo.exibir_tabuleiro()
        try:
            x = int(input("Digite a coluna (0 a {}): ".format(largura - 1)))
            y = int(input("Digite a linha (0 a {}): ".format(altura - 1)))
            if jogo.revelar(x, y):
                print("Você atingiu uma mina! Jogo terminado.")
                break
        except ValueError:
            print("Entrada inválida. Tente novamente.")
        except IndexError:
            print("Coordenadas fora do limite. Tente novamente.")

if __name__ == "__main__":
    main()
