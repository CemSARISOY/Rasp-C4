from Player import *
from IAMinMax import *
from Game import *
import time

from lib_grovepi.button import *
from lib_grovepi.LCD import *

tabDifficulte = [0, 2, 4]
i = -1
button = 2
initButton(button)
setText("choisir\nla difficulte")
choisi = False
alreadyPressed = False
pressedOnce = False
while(not choisi):
#        start = time.time()
        while(readButton(button) == 0):
                test = time.time()
                try:
                      start
                      if(round(test - start, 2) > 0.5):
                            alreadyPressed = False
                except:
                      pass
                time.sleep(0.05)       
        while(readButton(button) == 1):
                time.sleep(0.05)
        if(alreadyPressed):
                #end = time.time()
                alreadyPressed = False
                choisi = True
        elif(pressedOnce):
                alreadyPressed = True
                start = time.time()
        pressedOnce = True
        #try:
              #end
              #start
             # print(start)
             # print(end)
            #  print(round(end-start, 2))
           #   if(round(end-start, 2) < 0.5 and round(end-start, 2) >0):
          #          i = i - 1
         #           choisi = True
        #except:
              #pass 
#        end = time.time()
#        if(round(end - start, 2) > 5):
#                choisi = True
        if(not choisi):
                i = i + 1
                if(i==3):
                       i=0
                if(i==0):
                       setText("Difficulte 1")
                elif(i==1):
                       setText("Difficulte 2")
                else:
                       setText("Difficulte 3")
i = i - 1

if(i == -1):
     i = 2

if(i==0):
       setText("Choisi 1")
elif(i==1):
       setText("Choisi 2")
else:
       setText("Choisi 3")

print("Choisi : ", i+1)       

#game = Game(iaDepth = tabDifficulte[i])  # Partie réelle contre IA
#game = Game(commandLine=True)  # Partie terminal contre IA
game = Game(commandLine=True, playerOnly=True) # Partie terminal contre Joueur
game.run()
