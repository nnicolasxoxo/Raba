import sys
import pygame
from pygame.locals import * 

pygame.init()
pantalla= pygame.display.set_mode((1500,500))
pygame.display.set_caption ("Raba")

Blanco= (255,255,255)
Negro=(0,0,0)
rojo=(255,0,0)
azul=(0,0,255)
verde=(0,255,0)

pantalla.fill(Blanco)
rectangulo= pygame.draw.rect(pantalla,rojo, (100,50,100,50))
print(rectangulo)

line=pygame.draw.line(pantalla, verde, (100,104) , (199,104),1)
print(line)

circulo=pygame.draw.circle(pantalla,azul,(122,250), 20,0) #x,y,r,relleno
print(circulo)

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

