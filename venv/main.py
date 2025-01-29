import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    print ("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids =pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        screen.fill("black")
        milliseconds = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (milliseconds / 1000)
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print ("Game Over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()