import board
import random

class Main:
    def __init__(self) -> None:
        self._mode = ""
        self._players = []
        self._order = {}
        self.settup_game()

    def settup_game(self):
        print("Tic Tac Toa\n===========\n===========\n")
        print("Welcome to Tic Tac Toa")
        while True:
            print("Modes\n=====\nRegular: The original classic Tic Tac Toa game.\n")
            self._mode = input("Select a mode.\n> ").lower()
            match self._mode:
                case "regular":
                    self._players = input("Allowed player combinations\n===========================\nPlayer player\nPlayer bot\nBot bot\nSelect one of the allowed player options\n> ").lower().split()
                case _:
                    print("Invalid input!")
                    continue
            break

        #while True:
            #match input("Who shall go first? (Random, {self._players[0]}, or {self._players[1]}).\n>").lower():
                #case "random":
                #    players = self._players
                #    while true:
                #        for i, player in players:
                #            self._order.add(random.randint(0, len(players - i)))
                #case _:
                    #print("Invalid input! Valid inouts are random, {self._players[0]}, and {self._players[1]}")
                    #continue
            #break

        while True:
            print("Available actions\n=================\nStart-game\n")
            match input("Select one of the available actions.\n> ").lower():
                case "start-game":
                    eval("self." + self._mode)()
                case _:
                    print("invalid input!")
                    continue
            break

    def regular(self):
        game_board = board.Board()
        turns = 0
        while True:
            curent_game_board = game_board.get_board()

            print(range(len(curent_game_board)), curent_game_board)

            for row in range(len(curent_game_board)):
                print("  0, 1, 2")
                print(str(row) + " " + str(curent_game_board[row]))
            
            while True:
                if self._players[0] == "player":
                    position = input("Which position would you like to take? (number,number)\n>").replace("", "").split(",")
                    if curent_game_board[int(position[0])][int(position[1])] == (" " or ""):
                        curent_game_board[int(position[0])][int(position[1])]
                        break
                print("That slot is already taken!")

            while True:
                if self._players[1] == "player":
                    position = input("Which position would you like to take? (number,number)\n>").replace("", "").split(",")
                    if curent_game_board[int(position[0])][int(position[1])] == (" " or ""):
                        curent_game_board[int(position[0])][int(position[1])]
                        break
                    print("That slot is already taken!")

            turns += 1
            if (turns > 3):
                winner = game_board.check_win()
                if winner == ("X" or "O"):
                    print(winner + "won!")
                    if self._players[0] == "player" and self._players[1] == "bot":
                        if winner == "O":
                            print("Be smarter and maybe you will win next time. :(")
                        else:
                            print("Congradulations " + winner)
                    elif self._players[0 and 1] == "player":
                        print("Congradulations " + winner)

Main()