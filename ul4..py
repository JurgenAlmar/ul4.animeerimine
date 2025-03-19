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

# Siniste autode algpositsioonid ja kiirus (veel aeglasemad)
sinised_autod = [
    {"x": 150, "y": -f1_sinine.get_height(), "kiirus": 0.1},  # Väga aeglane auto
    {"x": 250, "y": -f1_sinine.get_height(), "kiirus": 0.15},  # Väga aeglane auto
    {"x": 350, "y": -f1_sinine.get_height(), "kiirus": 0.12}   # Väga aeglane auto
]

# Punase auto algpositsioon (ekraani all keskel)
posX_punane = (ekraani_laius - f1_punane.get_width()) // 2
posY_punane = ekraani_korgus - f1_punane.get_height()  # Punane auto ekraani all

gameover = False
while not gameover:
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            sys.exit()

    # Tausta värskendamine
    ekraan.fill((0, 0, 0))
    ekraan.blit(bg, (0, 0))

    # Liiguta iga sinine auto (veel aeglasemalt)
    for auto in sinised_autod:
        auto["y"] += auto["kiirus"]

        # Kui auto jõuab ekraani allserva, liigu tagasi üles
        if auto["y"] > ekraani_korgus:
            auto["y"] = -f1_sinine.get_height()

        # Joonista auto ekraanile
        ekraan.blit(f1_sinine, (auto["x"], auto["y"]))

    # Joonista punane auto, mis jääb ekraani all keskele
    ekraan.blit(f1_punane, (posX_punane, posY_punane))

    # Ekraani värskendamine
    pygame.display.update()
