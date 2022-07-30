import pygame
import os
width, Height = 900,500
Ventana= pygame.display.set_mode((width, Height))
pygame.display.set_caption("Raba")

Blanco= (255,255,255)
Negro= (0, 0, 0)
Red= (255, 255, 0)
yellow= (255, 255, 0)
Fotogramas=60

def main():
    clock= pygame.time.Clock()
    run = True

    while run:

        clock.tick(Fotogramas)

        for event in pygame.event.get():
           if event.type== pygame.Quit:
              run=False
              pygame.quit()
    main()
if __name__ == "__main__":
    main()


