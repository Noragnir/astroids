import pygame
from constants import *
from player import Player
def main():
    print ("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        screen.fill("black")
        milliseconds = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (milliseconds / 1000)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()