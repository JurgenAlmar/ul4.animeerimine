import pygame
import sys

pygame.init()


ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Objektide animeerimine")


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
punase_auto_kiirus = 0.5


skoor = 0
font = pygame.font.Font(None, 36)

f1_sinine_copy = f1_sinine.copy()

img_with_flip = pygame.transform.flip(f1_sinine_copy, True, True)

vasak_piir = 150
parem_piir = 500


gameover = False
while not gameover:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    keys = pygame.key.get_pressed()


    if keys[pygame.K_UP]:
        posY_punane -= punase_auto_kiirus
    if keys[pygame.K_DOWN]:
        posY_punane += punase_auto_kiirus
    if keys[pygame.K_LEFT]:
        posX_punane -= punase_auto_kiirus
    if keys[pygame.K_RIGHT]:
        posX_punane += punase_auto_kiirus


    if posX_punane < vasak_piir:
        posX_punane = vasak_piir
    if posX_punane > parem_piir - f1_punane.get_width():
        posX_punane = parem_piir - f1_punane.get_width()
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
        ekraan.blit(img_with_flip, (auto["x"], auto["y"]))





    ekraan.blit(f1_punane, (posX_punane, posY_punane))


    skoor_teksts = font.render(f"Skoor: {skoor}", True, (255, 255, 255))
    ekraan.blit(skoor_teksts, (10, 10))

    if skoor > 2000:
        gameover


    pygame.display.update()

pygame.quit()
sys.exit()
