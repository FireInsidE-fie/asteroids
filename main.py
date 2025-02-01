import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("[!] - Starting asteroids!")

    pygame.init()

    print(f"[!] - Screen width: {SCREEN_WIDTH}")
    print(f"[!] - Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid)
    Shot.containers = (updatable, drawable, shot)
    AsteroidField.containers = updatable

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        updatable.update(dt)
        for a in asteroid:
            if player.check_collision(a):
                print("Game over!")
                sys.exit()
            for s in shot:
                if a.check_collision(s):
                    s.kill()
                    a.kill()
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()