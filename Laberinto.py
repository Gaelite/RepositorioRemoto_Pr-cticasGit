import random
# Eduardo Gael García Zuviría 22 de marzo de 2024

FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 2
META_COLUMNA = COLUMNAS - 1
def main():
    laberinto = [[False] * COLUMNAS for _ in range(FILAS)]
    fila_jugador, columna_jugador = 0, 0
    # Inicializar el laberinto
    laberinto[META_FILA][META_COLUMNA] = True  # Meta
    # Bucle principal del juego
    while True:
        # Imprimir el laberinto
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if i == fila_jugador and j == columna_jugador:
                    print("X ", end='')  # Jugador
                elif laberinto[i][j]:
                    print("O ", end='')  # Meta
                else:
                    print(". ", end='')  # Espacio vacío
            print()
        # Verificar si el jugador alcanzó la meta
        if fila_jugador == META_FILA and columna_jugador == META_COLUMNA:
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break
        # Solicitar al jugador el siguiente movimiento
        movimiento = input("\nIngrese su siguiente movimiento (w: arriba, s: abajo, a: izquierda, d: derecha): ")

        # Mover al jugador según la entrada del usuario
        if movimiento == 'w' and fila_jugador > 0:
            fila_jugador -= 1
        elif movimiento == 's' and fila_jugador < FILAS - 1:
            fila_jugador += 1
        elif movimiento == 'a' and columna_jugador > 0:
            columna_jugador -= 1
        elif movimiento == 'd' and columna_jugador < COLUMNAS - 1:
            columna_jugador += 1
        else:
            print("Movimiento no válido.")

if __name__ == "__main__":
    main()

#15/03/2024#

#Diego Niebla / Emiliano Galeana / Mellisa Gutierrez

    