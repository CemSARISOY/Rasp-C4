import numpy as np
import cv2 as cv
import sys
import io

boundaries = [
    ([0, 15, 100], [50, 50, 255]),
    ([0, 150, 150], [50, 255, 255]),
]
imgG = cv.imread(str(sys.argv[1]) + '.png', 0)
cimg = cv.cvtColor(imgG, cv.COLOR_GRAY2BGR)

img = cv.imread(str(sys.argv[1]) + ".png", 1)

lowerRed = np.array(boundaries[0][0], dtype="uint8")
upperRed = np.array(boundaries[0][1], dtype="uint8")

lowerYellow = np.array(boundaries[1][0], dtype="uint8")
upperYellow = np.array(boundaries[1][1], dtype="uint8")

maskRed = cv.inRange(img, lowerRed, upperRed)
maskYellow = cv.inRange(img, lowerYellow, upperYellow)

outputRed = cv.bitwise_and(img, img, mask=maskRed)
gimg = cv.cvtColor(outputRed, cv.COLOR_BGR2GRAY)

circlesRed = cv.HoughCircles(gimg, cv.HOUGH_GRADIENT, 1, 150,
                             param1=1, param2=20, minRadius=60, maxRadius=120)

circles = np.uint16(np.around(circlesRed))
for i in circles[0, :]:
    # draw the outer circle
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)


tabRed = []
if(not (circlesRed is None)):
    circlesRed = np.uint16(np.around(circlesRed))
    for i in circlesRed[0, :]:
        x = i[0]
        y = i[1]
        l = len(gimg[0])/7
        h = len(gimg)/6
        colonne = x // l
        hauteur = y // h
        tabRed.append((int(colonne), int(hauteur)))

outputYellow = cv.bitwise_and(img, img, mask=maskYellow)
gimg = cv.cvtColor(outputYellow, cv.COLOR_BGR2GRAY)
circlesYellow = cv.HoughCircles(gimg, cv.HOUGH_GRADIENT, 1, 150,
                                param1=1, param2=20, minRadius=60, maxRadius=120)

tabYellow = []
if(not (circlesYellow is None)):
    circles = np.uint16(np.around(circlesYellow))
    for i in circles[0, :]:
        # draw the outer circle
        cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    for i in circlesYellow[0, :]:
        x = i[0]
        y = i[1]
        l = len(gimg[0])/7
        h = len(gimg)/6
        colonne = x // l
        hauteur = y // h
        tabYellow.append((int(colonne), int(hauteur)))
# print(tabRed)  # Red = 1
# print(tabYellow)  # Yellow =2

tab = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

for i in tabRed:
    tab[i[1]][i[0]] = 1

for i in tabYellow:
    tab[i[1]][i[0]] = 2

for i in tab:
    print(i)

with io.open("tab.txt", "w", encoding="utf8") as f:
    f.write(str(tab))
