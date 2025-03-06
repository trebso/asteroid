import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.radius = radius

        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, surface):
#        if hasattr(self, 'position'):
 #           pos = self.position
  #      elif hasattr(self, 'pos'):
   #         pos = self.pos
    #    else:
     #       pos = pygame.Vector2(self.rect.centerx, self.rect.centery)
        pos = getattr(self, 'position', getattr(self, 'pos', pygame.Vector2(self.rect.centerx, self.rect.centery)))
        pygame.draw.circle(surface, (255,255,255), (int(pos.x), int(pos.y)), self.radius, 2)



    # Use pos.x and pos.y instead of self.x and self.y
        pygame.draw.circle(surface, (255,255,255), (int(pos.x), int(pos.y)), self.radius, 2)

    def update(self, dt):
        if hasattr(self, 'position'):
            self.position.x += self.velocity.x * dt
            self.position.y += self.velocity.y * dt
            self.rect.center = (self.position.x, self.position.y)
        elif hasattr(self, 'pos'):
            self.pos.x += self.velocity.x * dt
            self.pos.y += self.velocity.y * dt
            self.rect.center = (self.pos.x, self.pos.y)
        else:
            # If you're using self.rect for position
            self.rect.x += self.velocity.x * dt
            self.rect.y += self.velocity.y * dt

    def split(self):
        # Step 1: Kill itself first
        self.kill()
        
        # Step 2: If radius is too small, just return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        
        # Step 3: Generate random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Step 4: Create 2 new velocity vectors
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Step 5: Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Step 6: Get current position
        pos = getattr(self, 'position', getattr(self, 'pos', pygame.Vector2(self.rect.centerx, self.rect.centery)))
        
        # Step 7: Create two new asteroids
        asteroid1 = Asteroid(pos.x, pos.y, new_radius)
        asteroid2 = Asteroid(pos.x, pos.y, new_radius)
        
        # Step 8: Set velocities with increased speed
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2
        
        # Step 9: Return the new asteroids
        return [asteroid1, asteroid2]
