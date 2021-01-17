from Player import *
from IAMinMax import *
from Game import *
import time

from lib_grovepi.button import *
from lib_grovepi.LCD import *

tabDifficulty = [0, 2, 4]
oldDifficulty = -1
i = -1
button = 2
initButton(button)

score = [0, 0]
setText("Veuillez appuyer\npour commencer")
while(readButton(button) == 0):
    time.sleep(0.1)

while(True):

    setText("choisir la\ndifficulte")
    choisi = False
    alreadyPressed = False
    pressedOnce = False

    # -- Choix de la difficulté
    while(not choisi):
        while(readButton(button) == 0):
            waitedTime = time.time()
            try:
                if(round(waitedTime - pressedTime, 2) > 0.3):
                    pressedOnce = True
                    alreadyPressed = False
                    i = i + 1
                    if(i == 3):
                        i = 0
                    diffString = "Difficulte ", (i+1)
                    setText(diffString)
            except:
                pass
            time.sleep(0.05)
        while(readButton(button) == 1):
            time.sleep(0.05)
        pressedTime = time.time()

        if(alreadyPressed and pressedOnce):
            choisi = True
        else:
            pressedOnce = True
    # -- Fin choix de difficulté

    if(oldDifficulty != -1 and oldDifficulty != tabDifficulty[i]):
        setText("Réinitialisation\ndes scores")
        score = [0, 0]
        time.sleep(1)

    oldDifficulty = tabDifficulty[i]

    setText("La partie va\ncommencer !")
    time.sleep(1)

    game = Game(iaDepth=tabDifficulty[i])  # Partie réelle contre IA
    # game = Game(commandLine=True)  # Partie terminal contre IA
    # game = Game(commandLine=True, playerOnly=True)  # Partie terminal contre Joueur
    winner = game.run()
    score[winner - 1] = score[winner - 1] + 1

    scoreString = "Vous ", score[0], " - ", score[1], " Ennemi"
    setText(scoreString)
    time.sleep(1)
