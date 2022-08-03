#Aqui voy a crear el lugar del juego llamado raba
import pygame
from pygame.locals import * 
import sys
import os

pygame.init()
pantalla= pygame.display.set_mode((1000,600))

fondo=pygame.image.load("imagenes/fondo.jpg")
pantalla.blit(fondo,(0,0))

