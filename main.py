import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


VERSION = pygame.version.ver

def main():
    
    print(f'Starting Asteroids with pygame version: {VERSION}')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()   # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running = True

    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("purple")

        pygame.display.flip()


if __name__ == "__main__":
    main()
