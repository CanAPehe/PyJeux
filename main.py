#Import
import pygame

pygame.init()

#Fenêtre du jeux
ecran = pygame.display.set_mode((1250, 650))

pygame.display.set_caption("PyJeux")


fond = pygame.image.load("bg.jpg").convert()

ecran.blit(fond, (-10,-10))
pygame.display.flip()

#Joueur
perso = pygame.image.load("perso.png").convert_alpha()

ecran.blit(perso, (0,440))
pygame.display.flip()

#Boucle
continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
