import pygame,sys,random
white=255,255,255
blue=0,0,200
score=0
pygame.init()
speed=[0,0]
index=0
x1=random.randint(0,500)
y1=0
x2=random.randint(0,500)
y2=-80
x3=random.randint(0,500)
y3=-160
x4=random.randint(0,500)
y4=-240
x5=random.randint(0,500)
y5=-300
x6=random.randint(0,500)
y6=-370

switch1=True

screen=pygame.display.set_mode((600,600))
myfont=pygame.font.Font(None,40)
mou1=pygame.image.load('1.png')
mou2=pygame.image.load('2.png')
mou3=pygame.image.load('3.png')
mou4=pygame.image.load('4.png')
mou5=pygame.image.load('5.png')
mou6=pygame.image.load('6.png')
background=pygame.image.load('floor.jpg')
list1=[mou1,mou2,mou3,mou4,mou5,mou6]

def print_text(font,x,y,text,color=(0,0,0)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))
def image_appear():
    example=random.choice(list1)
    screen.blit(example,(550,0))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()

    screen.blit(background,(0,0))
    print_text(myfont,0,0,'score:'+str(score))
    
    screen.blit(mou1,(x1,y1))
    screen.blit(mou2,(x2,y2))
    screen.blit(mou3,(x3,y3))
    screen.blit(mou4,(x4,y4))
    screen.blit(mou5,(x5,y5))
    screen.blit(mou6,(x6,y6))

    if switch1==True:
        image_appear()

    if y1 < 600:
        y1+=0.5
    else:
        y1+=0.5
        y1=-90
        x1=random.randint(0,500)
    if y2 < 600:
        y2+=0.5
    else:
        y2+=0.5
        y2=-180
        x2=random.randint(0,500)
    if y3 < 600:
        y3+=0.5
    else:
        y3+=0.5
        y3=-270
        x3=random.randint(0,500)
    if y4 < 600:
        y4+=0.5
    else:
        y4+=0.5
        y4=-360
        x4=random.randint(0,500)
    if y5 < 600:
        y5+=0.5
    else:
        y5+=0.5
        y5=-450
        x5=random.randint(0,500)
    if y6 < 600:
        y6+=0.5
    else:
        y6+=0.5
        y6=-540
        x6=random.randint(0,500)

    
    pygame.display.update()
image_appear()
