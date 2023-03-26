import pygame
import sys

# pygame是一个包，要将pygame初始化，让里面的类做好准备
pygame.init()

# 初始化
bg = (213, 1, 144)
speed = [-2, 1]
size = width, height = 600, 400

# 设置界面大小
screen = pygame.display.set_mode(size)
# 设置界面标题
pygame.display.set_caption("turtle play game")
# 加载图片
turtle = pygame.image.load("1.png")
# 确定图片位置
position = turtle.get_rect()

while True:
    # 可以使游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 移动图像
    position = position.move(speed)
    # 判断图像位置，使小乌龟不出边界
    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    print(position.bottom)
    # 加载背景
    screen.fill(bg)
    # 更新小乌龟的位置
    screen.blit(turtle, position)
    # 更新屏幕，双缓冲模式
    pygame.display.flip()
    # 延时
    pygame.time.delay(10)