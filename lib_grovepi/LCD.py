# coding: utf-8
from lib_grovepi.defcom import *

#bus defini dans defcom.py

# Adresses de l'ecran LCD
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

# Completez le code de la fonction permettant de choisir la couleur
# du fond d'ecran, n'oubliez pas d'initialiser l'ecran
def setRGB(rouge,vert,bleu):
	# rouge, vert et bleu sont les composantes de la couleur qu'on vous demande
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,bleu)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,vert)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,rouge)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xAA)
	#print("Couleur écran changée")

def setCouleur(couleur):
	if couleur=="rouge":
		setRGB(255,0,0)
		return 1
	elif couleur=="vert":
		setRGB(0,255,0)
		return 1
	elif couleur=="bleu":
		setRGB(0,0,255)
		return 1
	elif couleur=="blanc":
		setRGB(255,255,255)
		return 1
	elif couleur=="noir":
		setRGB(0,0,0)
		return 1
	else:
		print ("Couleur non-supportée")
		return -1


# Envoie  a l'ecran une commande concernant l'affichage des caracteres
def textCmd(cmd):
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)
	time.sleep(0.06)


def initScreen():
	# bus.write_i2c_block_data(DISPLAY_TEXT_ADDR,0x80,[0x01,0x0F,0x38])
	# time.sleep(0.06)
	textCmd(0x01)
	textCmd(0x0F)
	textCmd(0x38)

def setText(texte,mode='scroll'):
	initScreen()
	# ...
	i = 0 #Nb de caracteres sur la ligne
	l = 0 #Nb de lignes
	p = False #flag print
	buf_l = [] #Buffer ligne
	for c in texte:
		i+=1
		if c == '\n':
			p=True
		elif i==16 :
			buf_l.append(ord(c))
			p=True
		else: 
			buf_l.append(ord(c))
		
		if p:
			p=False
			# envoi de la ligne à afficher à l'écran
			bus.write_i2c_block_data(DISPLAY_TEXT_ADDR,0x40,buf_l)
			l+=1
			i=0
			if l==2:
				time.sleep(1)
				initScreen()
				if mode == 'scroll':
					bus.write_i2c_block_data(DISPLAY_TEXT_ADDR,0x40,buf_l)
					textCmd(0xc0)
					l=1 
				else: 
					l=0
			else: 
				textCmd(0xc0)
			buf_l=[]
	bus.write_i2c_block_data(DISPLAY_TEXT_ADDR,0x40,buf_l)
	# print ("texte ecrit")


	
