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
            "top_row": {"X": 0, "O": 0},
            "middle_row": {"X": 0, "O": 0},
            "bootom_row": {"X": 0, "O": 0},
            "left_column": {"X": 0, "O": 0},
            "middle_column": {"X": 0, "O": 0},
            "right_column": {"X": 0, "O": 0},
        }

        for i, row in range(len(self._board)), self._board:
            j = 0
            for j, column in range(len(self[i]._board)), self[i]._board:
                if i == 0:
                    if j == 0:
                        board_matches["top_row"][self._board[i][j]] += 1
                        board_matches["left_column"][self._board[i][j]] += 1
                    if j == 1:
                        board_matches["top_row"][self._board[i][j]] += 1
                        board_matches["middle_column"][self._board[i][j]] += 1
                    if j == 2:
                        board_matches["top_row"][self._board[i][j]] += 1
                        board_matches["right_column"][self._board[i][j]] += 1
                if i == 1:
                    if j == 0:
                        board_matches["middle_row"][self._board[i][j]] += 1
                        board_matches["left_column"][self._board[i][j]] += 1
                    if j == 1:
                        board_matches["middle_row"][self._board[i][j]] += 1
                        board_matches["middle_column"][self._board[i][j]] += 1
                    if j == 2:
                        board_matches["middle_row"][self._board[i][j]] += 1
                        board_matches["right_column"][self._board[i][j]] += 1
                if i == 2:
                    if j == 0:
                        board_matches["bootom_row"][self._board[i][j]] += 1
                        board_matches["left_column"][self._board[i][j]] += 1
                    if j == 1:
                        board_matches["bootom_row"][self._board[i][j]] += 1
                        board_matches["middle_column"][self._board[i][j]] += 1
                    if j == 2:
                        board_matches["bootom_row"][self._board[i][j]] += 1
                        board_matches["right_column"][self._board[i][j]] += 1

        async def detremin_winner():
            async for values in board_matches.values:
                if values[0] == 3:
                    return "X"
                elif values[1] == 3:
                    return "O"
        detremin_winner()
        return False