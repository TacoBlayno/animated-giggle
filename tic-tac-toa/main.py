import board

class Main:
    def __init__(self) -> None:
        self._mode = ""
        self._players = []
        self.settup_game()

    def settup_game(self):
        print("Tic Tac Toa\n===========\n===========\n")
        print("Welcome to Tic Tac Toa")
        print("Modes\n=====\nRegular: The original classic Tic Tac Toa game.\n")
        self._mode = input("Select a mode.\n> ").lower()
        match self._mode:
            case "regular":
                self._players = input("Allowed player combinations\n===========================\nPlayer player\nPlayer bot\nBot bot\nSelect one of the allowed player options\n> ").lower().split()

        print("Available actions\n=================\nStart-game\n")
        match input("Select one of the available actions.\n> ").lower():
            case "start-game":
                eval("self." + self._mode)()

    def regular(self):
        game_board = board.Board()
        turns = 0
        while True:
            curent_game_board = game_board.get_board()

            for row in curent_game_board:
                print(row)
            
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