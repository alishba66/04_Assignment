# Connect Four

ROWS = 6
COLUMNS = 7

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(map(str, range(1, COLUMNS+1))))
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("-" * (COLUMNS * 4 + 1))

def is_valid_column(board, col):
    return board[0][col] == " "

def get_next_open_row(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == " ":
            return row

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    # Vertical
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    # Diagonal \
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    return False

def is_board_full(board):
    return all(board[0][c] != " " for c in range(COLUMNS))

def main():
    board = create_board()
    game_over = False
    turn = 0

    print("Welcome to Connect Four! 🎉")
    print_board(board)

    while not game_over:
        player = "X" if turn % 2 == 0 else "O"
        try:
            col = int(input(f"Player {player}, choose a column (1-{COLUMNS}): ")) - 1
            if col < 0 or col >= COLUMNS:
                print("Invalid column. Try again.")
                continue
            if not is_valid_column(board, col):
                print("Column is full. Try a different one.")
                continue
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, player)

            print_board(board)

            if winning_move(board, player):
                print(f"🏆 Player {player} wins!")
                game_over = True
            elif is_board_full(board):
                print("It's a draw!")
                game_over = True
            else:
                turn += 1
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
