# Minesweeper

import random

ROWS = 5
COLS = 5
NUM_BOMBS = 5

def create_board():
    board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
    bombs = set()
    while len(bombs) < NUM_BOMBS:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        bombs.add((r, c))
    return board, bombs

def print_board(board):
    print("   " + " ".join(str(i) for i in range(COLS)))
    print("  " + "--" * COLS)
    for idx, row in enumerate(board):
        print(f"{idx}| " + " ".join(row))

def get_neighbors(row, col):
    neighbors = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) != (row, col):
                neighbors.append((r, c))
    return neighbors

def count_adjacent_bombs(row, col, bombs):
    return sum((r, c) in bombs for r, c in get_neighbors(row, col))

def reveal(board, row, col, bombs, visited):
    if (row, col) in visited or board[row][col] != " ":
        return
    visited.add((row, col))
    count = count_adjacent_bombs(row, col, bombs)
    if count > 0:
        board[row][col] = str(count)
    else:
        board[row][col] = "."
        for r, c in get_neighbors(row, col):
            reveal(board, r, c, bombs, visited)

def play():
    board, bombs = create_board()
    revealed = set()
    print("\n🧨 Welcome to Minesweeper! Type row and column separated by space (e.g., `1 2`)")

    while True:
        print_board(board)
        try:
            row, col = map(int, input("Enter row and col: ").split())
            if not (0 <= row < ROWS and 0 <= col < COLS):
                print("⚠️ Invalid position. Try again.")
                continue
            if (row, col) in bombs:
                print_board(board)
                print("💥 Boom! You hit a bomb. Game over.")
                break
            reveal(board, row, col, bombs, revealed)
            if ROWS * COLS - len(bombs) == len(revealed):
                print_board(board)
                print("🎉 Congratulations! You cleared the board.")
                break
        except Exception as e:
            print("⚠️ Invalid input. Format should be: row col (e.g., 1 3)")

if __name__ == "__main__":
    play()
