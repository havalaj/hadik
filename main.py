import pygame
import sys
from random import randrange

if __name__ == "__main__":
    screen = pygame.display.set_mode((500, 800))

    for x in range(1, 5, 1):
        print(x)
        print("Jurko ")
    print("Ako sa mas ")

    farba = (randrange(255), randrange(255), randrange(255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # pygame.draw.circle(screen, (255, 0, 0), (100, 300), 20)
        # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 30, 60, 60))

        zaciatok_x =30
        zaciatok_y = 30    
        sirka = 30
        vyska = 40

        pocet = 15


        for y in range(0, pocet, 1):
            for x in range(0, pocet, 1):
                pygame.draw.rect(screen, farba, pygame.Rect(zaciatok_x + (sirka+1)*x, zaciatok_y + (vyska+1)*y, sirka, vyska))

        pygame.display.update()
