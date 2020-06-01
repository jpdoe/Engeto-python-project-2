#!/usr/bin/env python3

# change
import textwrap

board = [" " for i in range(9)]

print(board)


def print_rules():
    # \ to avoid empty line
    rules = """\
    GAME RULES:
    Each player can place one mark (or stone) per turn on the 3x3 grid
    The WINNER is who succeeds in placing three of their marks in a
    * horizontal,
    * vertical or
    * diagonal row
    Board schema:
    ---------
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    ---------
    """

    print(textwrap.dedent(rules))


def show_board(board):
    print_board = f"""\
    ---------
    {board[0]} | {board[1]} | {board[2]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[6]} | {board[7]} | {board[8]}
    ---------"""
    print(textwrap.dedent(print_board))



def update_board(board, player, cell):
    pass


def user_input(player):
    print(f"Player {player} |", end=" ")
    while True:

        try:
            cell = int(input("Choose cell(number): "))

            if cell in range(9):
                return cell
            else:
                print("Choose valid cell")
                continue
        except ValueError:
            print("Choose number")


def check_victory(board, player):

    # horizontal
    for c in range(0, 7, 3):
        if board[c] == player and board[c + 1] == player and board[c + 2] == player:
            return True

    # vertical
    for c in range(0, 3):
        if board[c] == player and board[c + 3] == player and board[c + 6] == player:
            return True

    # diagonal
    if board[0] == player and board[4] == player and board[8] == player or \
        board[2] == player and board[4] == player and board[6] == player:
        return True

    return False


# print_rules()
# check_victory(board)
# user_input("X")
import profile

m_board = ["o", "x", "o", " ", "x", "o", "o", " ", "o"]
sym = "o"

if __name__ == '__main__':
   print(check_victory(m_board,sym))
   show_board(m_board)
