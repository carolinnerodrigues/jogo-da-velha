def game():
    movement = 0 #Contabiliza o numero de rodadas, é incrementada a cada rodada

    #cada jogador é simbolizado por: (jogada%2 + 1), 0 e 1
    while winner() == 0:
        print("\nJogador ", movement % 2 + 1)
        view()
        line = int(input("\nX :"))
        column = int(input("Y:"))

        if board[line - 1][column - 1] == 0:
            if (movement % 2 + 1) == 1:
                board[line - 1][column - 1] = 1
            else:
                board[line - 1][column - 1] = -1
        else:
            print("Nao esta vazio")
            movement -= 1

        if winner():
            print("Jogador ", movement % 2 + 1, " ganhou apos ", movement + 1, " rodadas")

        movement += 1

def winner():
    # checando linhas
    for i in range(3):
        sum = board[i][0] + board[i][1] + board[i][2]
        if sum == 3 or sum == -3:
            return 1

    # checando colunas
    for i in range(3):
        sum = board[0][i] + board[1][i] + board[2][i]
        if sum == 3 or sum == -3:
            return 1

    # checando diagonais
    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0

def view():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')
        print()

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

game()