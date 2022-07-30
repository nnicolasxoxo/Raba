import pygame
from pygame.locals import *
pygame.init()  #Inicializa pygame

screen= pygame.display.set_mode((1500,500)) #Tamaño de la pantalla (ancho y largo)
runing=True
velocidad = 20
direccion = True
posX, posY = (50,450) #posicion inicial
while runing:
    screen.fill((250,0,0)) #Tuplas
    pygame.draw.rect(screen,(0,250,0), 10)
    
   
    pygame.display.update()   
    