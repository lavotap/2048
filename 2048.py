#-*-coding:utf-8-*-
# 游戏主程序

from gui.graph import *
from pygame.locals import *
import pygame
from sys import exit

from tools.game import Game
from gui.graph import Graph
from gui.lost import Lost
from gui.win import Win
from gui.welcome import Welcome

row=4# 行数
gb=Game(row,True)
gb.start_test()
gr=Graph(row)
gr.start_graph('2048')

we=Welcome(gr.screen)
we.get_welcome()

# 随机生成数和位置并初始化
n=gb.get_rand_num()
v=gb.get_rand_vector()
gb.change_num(v,n)
gr.background()
box=gb.get_box()
gr.playbox(box)
gr.flash()

win_number=2048

end=0# 结束因子，0为未结束，1为输，2为赢

while end==0 or end==2:
    d=None
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    exit()
                elif event.key==K_UP:
                    d='u'
                elif event.key==K_DOWN:
                    d='d'
                elif event.key==K_LEFT:
                    d='l'
                elif event.key==K_RIGHT:
                    d='r'

    if d:
        # 移动
        gb.move(d)
        gr.playbox(gb.get_box())
        gr.flash()
        n=gb.get_rand_num()
        v=gb.get_rand_vector()
        if v:
            gb.change_num(v,n)
        else:
            end=1

        max=gb.get_max()# 判断最大值
        # 赢时的画面
        if max==win_number and end==0:
            win=Win(gr.screen)
            win.get_win()
            end=2

    gr.playbox(gb.get_box())
    gr.flash()

# 输时的画面
if end==1:
    lost=Lost(gr.screen)
    lost.get_lost()

gb.end_test()
