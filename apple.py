import pygame
from pygame.sprite import Sprite

from settings import RED
from settings import SIZE_APPLE
from settings import WIDTH_APPLE
from settings import HEIGHT_APPLE


class Apple(Sprite):
    
    def __init__(self, pos_x, pos_y):
        Sprite.__init__(self)
        
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = pygame.Surface(SIZE_APPLE, pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
        pygame.draw.circle(self.image, RED, (10, 10), WIDTH_APPLE // 2)
        
        self.visible = True
        
    
    def draw(self, surface):
        
        surface.blit(self.image, self.rect)
    