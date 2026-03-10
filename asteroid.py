from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color='white', center=self.position, radius=self.radius, width=LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return f"This was a small asteroid and we're done"
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_asteroid_velocity = self.velocity.rotate(angle)
            second_asteroid_velocity = self.velocity.rotate(-angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            small_asteroid_1 = Asteroid(*self.position, new_asteroid_radius )
            small_asteroid_2 = Asteroid(*self.position, new_asteroid_radius )
            small_asteroid_1.velocity = first_asteroid_velocity * 1.2
            small_asteroid_2.velocity = second_asteroid_velocity

        
