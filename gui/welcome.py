#-*-coding:utf-8-*-
# 欢迎画面

import pygame
from pygame.locals import *
from sys import exit
from pylib.vector import Vector

class Welcome(object):
    def __init__(self,surface):
        self.surface=surface

        self.backcolor=(127,255,0)
        self.welcomecolor=(138,43,226)

        self.w,self.h=self.surface.get_size()
        self.font=pygame.font.Font('./fonts/FRSCRIPT.TTF',int(self.h/2))
        self.welcomefont=pygame.font.Font('./fonts/COLONNA.TTF',int(self.h/4))

    def get_welcome(self):
        self.surface.fill(self.backcolor)
        welcome=self.font.render('2048',True,self.welcomecolor)
        answer=self.welcomefont.render('Start',True,self.welcomecolor)
        ww,wh=welcome.get_size()
        aw,ah=answer.get_size()
        wv=(self.w/2.0-ww/2.0,self.h/2-wh/2.0)
        av=(self.w-aw-10,self.h-ah-10)# 终点
        self.surface.blit(welcome,wv)
        pygame.display.update()
        pygame.image.save(self.surface,'./images/image_2048.png')
        image_2048=pygame.image.load('./images/image_2048.png').convert()
        sav=(self.w-aw-10,self.h)# 起点
        nav=sav# 下一步坐标
        dav=(0,-(ah+10)/500.0)# 每步差值
        while nav[1]>av[1]:
            nav=(nav[0]+dav[0],nav[1]+dav[1])
            self.surface.blit(image_2048,(0,0))
            self.surface.blit(answer,nav)
            pygame.display.update()
        self.surface.blit(answer,av)
        pygame.display.update()

        pygame.image.save(self.surface,'./images/welcome.png')
        welcome_image=pygame.image.load('./images/welcome.png').convert()

        pygame.mouse.set_visible(True)# 鼠标可见

        while True:
            self.surface.blit(welcome_image,(0,0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==QUIT:
                    exit()
                elif event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                            exit()
                elif event.type==MOUSEBUTTONDOWN:
                    mx,my=pygame.mouse.get_pos()
                    if mx>=av[0] and mx<=av[0]+aw and my>=av[1] and my<=av[1]+ah:
                        return True
