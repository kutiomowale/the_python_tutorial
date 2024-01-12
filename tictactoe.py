#!/usr/bin/env python3
"""A Tic Tac Toe command line game

Code gotten from:
    https://code.activestate.com/recipes/578816-the-game-of-tic-tac-toe-in-python/

And modified with the help of Chatgpt
"""


def print_board(board):
    print("The board looks like this:\n")
    for i in range(3):
        for j in range(3):
            cell = board[i * 3 + j]
            if cell == 'X':
                print('X', end=' ')
            elif cell == 'O':
                print('O', end=' ')
            else:
                print(' ', end=' ')
            if j < 2:
                print('|', end=' ')
        print()
        if i < 2:
            print('-'*9)


def print_instruction():
    print("Please use the following cell numbers to make your move")
    print_board([str(i) for i in range(1, 10)])


def get_input(turn):
    while True:
        try:
            user = int(input(f"Where would you like to place {turn} (1-9)? "))
            if 1 <= user <= 9:
                return user - 1
            else:
                print("That is not a valid move! Please try again.\n")
                print_instruction()
        except ValueError:
            print("Invalid input! Please enter a number (1-9).\n")


def check_win(board):
    win_cond = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_cond:
        if board[each[0]] == board[each[1]] == board[each[2]] != ' ':
            return board[each[0]]
    return -1


def quit_game(board, msg):
    print_board(board)
    print(msg)
    quit()


def main():
    print_instruction()

    board = [' ']*9
    win = False
    move = 0

    while not win:
        print_board(board)
        print(f"Turn number {move+1}")
        turn = 'X' if move % 2 == 0 else 'O'

        user = get_input(turn)
        while board[user] != ' ':
            print("Invalid move! Cell already taken. Please try again.\n")
            user = get_input(turn)
        board[user] = turn

        move += 1
        if move > 4:
            winner = check_win(board)
            if winner != -1:
                out = f"The winner is {winner} :)"
                quit_game(board, out)
            elif move == 9:
                quit_game(board, "No winner :(")


if __name__ == "__main__":
    main()
