import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


VERSION = pygame.version.ver

def main():
    
    print(f'Starting Asteroids with pygame version: {VERSION}')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()   # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running = True

    game_clock = pygame.time.Clock()    # game_clock
    dt = 0
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        log_state() #Start logging to game_state.jsonl
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        my_player.draw(screen)

        pygame.display.flip()
        
        # game_clock.tick(60)     # pause the game loop until 1/60th of a second has passed
        dt = (game_clock.tick(60)) /1000
        
        

if __name__ == "__main__":
    main()
