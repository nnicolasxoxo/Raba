#Aqui se estara creando a la princesa gaby

 #Aqui esta mi personaje principal Niga
import pygame
from pygame.locals import *
pygame.init()  #Inicializa pygame

screen= pygame.display.set_mode((1500,500)) #Tamaño de la pantalla (ancho y largo)
runing=True
velocidad = 20
direccion = True
posX, posY = (50,450) #posicion inicial
while runing:
    screen.fill((0,0,0)) #Tuplas
    pygame.draw.circle(screen,(200,0,0),(posX,posY), 20)
    
    for event in pygame.event.get():  
        if event.type==pygame.QUIT:
            runing=False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                posX-=velocidad
                if posX<100:
                    posX=100
            elif event.key == K_RIGHT:
                posX+=velocidad
                if posX>(1500-50):
                    posX=1500-50
            elif event.key == K_UP:
                posY-=velocidad
                if posY<100:
                    posY=100
            elif event.key == K_DOWN:
                posY+=velocidad
                if posY>(600-50):
                    posY=600-50       
    pygame.display.update()  