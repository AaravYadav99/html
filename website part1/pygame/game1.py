import pygame
pygame.init()
window=pygame.display.set_mode((400,400))
pygame.display.set_caption("My pygame window")
window.fill("red")
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()

