#Aqui se estara creando a la princesa gaby

import pygame
from pygame.locals import *
pygame.init()  #Inicializa pygame

screen= pygame.display.set_mode((1500,500)) #Tamaño de la pantalla (ancho y largo)
runing=True
velocidad = 20
direccion = True
negro=(0,0,0)
while runing:
    screen.fill((250,0,0)) #Tuplas
    pygame.draw.rect(screen, negro,[150,50,400,400], 0)
    
   
    pygame.display.update() 