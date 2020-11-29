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
            hasWon = self.__board.placePawn(
                self.__players[self.__turn].getId(), col)
            self.__board.printBoard()
            if(hasWon):
                print("Gagnant : ", self.__players[self.__turn].getId())
                self.__playing = False
            if(self.__turn == 0):
                self.__turn = 1
            else:
                self.__turn = 0
