#-*-coding:utf-8-*-
# 输时的图像

import pygame
from pygame.locals import *
from sys import exit
from pylib.vector import Vector

class Lost(object):
    def __init__(self,surface):
        self.surface=surface
        pygame.image.save(self.surface,'./images/lost.png')# 存储背景图片
        self.background_image=pygame.image.load('./images/lost.png').convert()
        self.backcolor=(127,127,127)
        self.lostcolor=(255,127,0)
        self.answercolor=(0,127,255)
        self.w,self.h=self.surface.get_size()
        self.font=pygame.font.Font('./fonts/comic.ttf',30)

    def get_lost(self):
        self.surface.blit(self.background_image,(0,0))
        vect=(self.w/2.0-150,self.h/2.0-80)
        w=300
        h=160
        pygame.draw.rect(self.surface,self.backcolor,Rect(vect,(w,h)))
        lost=self.font.render('You have lost!',True,self.lostcolor)
        answer=self.font.render(' OK ',True,self.answercolor)
        lw,lh=lost.get_size()
        aw,ah=answer.get_size()
        lv=(vect[0]+w/2.0-lw/2.0,vect[1]+10)
        av=(vect[0]+w/2.0-aw/2.0,vect[1]+20+lh)
        self.surface.blit(lost,lv)
        self.surface.blit(answer,av)
        pygame.image.save(self.surface,'./images/lost_game.png')
        lost_image=pygame.image.load('./images/lost_game.png').convert()

        pygame.mouse.set_visible(True)# 鼠标可见
        while True:
            self.surface.blit(lost_image,(0,0))
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
                        exit()
