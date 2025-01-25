import pygame
import random
pygame.init()
width=500
height=400
screen_res=(width,height)
colors=['blue','red','orange','yellow','green','black','brown']
bg_colors=['blue','red','orange','yellow','green','black','brown']
clr=random.choice(colors)
pygame.display.set_caption("Bouncing game")
screen=pygame.display.set_mode(screen_res)
red=(255,0,0)
black=(0,0,0)
x=100
y=100
rect_obj=pygame.draw.rect(screen,'Red',pygame.Rect(x,y,40,40))
speed=[-1,-1]
bg_color=black
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            exit()
    screen.fill(bg_color)
    rect_obj=rect_obj.move(speed)

    if rect_obj.left <=0 or rect_obj.right >=width:
        speed[0]= -speed[0]
        clr=random.choice(colors)
        bg_color=random.choice(bg_colors)
    if rect_obj.top <=0 or rect_obj.right >=height:
        speed[1]= -speed[1]
        clr=random.choice(colors)
        bg_color=random.choice(bg_colors)
    rect_obj=pygame.draw.rect(screen,clr,pygame.Rect(rect_obj.x,rect_obj.y,40,40))
    pygame.display.update()