import pygame
pygame.init()
clock=pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('sprite goku')
sprite=pygame.Rect(375, 275, 50, 50)
color=(255, 0, 0)
velocity=5
running=True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sprite.x+=velocity
    if keys[pygame.K_LEFT]:
        sprite.x-=velocity    
    if keys[pygame.K_UP]:
        sprite.y-=velocity
    if keys[pygame.K_DOWN]:
        sprite.y+=velocity 

    if (sprite.left <= 0 or sprite.right >= WIDTH or
    sprite.top <= 0 or sprite.bottom >= HEIGHT):
        color = (0, 0, 255)
    else:
        color = (0, 255, 0)
    pygame.draw.rect(screen, color, sprite)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()                   