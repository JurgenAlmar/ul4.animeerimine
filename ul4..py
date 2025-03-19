import pygame
import sys

pygame.init()

ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Objektide_animeerimine")
bg = pygame.image.load("bg_rally.jpg")
f1_sinine = pygame.image.load("f1_blue.png")
f1_punane = pygame.image.load("f1_red.png")

sinised_autod = [
    {"x": 150, "y": -f1_sinine.get_height(), "kiirus": 0.1},
    {"x": 250, "y": -f1_sinine.get_height(), "kiirus": 0.15},
    {"x": 350, "y": -f1_sinine.get_height(), "kiirus": 0.12}
]

posX_punane = (ekraani_laius - f1_punane.get_width()) // 2
posY_punane = ekraani_korgus - f1_punane.get_height()

skoor = 0
font = pygame.font.Font(None, 36)

punase_auto_kiirus = 0.5  # Muudetud liikumiskiirus aeglasemaks

gameover = False
while not gameover:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        posY_punane -= punase_auto_kiirus
    if keys[pygame.K_DOWN]:
        posY_punane += punase_auto_kiirus
    if keys[pygame.K_LEFT]:
        posX_punane -= punase_auto_kiirus
    if keys[pygame.K_RIGHT]:
        posX_punane += punase_auto_kiirus

    if posX_punane < 0:
        posX_punane = 0
    if posX_punane > ekraani_laius - f1_punane.get_width():
        posX_punane = ekraani_laius - f1_punane.get_width()
    if posY_punane < 0:
        posY_punane = 0
    if posY_punane > ekraani_korgus - f1_punane.get_height():
        posY_punane = ekraani_korgus - f1_punane.get_height()

    ekraan.fill((0, 0, 0))
    ekraan.blit(bg, (0, 0))

    for auto in sinised_autod:
        auto["y"] += auto["kiirus"]

        if auto["y"] > ekraani_korgus:
            auto["y"] = -f1_sinine.get_height()
            skoor += 10

        ekraan.blit(f1_sinine, (auto["x"], auto["y"]))

    ekraan.blit(f1_punane, (posX_punane, posY_punane))

    skoor_teksts = font.render("Skoor: " + str(skoor), True, (255, 255, 255))
    ekraan.blit(skoor_teksts, (10, 10))

    pygame.display.update()
