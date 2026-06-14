import pygame
pygame.init()
screen=pygame.display.set_mode((1280,720))
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
    screen.fill((50,180,50))
    pygame.display.flip()
pygame.quit()
