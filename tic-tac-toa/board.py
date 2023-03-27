class Board:
    def __init__(self) -> None:
        self._board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def get_board(self):
        return self._board
    
    def set_board(self, board):
        self._board = board

    def check_win(self):
        board_matches = {
            "top_row": { "X": 0, "O": 0, " ": 0 },
            "middle_row": { "X": 0, "O": 0, " ": 0 },
            "bootom_row": { "X": 0, "O": 0, " ": 0 },
            "left_column": { "X": 0, "O": 0, " ": 0 },
            "middle_column": { "X": 0, "O": 0, " ": 0 },
            "right_column": { "X": 0, "O": 0, " ": 0 },
        }

        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if row == 0:
                    if column == 0:
                        board_matches["top_row"][self._board[row][column]] += 1
                        board_matches["left_column"][self._board[row][column]] += 1
                    if column == 1:
                        board_matches["top_row"][self._board[row][column]] += 1
                        board_matches["middle_column"][self._board[row][column]] += 1
                    if column == 2:
                        board_matches["top_row"][self._board[row][column]] += 1
                        board_matches["right_column"][self._board[row][column]] += 1
                if row == 1:
                    if column == 0:
                        board_matches["middle_row"][self._board[row][column]] += 1
                        board_matches["left_column"][self._board[row][column]] += 1
                    if column == 1:
                        board_matches["middle_row"][self._board[row][column]] += 1
                        board_matches["middle_column"][self._board[row][column]] += 1
                    if column == 2:
                        board_matches["middle_row"][self._board[row][column]] += 1
                        board_matches["right_column"][self._board[row][column]] += 1
                if row == 2:
                    if column == 0:
                        board_matches["bootom_row"][self._board[row][column]] += 1
                        board_matches["left_column"][self._board[row][column]] += 1
                    if column == 1:
                        board_matches["bootom_row"][self._board[row][column]] += 1
                        board_matches["middle_column"][self._board[row][column]] += 1
                    if column == 2:
                        board_matches["bootom_row"][self._board[row][column]] += 1
                        board_matches["right_column"][self._board[row][column]] += 1

        for values in board_matches.values():
            if values["X"] == 3:
                return "X"
            elif values["O"] == 3:
                return "O"
        return False