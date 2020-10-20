from Player import Player
from Board import Board


class Game:
    def __init__(self, p1, p2):
        self.__board = Board()
        self.__players = [p1, p2]
        self.__turn = 0
        self.__playing = True

    def run(self):
        while(self.__playing):
            played = False
            col = 0
            while(not played):
                col = self.__players[self.__turn].play(self.__board)
                if(self.__board.isValid(col)):
                    played = True
            self.__board.placePawn(self.__players[self.__turn], col)
            if(self.__turn == 0):
                self.__turn = 1
            else:
                self.__turn = 0
            self.__board.printBoard()

            gagnant = self.__board.detectWin()
            if(gagnant != 0):
                print("Gagnant : "+str(gagnant))
                self.__playing = False

# 2 jetons aligné = 1
# 3 jetons aligné = 5
# 4 jetons aligné = 200
