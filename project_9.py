# Tic-Tac-Toe
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("🎮 Welcome to Tic-Tac-Toe!\n")
    print_board(board)

    while True:
        try:
            move = input(f"\nPlayer {current_player}, enter your move (row,col): ")
            row, col = map(int, move.strip().split(","))

            if board[row][col] != " ":
                print("❌ Cell already taken. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break
            elif is_draw(board):
                print("🤝 It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("⚠️ Invalid input. Use format row,col (e.g., 0,2) and valid positions.")

if __name__ == "__main__":
    main()
