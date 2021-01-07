import random
import os
import sys
import json
import time
import io

from lib_grovepi.button import *

class Player:
    def __init__(self, id, commandline=False):
        self.__id = id
        self.__isCommandline = commandline

    def getId(self):
        return self.__id

    def play(self, board):
        """
        Pré-requis :
            board (Board) : Représente le plateau dans lequel le joueur doit jouer
        Résultat :
            Retourne la colonne entrée dans le terminal si le joueur est en mode terminal,
            sinon retourne la colonne detectée grâce à la photo prise.
        """
        button = 2
        initButton(button)
        print("Joueur " + str(self.__id))
        if(not self.__isCommandline):
            try:
                while (readButton(button) == 0):
                    time.sleep(0.1)
                differenceTab = []
                col = -1
                while(col == -1):
                    # os.system("sudo raspistill -o plateau.png")
                    print(os.system("python3 ../scripts/detection.py plateau"))

                    while(not os.path.exists("tab.txt")):  # Bloquer
                        time.sleep(0.1)
                    with io.open("tab.txt", mode="r", encoding="utf8") as f:
                        text = f.read()

                    tab = json.loads(text)  # parse les données du fichier tab.txt
                    os.remove("tab.txt")

                    # fonction de detection de différence

                    difference = board.compare(tab)

                    # Si il y a une unique différence entre les données detectées et le board en mémoire,
                    # alors le joueur à joué cette case
                    if(len(difference) == 1):
                        col = difference[0][1]
                    else:
                        time.sleep(2)
            except IOError:
                print("error")
        else:
            col = int(input())
        return col
