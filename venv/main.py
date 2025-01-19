import pygame
from constants import *
def main():
    print ("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill("black")
        pygame.display.flip()
        milliseconds = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (milliseconds / 1000)
if __name__ == "__main__":
    main()