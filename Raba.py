#Aqui voy a crear el lugar del juego llamado raba
import pygame
from pygame.locals import * 
import sys
import os

pygame.init()
pantalla= pygame.display.set_mode((1500,500))
pygame.display.set_caption ("Raba")
while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()

fondo=pygame.image.load("imagenes/fondo.jpg")
pantalla.blit(fondo,(0,0))

