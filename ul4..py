import pygame
import sys

pygame.init()

ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Objektide_animeerimine")
bg = pygame.image.load("bg_rally.jpg")

posX, posY = 0, 0

gameover = False
while not gameover:
    #mängu sulgemine ristist
    events = pygame.event.get()
    for i in events:
       if i.type == pygame.QUIT:
           sys.exit()


    ekraan.fill((0, 0, 0))

    # Pildi joonistamine ekraanile
    ekraan.blit(bg, (posX, posY))

    # Ekraani värskendamine
    pygame.display.update()
