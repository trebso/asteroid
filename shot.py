import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

#class Shot(CircleShape):

#    def __init__(self, x, y):
 #       super().__init__(x, y, SHOT_RADIUS)
  #      self.velocity = pygame.Vector2(0,0)
#
 #   def update(self, dt=0):
  #      self.position.x += self.velocity.x
   #     self.position.y += self.velocity.y
    #    if hasattr(self, 'circle_pos'):
     #       self.circle_pos = pygame.Vector2(self.position.x, self.position.y)

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

        # Create standard pygame sprite attributes
        self.image = pygame.Surface((SHOT_RADIUS*2, SHOT_RADIUS*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)

        self.rect = self.image.get_rect()
        self.rect.center = (self.position.x, self.position.y)

    def update(self, dt=0):
        # Update position using the CircleShape position attribute
        self.position += self.velocity * dt

        # Keep rect in sync with position for pygame's drawing methods
        self.rect.center = (self.position.x, self.position.y)

    def draw(self, screen):
        # Custom draw method if CircleShape's draw isn't sufficient
        pygame.draw.circle(screen, "white", (int(self.rect.centerx), int(self.rect.centery)), SHOT_RADIUS)


#    def shoot(self):
        # Get the triangle points - the first point (a) is the tip
 #       triangle_points = self.triangle()
  #      tip_position = triangle_points[0]  # The forward point of the triangle
    
        # Create shot at the triangle's tip
   #     new_shot = Shot(tip_position.x, tip_position.y)
    
        # Create direction vector - forward direction
        # The Vector2(0, 1) needs to be rotated the same way as your player
    #    direction = pygame.Vector2(0, 1).rotate(self.rotation)
     #   new_shot.velocity = direction * PLAYER_SHOOT_SPEED
    
      #  return new_shot
