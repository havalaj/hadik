import pygame
import sys
from random import randrange
import keyboard
import pygame.locals
import time

if __name__ == "__main__":
    screen = pygame.display.set_mode((500, 800))

    for x in range(1, 5, 1):
        print(x)
        print("Jurko ")
    print("Ako sa mas ")

    # farba_pozadia = (randrange(255), randrange(255), randrange(255))
    farba_pozadia = (255, 255, 255)
    farba_hada = (0, 255, 0)
    farba_mnammnamu = (0, 0, 255)

    pocet = 15

    poloha_hada_x = randrange(15)
    poloha_hada_y = randrange(15)

    poloha_mnammnamu_x = randrange(15)
    poloha_mnammnamu_y = randrange(15)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    poloha_hada_y = poloha_hada_y - 1


            # if event.tty == pygame.K_w:
            #     print("aa")
            #     poloha_hada_y = poloha_hada_y - 1
        
        # pygame.draw.circle(screen, (255, 0, 0), (100, 300), 20)
        # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 30, 60, 60))

        zaciatok_x = 30
        zaciatok_y = 30    
        sirka_kocky = 30
        vyska_kocky = 40

        

        for y in range(0, pocet, 1):
            for x in range(0, pocet, 1):
                farba_kocky = farba_pozadia

                # nastavenie farby hada
                if (y == poloha_hada_y and x == poloha_hada_x):
                    farba_kocky = farba_hada

                # nastavenie farby mnammnamu
                if (y == poloha_mnammnamu_y and x == poloha_mnammnamu_x):
                    farba_kocky = farba_mnammnamu


                #vykreslenie kocky
                pygame.draw.rect(screen, farba_kocky, pygame.Rect(zaciatok_x + (sirka_kocky+1)*x, zaciatok_y + (vyska_kocky+1)*y, sirka_kocky, vyska_kocky))

        
        pygame.display.update()
