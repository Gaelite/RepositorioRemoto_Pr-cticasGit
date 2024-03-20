import random

FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 1
META_COLUMNA = COLUMNAS - 1

def inicializar_laberinto():
    laberinto = [[False] * COLUMNAS for _ in range(FILAS)]
    laberinto[META_FILA][META_COLUMNA] = True  # Goal
    return laberinto

def imprimir_laberinto(laberinto, fila_jugador, columna_jugador):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if i == fila_jugador and j == columna_jugador:
                print("X ", end='')  # Player
            elif laberinto[i][j]:
                print("O ", end='')  # Goal
            else:
                print(". ", end='')  # Empty space
        print()

def verificar_meta(fila_jugador, columna_jugador):
    return fila_jugador == META_FILA and columna_jugador == META_COLUMNA

def obtener_movimiento(up, down, left, right, quit):
    return input(f"\nIngrese su siguiente movimiento ({up}: arriba, {down}: abajo, {left}: izquierda, {right}: derecha, {quit}: salir): ")

def mover_jugador(fila_jugador, columna_jugador, movimiento):
    if movimiento == 'w' and fila_jugador > 0:
        fila_jugador -= 1
    elif movimiento == 's' and fila_jugador < FILAS - 1:
        fila_jugador += 1
    elif movimiento == 'a' and columna_jugador > 0:
        columna_jugador -= 1
    elif movimiento == 'd' and columna_jugador < COLUMNAS - 1:
        columna_jugador += 1
    elif movimiento == 'l':
        obtener_movimiento()
    else:
        print("Movimiento no válido.")
    return fila_jugador, columna_jugador

def main():
    laberinto = inicializar_laberinto()
    fila_jugador, columna_jugador = 0, 0
    up_key = 'w'
    down_key = 's'
    left_key = 'a'
    right_key = 'd'
    quit_key = 'q'
    while True:
        imprimir_laberinto(laberinto, fila_jugador, columna_jugador)
        if verificar_meta(fila_jugador, columna_jugador):
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break
        movimiento = obtener_movimiento(up_key, down_key, left_key, right_key, quit_key)
        if movimiento == quit_key:
            print("¡Gracias por jugar!")
            break
        fila_jugador, columna_jugador = mover_jugador(fila_jugador, columna_jugador, movimiento)

if __name__ == "__main__":
    main()

#15/03/2024#

#Diego Niebla / Emiliano Galeana / Mellisa Gutierrez