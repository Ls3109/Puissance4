import pygame


class Board:
    RED = -1
    YELLOW = 1

    winRed = -4
    winYellow = 4

    def __init__(self):
        self.board = []

    def feed_board(self):
        for row in range(6):
            self.board.append([])
            for column in range(7):
                self.board[row].append(0)

    def show(self):
        print("\n")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()
        print("\n")

    def check_horizontal(self):
        print("In check_hor")
        y = 5
        endCheck = False

        while y >= 0 and not endCheck:
            for x in range(4):
                if self.board[y][x] + self.board[y][x + 1] + self.board[y][x + 2] \
                        + self.board[y][x + 3] == self.winRed:
                    print("the winner is Red")
                    return "red"
                if self.board[y][x] + self.board[y][x + 1] + self.board[y][x + 2] \
                        + self.board[y][x + 3] == self.winYellow:
                    print("the winner is Yellow")
                    return "yellow"
            y -= 1
        return ""

    def check_vertical(self):
        print("In check_vert")
        for x in range(7):
            for y in range(5, 2, -1):
                if self.board[y][x] + self.board[y - 1][x] + self.board[y - 2][x] \
                        + self.board[y - 3][x] == self.winRed:
                    return "red"
                if self.board[y][x] + self.board[y - 1][x] + self.board[y - 2][x] \
                        + self.board[y - 3][x] == self.winYellow:
                    return "yellow"
        return ""

    def check_diagonal(self):
        for y in range(3):
            for x in range(4):
                if self.board[y][x] + self.board[y + 1][x + 1] + self.board[y + 2][x + 2] + \
                        self.board[y + 3][x + 3] == Board.winYellow:
                    return "yellow"
                if self.board[y][x] + self.board[y + 1][x + 1] + self.board[y + 2][x + 2] + \
                        self.board[y + 3][x + 3] == Board.winRed:
                    return "red"
        for y in range(3):
            for x in range(3, 7):
                if self.board[y][x] + self.board[y + 1][x - 1] + self.board[y + 2][x - 2] + \
                        self.board[y + 3][x - 3] == Board.winYellow:
                    return "yellow"
                if self.board[y][x] + self.board[y + 1][x - 1] + self.board[y + 2][x - 2] + \
                        self.board[y + 3][x - 3] == Board.winRed:
                    return "red"
        return ""
        # print("In check_diag")
        # for line in range(3):
        #     for column in range(4):
        #         print(self.board[line][column] + self.board[line + 1][column + 1] + self.board[line + 2][column + 2] + self.board[line + 3][column + 3])
        #         if self.board[line][column] + self.board[line + 1][column + 1] + self.board[line + 2][column + 2] + \
        #                 self.board[line + 3][column + 3] == Board.winYellow:
        #             return "yellow"
        #         if self.board[line][column] + self.board[line + 1][column + 1] + self.board[line + 2][column + 2] + \
        #                 self.board[line + 3][column + 3] == Board.winRed:
        #             return "red"
        # for y in range(3):
        #     for x in range(3, 7):
        #         if self.board[y][x] + self.board[y + 1][y - 1] + self.board[y + 2][x - 2] + \
        #                 self.board[y + 3][x - 3] == Board.winYellow:
        #             return "yellow"
        #         if self.board[y][x] + self.board[y + 1][x - 1] + self.board[y + 2][x - 2] + \
        #                 self.board[y + 3][x - 3] == Board.winRed:
        #             return "red"
        # return ""

    def check_column_place(self, x):
        for y in range(5):
            if self.board[y][x] == 0:
                return True

    def check_win(self):
        print("In check_win")
        gamer = self.check_horizontal()
        if gamer != "":
            return gamer
        gamer = self.check_vertical()
        if gamer != "":
            return gamer
        gamer = self.check_diagonal()
        if gamer != "":
            return gamer
        else:
            return ""

    def put_chip(self, column, gamer):
        line = 5

        stop = False
        while line >= 0 and not stop:
            if self.board[line][column] == 0:
                if gamer == Board.YELLOW:
                    self.board[line][column] = Board.YELLOW
                    stop = True
                else:
                    self.board[line][column] = Board.RED
                    stop = True
            line = line - 1

    def reverse_game_board(self):
        reversed_game_board = []
        for row in range(5, -1, -1):
            reversed_game_board.append(self.board[row])
        return reversed_game_board
