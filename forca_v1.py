# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe

# Tratando exceções
class InputLetterException(Exception):
    """Exception raised for errors in the input.

        Attributes:
            message -- explanation of the error
    """
    def __init__(self, message):
        super().__init__(message)


class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = str(word)
        self.acertos = []
        self.erros = []

    # Método para adivinhar a letra
    def guess(self, letter):
        # verifica se a letra esta na palavra word
        if letter in self.word:
            self.acertos.append(letter)
        else:
            self.erros.append(letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if len(self.erros) >= 6:
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        for i in self.word:
            if i not in self.acertos:
                return False
        return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        tamanho_word = len(self.word)
        if len(self.acertos) == 0:
            # cada letra codificada com underline _
            return tamanho_word * "_"
        else:
            palavra = ''
            for i in self.word:
                if i in self.acertos:
                    palavra += i
                else:
                    palavra += '_'
            return palavra

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print("\n" + board[len(self.erros)])
        print("\nPalavra: " + self.hide_word())
        print("\nLetras Erradas: ")
        for i in self.erros:
            print(i)
        print("\nLetras Corretas: ")
        for i in self.acertos:
            print(i)


    #metodo para chamar uma letra
    def get_letter(self):

        while True:
            try:
                letra = input("\nDigite uma letra: ")
                if not letra.isalpha():
                    raise InputLetterException("Não é uma letra")
                if len(letra) != 1:
                    raise InputLetterException("Não é apenas uma letra")
                if letra.lower() in self.acertos or letra.lower() in self.erros:
                    raise InputLetterException("Letra já usada")
            except InputLetterException as erro:
                print(erro)
                continue
            else:
                return letra.lower()


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()



# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word().lower())

    game.print_game_status()

    while not(game.hangman_over() or game.hangman_won()):
        # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
        letra = game.get_letter()
        game.guess(letra)

        # Verifica o status do jogo
        game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()

