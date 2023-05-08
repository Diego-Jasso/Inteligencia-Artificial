import sys
import time

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()

# Función para verificar si el juego ha terminado y hay un ganador
def hay_ganador(tablero, jugador):
    # Verificar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True

    # Verificar columnas
    for j in range(3):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] == jugador:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para evaluar el estado del tablero
def evaluar(tablero):
    if hay_ganador(tablero, "X"):
        return 1
    elif hay_ganador(tablero, "O"):
        return -1
    else:
        return 0

# Función para encontrar el mejor movimiento utilizando el algoritmo Minimax con poda alfa-beta
def minimax(tablero, profundidad, es_maximizador, alfa, beta):
    puntuacion = evaluar(tablero)

    if puntuacion == 1:
        return puntuacion - profundidad
    if puntuacion == -1:
        return puntuacion + profundidad
    if puntuacion == 0 and len(movimientos_disponibles(tablero)) == 0:
        return 0

    if es_maximizador:
        mejor_valor = -sys.maxsize
        for movimiento in movimientos_disponibles(tablero):
            tablero[movimiento[0]][movimiento[1]] = "X"
            valor = minimax(tablero, profundidad + 1, False, alfa, beta)
            tablero[movimiento[0]][movimiento[1]] = " "
            mejor_valor = max(mejor_valor, valor)
            alfa = max(alfa, mejor_valor)
            if beta <= alfa:
                break
        return mejor_valor
    else:
        mejor_valor = sys.maxsize
        for movimiento in movimientos_disponibles(tablero):
            tablero[movimiento[0]][movimiento[1]] = "O"
            valor = minimax(tablero, profundidad + 1, True, alfa, beta)
            tablero[movimiento[0]][movimiento[1]] = " "
            mejor_valor = min(mejor_valor, valor)
            beta = min(beta, mejor_valor)
            if beta <= alfa:
                break
        return mejor_valor

# Función para obtener la lista de movimientos disponibles en el tablero
def movimientos_disponibles(tablero):
    movimientos = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                movimientos.append((i, j))
    return movimientos

# Función para que el jugador humano realice su movimiento
def turno_jugador(tablero):
    while True:
        fila = int(input("Ingrese la fila (0-2): "))
        columna = int(input("Ingrese la columna (0-2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "O"
            break
        else:
            print("La casilla está ocupada. Intente nuevamente.")

# Función para que la computadora realice su movimiento utilizando el algoritmo Minimax con poda alfa-beta
def turno_computadora(tablero):
    mejor_valor = -sys.maxsize
    mejor_movimiento = None
    for movimiento in movimientos_disponibles(tablero):
        tablero[movimiento[0]][movimiento[1]] = "X"
        valor = minimax(tablero, 1, False, -sys.maxsize, sys.maxsize)
        tablero[movimiento[0]][movimiento[1]] = " "
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento
    tablero[mejor_movimiento[0]][mejor_movimiento[1]] = "X"

# Función principal para ejecutar el juego
def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    imprimir_tablero(tablero)
    while True:
        turno_jugador(tablero)
        imprimir_tablero(tablero)
        if hay_ganador(tablero, "O"):
            print("¡Ganaste!")
            break
        if len(movimientos_disponibles(tablero)) == 0:
            print("¡Empate!")
            break
        inicio = time.time()
        turno_computadora(tablero)
        fin = time.time()
        tiempo = fin-inicio
        imprimir_tablero(tablero)
        print("%f" % tiempo)
        if hay_ganador(tablero, "X"):
            print("¡Perdiste!")
            break

# Ejecutar el juego
jugar()
