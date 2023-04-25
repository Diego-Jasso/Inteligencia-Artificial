import math

# Esta función evalúa el tablero y devuelve un valor numérico que representa la puntuación de la posición
def evaluate(board):
    # Comprobar si hay algún ganador en las filas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 1
            elif board[i][0] == 'O':
                return -1
    # Comprobar si hay algún ganador en las columnas
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 1
            elif board[0][i] == 'O':
                return -1
    # Comprobar si hay algún ganador en las diagonales
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 1
        elif board[0][0] == 'O':
            return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O':
            return -1
    # Si no hay ganadores, devolver un empate
    return 0

# Esta función devuelve todas las posibles jugadas que se pueden hacer en el tablero actual
def get_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                moves.append((i, j))
    return moves

# Esta función aplica la jugada en el tablero
def apply_move(board, move, player):
    board[move[0]][move[1]] = player

# Esta función deshace la jugada en el tablero
def undo_move(board, move):
    board[move[0]][move[1]] = '-'

# Esta es la función principal del algoritmo Minimax
def minimax(board, depth, is_maximizing_player):
    # Evaluar el tablero si se alcanza la profundidad máxima o si hay un ganador
    score = evaluate(board)
    if score != 0 or depth == 0:
        return score
    # Si el jugador es el maximizador
    if is_maximizing_player:
        best_score = -math.inf
        for move in get_moves(board):
            apply_move(board, move, 'X')
            score = minimax(board, depth - 1, False)
            undo_move(board, move)
            best_score = max(best_score, score)
        return best_score
    # Si el jugador es el minimizador
    else:
        best_score = math.inf
        for move in get_moves(board):
            apply_move(board, move, 'O')
            score = minimax(board, depth - 1, True)
            undo_move(board, move)
            best_score = min(best_score, score)
        return best_score

# Esta función devuelve la mejor jugada para el jugador maximizador
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_moves(board):
        apply_move(board, move, 'X')
        score = minimax(board, 5, False)
        undo_move(board, move)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Esta es la función principal del programa
def play_game():
    # Inicializar el tablero
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    # Mostrar el tablero vacío
    print_board(board)
    # Jugar hasta que haya un ganador o un empate
    while evaluate(board) == 0:
        # Turno del jugador
        row, col = get_player_move(board)
        apply_move(board, (row, col), 'O')
        print_board(board)
        # Comprobar si el jugador ganó
        if evaluate(board) == -1:
            print("¡Ganaste!")
            return
        # Si no hay ganadores, hay un empate
        if fullboard(board) == 10:
            print("¡Empate!")
            return
        # Turno de la máquina
        print("Turno de la máquina...")
        row, col = get_best_move(board)
        apply_move(board, (row, col), 'X')
        print_board(board)
        # Comprobar si la máquina ganó
        if evaluate(board) == 1:
            print("¡Perdiste!")
            return

# Esta función lee la jugada del jugador desde la entrada estándar
def get_player_move(board):
    while True:
        try:
            row = int(input("Ingresa la fila (1-3): ")) - 1
            col = int(input("Ingresa la columna (1-3): ")) - 1
            if board[row][col] == '-':
                return row, col
            else:
                print("Esa casilla ya está ocupada.")
        except ValueError:
            print("Ingresa un número válido.")


def fullboard(board):
    aux = int
    for i in range(1,3):
        for j in range(1,3):
            if board[i][j] == '-':
                aux =  0
                return aux
            else:
                aux = 10
    return aux
            
# Esta función muestra el tablero en la consola
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Jugar al juego
play_game()