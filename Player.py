import random
import os
import sys
import json
import time
import io

from lib_grovepi.button import *
from lib_grovepi.LCD import *
from lib_grovepi.LED import *


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
        led = 7
        setRGB(50, 150, 0)
        setText("C'est a votre\ntour !")
        button = 2
        initButton(button)
        print("Joueur " + str(self.__id))
        if(not self.__isCommandline):
            try:
                onLED(led)
                while (readButton(button) == 0):
                    time.sleep(0.1)
                offLED(led)
                setText("A l'adversaire !")
                differenceTab = []
                col = -1
                while(col == -1):
                    os.system("raspistill -o plateau.png")
                    os.system("python3.6 ./scripts/detection.py plateau")

                    while(not os.path.exists("tab.txt")):  # Bloquer
                        time.sleep(0.1)
                    with io.open("tab.txt", mode="r", encoding="utf8") as f:
                        text = f.read()

                    # parse les données du fichier tab.txt
                    tab = json.loads(text)
                    os.remove("tab.txt")

                    # fonction de detection de différence

                    difference = board.compare(tab)

                    # Si il y a une unique différence entre les données detectées et le board en mémoire,
                    # alors le joueur à joué cette case
                    if(len(difference) == 1):
                        col = difference[0][1]
                    elif(len(difference) > 1):
                        raise RuntimeError("Trop de différence")
                    else:
                        time.sleep(2)
            except IOError:
                print("error")
        else:
            col = int(input())
        return col
