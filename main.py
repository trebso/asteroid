# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # 'Delta time' starts as 0 for now
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Shot.containers = (shots_group, updatable, drawable)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        shots_group.update()
        collisions = pygame.sprite.groupcollide(shots_group, asteroids, True, False)
        for asteroid in collisions.values():
            for a in asteroid:
                new_asteroids = a.split()
                asteroids.add(new_asteroids)
                a.kill()
        screen.fill((0,0,0))
        shots_group.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot is not None:
                shots_group.add(new_shot)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                sys.exit()

if __name__ == "__main__":
    main()
