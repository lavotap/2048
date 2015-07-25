#-*-coding:utf-8-*-
# 图像程序

import pygame
from pygame.locals import *
from sys import exit
from pylib.vector import Vector
import math

class Graph(object):
    def __init__(self,row,):
        self.row=row

        self.screen_size=(640,420)# 屏幕尺寸
        self.box_size=400
        self.box_point=((self.screen_size[0]-self.box_size)/2.0,(self.screen_size[1]-self.box_size)/2.0)
        self.background_color=(200,200,200)# 背景颜色
        self.game_color=(255,200,100)# 游戏主题颜色
        self.line_color=(0,0,0)# 线的颜色
        self.line_width=5
        self.font_factory=0.5
        self.max_number_color=(65,105,225)

    def start_graph(self,name):
        pygame.init()
        self.screen=pygame.display.set_mode(self.screen_size,0,32)
        pygame.display.set_caption(name)
        self.font=pygame.font.Font('./fonts/AGENCYB.TTF',int(self.box_size*self.font_factory/self.row))
        self.max_number_font=pygame.font.Font('./fonts/calibrili.ttf',int(self.box_size*self.font_factory*2/(3*self.row)))
        pygame.mouse.set_visible(False)# 鼠标不可见

    def flash(self):
        pygame.display.update()

    def background(self):
        # 渲染出背景布局
        self.screen.fill(self.background_color)
        pygame.draw.rect(self.screen,self.game_color,Rect(self.box_point,(self.box_size,self.box_size)))
        pygame.draw.rect(self.screen,self.line_color,Rect(self.box_point,(self.box_size,self.box_size)),self.line_width)
        # 画出小方格
        for x in range(self.row-1):
            pygame.draw.line(self.screen,self.line_color,(self.box_point[0]+(x+1)*self.box_size/self.row,self.box_point[1]),(self.box_point[0]+(x+1)*self.box_size/self.row,self.box_point[1]+self.box_size),self.line_width)
        for y in range(self.row-1):
            pygame.draw.line(self.screen,self.line_color,(self.box_point[0],self.box_point[1]+(y+1)*self.box_size/self.row),(self.box_point[0]+self.box_size,self.box_point[1]+(y+1)*self.box_size/self.row),self.line_width)
        # max number
        max_number=self.max_number_font.render('Score:',True,self.max_number_color)
        self.max_x,self.max_y=max_number.get_size()
        self.screen.blit(max_number,(0,0))

        pygame.image.save(self.screen,'./images/screen_background.png')# 存储背景图片
        self.background_image=pygame.image.load('./images/screen_background.png').convert()


    def playbox(self,box):
        self.screen.blit(self.background_image,(0,0))
        #pygame.display.update()
        max_num=0# 最大数
        for j in range(self.row):
            for i in range(self.row):
                num=box[j][i]
                if num!=0:
                    # 获取最大值
                    if num>max_num:
                        max_num=num
                    # 获取数字颜色
                    n=math.log(int(num),2)
                    n=n%5
                    if n==0:
                        num_color=(127,0,0)
                    elif n==1:
                        num_color=(0,127,0)
                    elif n==2:
                        num_color=(0,0,127)
                    elif n==3:
                        num_color=(0,127,127)
                    elif n==4:
                        num_color=(127,127,0)
                    elif n==5:
                        num_color=(127,0,127)

                    font=self.font.render(str(num),True,num_color)
                    # 获取数字坐标
                    font_vector=Vector(self.box_point)+Vector(i*self.box_size/(self.row*1.0),j*self.box_size/(self.row*1.0))+Vector(self.box_size/(self.row*2.0),self.box_size/(self.row*2.0))-Vector(font.get_size())/2.0
                    self.screen.blit(font,(font_vector.x,font_vector.y))
                    # 渲染最大值
                    max_num_pic=self.max_number_font.render(str(max_num),True,self.max_number_color)
                    self.screen.blit(max_num_pic,(0,self.max_y+10))
