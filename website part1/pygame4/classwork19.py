import pygame
pygame.init()
SWIDTH=500
SHIEGHT=400
screen=pygame.display.set_mode((SWIDTH,SHIEGHT))
mspeed=1
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image=pygame.Surface([w,h])
        self.image.fill(color)
        self.rect=self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x=max(min(self.rect.x + xchange,SWIDTH-self.rect.w),0)
        self.rect.y=max(min(self.rect.y + ychange,SHIEGHT-self.rect.h),0)
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()
sprite1=Sprite("red",20,20) 
sprite1.rect.x=340
sprite1.rect.y=340
all_sprites.add(sprite1)
sprite2=Sprite("blue",20,20) 
sprite2.rect.x=100
sprite2.rect.y=50
all_sprites.add(sprite2)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
    keys=pygame.key.get_pressed()
    xchange= (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*mspeed
    ychange= (keys[pygame.K_DOWN]-keys[pygame.K_UP])*mspeed
    if sprite1.rect.colliderect(sprite2.rect):
        all_sprites.remove(sprite2)
    sprite1.move(xchange,ychange)
    screen.fill("black")
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(90)