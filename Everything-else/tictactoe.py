import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j], end="")
        print("|   |")
    print("---------")

# Function to check if any player has won
def check_win(board, player):
    # Check rows
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True

    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to make the bot's move
def make_bot_move(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = "O"

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        if player == "X":
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = "X"
        else:
            make_bot_move(board)

        if check_win(board, player):
            print_board(board)
            print(player + " wins!")
            break
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

# Start the game
play_game()
