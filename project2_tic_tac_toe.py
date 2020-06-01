#!/usr/bin/env python3

# change
import textwrap
from random import shuffle

VICTORY_CONDITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))



def show_rules():
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
    7 | 8 | 9
    ---------
    4 | 5 | 6
    ---------
    1 | 2 | 3
    ---------
    """

    print(textwrap.dedent(rules))


def show_board(board):
    print_board = f"""\
    ---------
    {board[6]} | {board[7]} | {board[8]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[0]} | {board[1]} | {board[2]}
    ---------"""
    print(textwrap.dedent(print_board))



def update_board(board, player, space):
    board[space] = player


def check_is_empty(board, space):
    return board[space] == " "

def user_input(player):
    print(f"Player {player} |", end=" ")
    while True:

        try:
            space = int(input("Choose space(number): "))

            if space in range(10):
                return space-1
            else:
                print("Choose space in valid range 1-9")
                continue
        except ValueError:
            print("Choose number")


# def check_victory2(board, player):
#
#
#     # horizontal
#     for c in range(0, 7, 3):
#         if board[c] == player and board[c + 1] == player and board[c + 2] == player:
#             return True
#
#     # vertical
#     for c in range(0, 3):
#         if board[c] == player and board[c + 3] == player and board[c + 6] == player:
#             return True
#
#     # diagonal
#     if board[0] == player and board[4] == player and board[8] == player or \
#         board[2] == player and board[4] == player and board[6] == player:
#         return True
#
#     return False

def check_victory(board, player):
    for x, y, z in VICTORY_CONDITIONS:
        if player == board[x] == board[y] == board[z]:
            return True
    return False

def check_is_tie(board):
    return " " not in board

# print_rules()
# check_victory(board)
# user_input("X")
import profile

test_board = ["o", "x", "x", "x", "x", "o", "o", "o", "o"]
sym = "o"

if __name__ == '__main__':

    board = [" " for i in range(9)]
    P1 = "X"
    P2 = "O"
    game = True
    player_order = [P1, P2]
    shuffle(player_order)
    # print(check_victory(test_board, sym))
    # show_board(test_board)
    # update_board(test_board,P1, 1)
    # show_board(test_board)
    # print(check_is_empty(test_board, 4))

    # show_rules()
    while game:

        for player in player_order:
            show_board(board)
            player_space = user_input(player)
            if not check_is_empty(board, player_space):
                print("Space is occupied. Choose another space")
                user_input(player)
            update_board(board, player, player_space)
            show_board(board)
            if check_victory(board, player):
                print(f"You win, player {player}")
                game = False
                break

            if check_is_tie(board):
                print("It is tie, nobody win")
                game = False
                break




