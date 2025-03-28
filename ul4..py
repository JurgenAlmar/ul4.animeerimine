import pygame
import sys

pygame.init()

ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("ul4")

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

def game_over_menu():
    while True:
        ekraan.fill((0, 0, 0))
        tekst = font.render(f"Mäng lõppes! Sinu skoor: {skoor}", True, (255, 255, 255))
        restart_tekst = font.render("Vajuta Enter, et uuesti mängida", True, (255, 255, 255))
        mangulopp_tekst = font.render("Vajuta q nuppu et mäng lõppetada", True, (255, 255, 255))
        ekraan.blit(mangulopp_tekst, (150, 350  ))
        ekraan.blit(tekst, (ekraani_laius // 2 - 100, ekraani_korgus // 2 - 50))
        ekraan.blit(restart_tekst, (ekraani_laius // 2 - 150, ekraani_korgus // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def restart_game():
    global posX_punane, posY_punane, skoor, sinised_autod
    posX_punane = (ekraani_laius - f1_punane.get_width()) // 2
    posY_punane = ekraani_korgus - f1_punane.get_height()
    skoor = 0
    for auto in sinised_autod:
        auto["y"] = -f1_sinine.get_height()

gameover = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
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

    punane_rect = pygame.Rect(posX_punane, posY_punane, f1_punane.get_width(), f1_punane.get_height())

    for auto in sinised_autod:
        auto["y"] += auto["kiirus"]
        if auto["y"] > ekraani_korgus:
            auto["y"] = -f1_sinine.get_height()
            skoor += 10
        ekraan.blit(img_with_flip, (auto["x"], auto["y"]))

        sinine_rect = pygame.Rect(auto["x"], auto["y"], f1_sinine.get_width(), f1_sinine.get_height())
        if punane_rect.colliderect(sinine_rect):
            game_over_menu()
            restart_game()

    ekraan.blit(f1_punane, (posX_punane, posY_punane))
    skoor_teksts = font.render(f"Skoor: {skoor}", True, (255, 255, 255))
    ekraan.blit(skoor_teksts, (10, 10))


    pygame.display.update()
