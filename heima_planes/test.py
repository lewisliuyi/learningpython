import pygame
from plane_sprites import *

pygame.init()
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1>加载图像数据
bg = pygame.image.load(
    r'D:\my_python\learningpython\heima_planes\images\background.png')
# 2> blit绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load(
    r"D:\my_python\learningpython\heima_planes\images\me1.png")
# 可以在所有绘制工作完成后
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite(
    r'D:\my_python\learningpython\heima_planes\images\enemy1.png')
enemy1 = GameSprite(
    r'D:\my_python\learningpython\heima_planes\images\enemy1.png', 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环意味着游戏的正式开始
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    # 捕获事件
    for event in pygame.event.get():

        # 判断事件类型
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()
    # 2修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的y值是否小于0
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 3 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update - 让组中的所有精灵更新位置
    enemy_group.update()
    # draw - 在screen对象上绘制所有的精灵
    enemy_group.draw(screen)
    # 4调用update方法更新显示
    pygame.display.update()

pygame.quit()
