import random


class Player:
    def __init__(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def play(self, board):
        print("Joueur " + str(self.__id))
        col = int(input())
        return col
