import random                #随机实数生成
import pygame                #导入pygame模块
from pygame.locals import *  #导入所有pygame常量
from sys import exit         #导入exit
PANEL_width = 1920
PANEL_highly = 1080
FONT_PX = 60                 #字体间距
pygame.init()                #初始化模块，安全第一，“安全，安全，还他妈的是安全”                           

#创建一个windows窗口
winSur = pygame.display.set_mode((PANEL_width, PANEL_highly),FULLSCREEN,32)

font = pygame.font.SysFont("Bauhaus 93", 60)           #字体设置

bg_suface = pygame.Surface((PANEL_width, PANEL_highly), flags=pygame.SRCALPHA)  #surface设置

pygame.Surface.convert(bg_suface)       #修改图像（surface对象）的像素格式

bg_suface.fill(pygame.Color(255,255 , 255))                                #图层颜色

winSur.fill((255, 255, 255))
letter = ['Hello World!']

texts = [
    font.render(str(letter[0]), True, (25,161,175))     #字体颜色
    ]
column = int(PANEL_width / FONT_PX)
drops = [0 for i in range(column)]

while True:
    # 从队列中获取事件
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:       #添加按键关闭功能
            exit()
    # 将暂停一段给定的毫秒数
    pygame.time.delay(50)

    # 重新编辑图像第二个参数是坐上角坐标
    winSur.blit(bg_suface, (0, 0))

    for i in range(len(drops)):
        text = random.choice(texts)

        # 重新编辑每个坐标点的图像
        winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))

        drops[i] += 1
        if drops[i] * 10 > PANEL_highly or random.random() > 0.95:
            drops[i] = 0

    pygame.display.flip()
