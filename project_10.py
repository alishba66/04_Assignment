# Tic-Tac-Toe AI

import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[r][col] == player for r in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score = minimax(board, False)
                    board[r][c] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, True)
                    board[r][c] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "O"
                score = minimax(board, False)
                board[r][c] = " "
                if score > best_score:
                    best_score = score
                    move = (r, c)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("🎮 Welcome to Tic-Tac-Toe! You are X. AI is O.\n")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row, col = map(int, input("Enter your move (row,col): ").split(","))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("❌ Cell already taken.")
            except:
                print("⚠️ Invalid input. Format: row,col (e.g., 0,2)")

        print_board(board)
        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

        # AI move
        print("\nAI is thinking...")
        row, col = best_move(board)
        board[row][col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("💻 AI wins!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    main()
