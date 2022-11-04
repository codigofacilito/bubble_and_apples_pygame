import pygame

from settings import WIDTH
from settings import HEIGHT
from settings import RANDOM
from settings import WIDTH_PLAYER
from settings import HEIGHT_PLAYER

from settings import UP, DOWN, LEFT, RIGHT

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.width = WIDTH_PLAYER
        self.height = HEIGHT_PLAYER 
        
        self.speed = 3
        self.direction = RIGHT
        self.apples = 0
        
        self.make_image()
        
    
    def make_image(self):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        
        pygame.draw.circle(self.image, RANDOM, self.rect.center,  (self.width // 2) - 1 )
    
    
    def draw(self, surface):
        self.move()
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
        surface.blit(self.image, self.rect)


    def move(self):
        self.validate_move()
        
        if self.direction == UP:
            self.pos_y -= self.speed
        
        elif self.direction == DOWN:
            self.pos_y += self.speed

        elif self.direction == RIGHT:
            self.pos_x += self.speed

        elif self.direction == LEFT:
            self.pos_x -= self.speed


    def validate_move(self):
        if self.pos_x <= 0:
            self.pos_x = 0

        if self.pos_x >= (WIDTH - WIDTH_PLAYER):
            self.pos_x = WIDTH - WIDTH_PLAYER
        
        if self.pos_y <= 0:
            self.pos_y = 0
            
        if self.pos_y >= (HEIGHT - HEIGHT_PLAYER):
            self.pos_y = HEIGHT - HEIGHT_PLAYER


    def up(self):
        self.direction = UP


    def down(self):
        self.direction = DOWN


    def left(self):
        self.direction = LEFT


    def right(self):
        self.direction = RIGHT
        
    
    def point(self):
        self.apples += 1
        
        self.width += 10
        self.height += 10
        
        self.make_image()