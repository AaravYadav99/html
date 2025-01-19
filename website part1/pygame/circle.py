import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.draw.circle(screen,(100,100,0),[300,300],50,0)
        pygame.draw.circle(screen,(100,100,0),[100,100],50,3)
    pygame.display.flip()
