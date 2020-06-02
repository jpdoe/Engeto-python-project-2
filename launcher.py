#!/usr/bin/env python3

# Description: Project 2 - Part 3 'Launcher for BC and TTT game' for Engeto Online Python Academy
# Author: Jan Polák

from bulls_cows import game_loop as bc_game_loop
from tic_tac_toe import game_loop as tc_game_loop


while True:
    print(16 * "*")
    print("Choose your game:")
    print("1. Bulls and cows")
    print("2. Tic Tac Toe")
    print("3. Exit")
    print(16 * "*")

    try:
        choice = int(input("Your choice: "))

        if choice in range(1, 4):
            if choice == 1:
                bc_game_loop()
                print("")
            elif choice == 2:
                tc_game_loop()
                print("")
            else:
                exit()
        else:
            print("Choose valid number")
            continue
    except ValueError:
        print("This is not number")


