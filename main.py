import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    

    while running:
        log_state() #Start logging to game_state.jsonl
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")        
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(my_player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event('asteroid_shot')
                    shot.kill()
                    asteroid.split()
            


        for player in drawable:
            player.draw(screen)
            


        pygame.display.flip()
        
        # game_clock.tick(60)     # pause the game loop until 1/60th of a second has passed
        dt = (game_clock.tick(60)) /1000

        
        
        

if __name__ == "__main__":
    main()
