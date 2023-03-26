import pygame,sys

pygame.init()
screen =pygame.display.set_mode([640,480])
pygame.display.set_caption("按键测试")
bg_color= [255,255,255]
screen.fill(bg_color)
image = pygame.image.load("1.png")
rect = image.get_rect()
x=300
y=0

while True:
    y=y+0.2
    if y>480:
        y=-20
    print(rect.bottom)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(image,(x,y))
    pygame.display.flip()