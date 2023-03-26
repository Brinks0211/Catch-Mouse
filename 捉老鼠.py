import pygame
import sys
import random
import itertools
import math


score=0
total=0
mouse_data=[]
switch=1

pygame.init()
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen=pygame.display.set_mode((600,700))
pygame.display.set_caption('捉老鼠')
font1=pygame.font.Font(r'C:\Windows\Fonts\msyh.ttc',20)
floor=pygame.image.load('floor.jpg').convert_alpha()

#写入路径
file=open('mice.txt','rb')
mouse_data1=file.readlines()
for i in mouse_data1:
    mouse_data.append(i.strip())

#创建老鼠类
class Mouse():
    #随机分配老鼠初始位置
    def __init__(self,path):
        self.x=random.randint(0,550)
        self.y=random.randint(-700,-400)
        self.mouse=pygame.image.load(path)
        self.position=self.mouse.get_rect()

        #pic=pygame.image.load(path)
        #position=pic.get_rect()
        #position=position.move([100,0])
        #screen.blit(pic,position)

    #老鼠上下循环
    def loop(self):
        screen.blit(self.mouse,(self.x,self.y))
        self.y+=0.3
        if self.y>700:
            self.x=random.randint(0,550)
            self.y=random.randint(-700,-400)

    #检测碰撞
    def collide(self, pos_x, pos_y):
        global score
        global switch
        if self.x<pos_x<self.x+60 and self.y<pos_y<self.y+60:
            score = score + 10
            switch=1
            self.y=800
        # if self.mouse.get_rect().collidepoint(pos_x,pos_y):
        #     score=score+10
        #     switch=1

#字体打印               
def print_text(font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))

#print(mouse_data)测试

#创建实例
mouse1=Mouse(mouse_data[0])
mouse2=Mouse(mouse_data[1])
mouse3=Mouse(mouse_data[2])
mouse4=Mouse(mouse_data[3])
mouse5=Mouse(mouse_data[4])
mouse6=Mouse(mouse_data[5])
list1=[mouse1,mouse2,mouse3,mouse4,mouse5,mouse6]

#选出一只老鼠
def selcetmouse(a):
    selection=random.choice(a)
    return selection

while True:
    #加载背景
    screen.blit(floor,(0,0))
    #图例运动
    mouse1.loop()
    mouse2.loop()
    mouse3.loop()
    mouse4.loop()
    mouse5.loop()
    mouse6.loop()

#呈现一只老鼠
    if switch==1:
        reference=selcetmouse(list1)
        switch=0
    screen.blit(reference.mouse,(550,0))

    # print(reference.left)

    #解决图像重叠问题
    for i in range(0,5):
        for j in range(0,6):
            if i <=j and j<=4:
                j+=1
            else:
                continue

            line= math.sqrt(int((list1[i].x-list1[j].x)*(list1[i].x-list1[j].x)+(list1[i].y-list1[j].y)*(list1[i].y-list1[j].y)))
            if line<250:
                list1[j].x=random.randint(0,550)
                list1[j].y=random.randint(-400,-100)

    #程序交互
    for event in pygame.event.get() :
        if event.type==pygame.QUIT:
            sys.exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            image_x,image_y=pygame.mouse.get_pos()
            # print(image_y,image_x)
            # print(reference.position)
            reference.collide(image_x,image_y)
            # if reference.position2.left<image_x<reference.position2.right and reference.position2.bottom<image_y<reference.position2.top:
            #     score=score+10
            #     switch=1

    print_text(font1,0,0,'得分：'+str(score))
    print_text(font1,480,18,"抓住他：")
    pygame.display.update()
