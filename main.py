import pygame
import random

from settings import SIZE
from settings import WHITE

from settings import WIDTH, HEIGHT
from settings import WIDTH_APPLE
from settings import HEIGHT_APPLE

from apple import Apple
from player import Player

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Bootcamp CódigoFacilito')

game = True

player = Player(100, 100)
apples = pygame.sprite.Group()

print(dir(pygame.sprite.Group))

for _ in range(0, 10):
    pos_x = random.randint(0, WIDTH - WIDTH_APPLE)
    pos_y = random.randint(0, HEIGHT - HEIGHT_APPLE)
    
    apples.add( Apple(pos_x, pos_y) )

clock = pygame.time.Clock()

while game:
    clock.tick(60)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False
    
    
    key_pressed = pygame.key.get_pressed()
    
    if key_pressed[pygame.K_LEFT]:
        player.left()
        
    if key_pressed[pygame.K_RIGHT]:
        player.right()
        
    if key_pressed[pygame.K_UP]:
        player.up()
        
    if key_pressed[pygame.K_DOWN]:
        player.down()
    
    
    screen.fill(WHITE)
    
    player.draw(screen)
    
    for apple in apples:
        if pygame.sprite.collide_mask(player, apple) and apple.visible:
            apple.visible = False
            
            player.point()
            apples.remove(apple)
            
            
        apple.draw(screen)
    
    pygame.display.flip()