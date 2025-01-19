import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.draw.rect(screen,(100,100,0),pygame.Rect(30,30,60,60))
    pygame.display.flip()