import pygame
pygame.init()
window=pygame.display.set_mode((400,400))
pygame.display.set_caption("Image")
image=pygame.image.load("")
imgsize=(400,300)
image=pygame.transform.scale(image,imgsize)

pos=(0,0)
window.fill("red")
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()

