import pygame

pygame.init()

ecran = pygame.display.set_mode((1250, 650))

pygame.display.set_caption("PyJeux")

continuer = True

fond = pygame.image.load("bg.jpg").convert()

ecran.blit(fond, (-10,-10))
pygame.display.flip()

perso = pygame.image.load("perso.png").convert_alpha()

ecran.blit(perso, (0,440))
pygame.display.flip()

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()