import math

def print_board(board):
    for i in range(3):
        print(board[3*i:3*i+3])
    print()

def is_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

def is_board_full(board):
    return all(spot != ' ' for spot in board)

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    board = [' ' for _ in range(9)]
    print("Tic Tac Toe! You are 'O', computer is 'X'.")
    print_board(board)
    
    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move, try again.")
            continue
        board[move] = 'O'
        print_board(board)
        if is_winner(board, 'O'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # Computer move
        comp_move = best_move(board)
        board[comp_move] = 'X'
        print("Computer plays:")
        print_board(board)
        if is_winner(board, 'X'):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
