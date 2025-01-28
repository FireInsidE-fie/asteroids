import pygame
from constants import *

def main():
    print("[!] - Starting asteroids!")
    pygame.init()
    print(f"[!] - Screen width: {SCREEN_WIDTH}")
    print(f"[!] - Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()