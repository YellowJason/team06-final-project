#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pygame as pg
import random
def main():
    pg.init()
    #建立視窗
    width,height = 600,600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("貪吃柴柴")        
    #建立畫面
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255,255,200))

    screen.blit(bg, (0,0))
    pg.display.update()
    #碰撞偵測
    def collide(a,b):
        if a.x - 20 < b.x < a.x + 20:
            if a.y - 20 < b.y < a.y + 20:
                return False
            else:
                return True
        else:
            return True

    class body:
        def __init__(self,x,n):
            self.x = x
            self.y = 300
            self.width = 30
            self.body = pg.Surface((self.width,self.width))#建立繪圖區
            self.body.fill((255,255,200))
            if n == 1:
                self.picture = pg.image.load('柴柴l.png')
            elif n == 2:
                self.picture = pg.image.load('身體.png')
            elif n == 3:
                self.picture = pg.image.load('尾巴l.png')
            self.picture.convert()
            self.direction = 'L'
            self.speed = 2
            self.t_direction = 'L'

        def draw(self):
            screen.blit(self.body,(self.x,self.y))
            self.body.fill((255,255,200))
            self.body.blit(self.picture,(0,0))

        def turn(self):
            keys = pg.key.get_pressed()#按鍵dict
            #確認是否按方向鍵
            if keys[pg.K_LEFT]:
                self.t_direction = 'L'
                self.picture = pg.image.load('柴柴l.png')
                self.picture.convert()
            elif keys[pg.K_RIGHT]:
                self.t_direction = 'R'
                self.picture = pg.image.load('柴柴r.png')
                self.picture.convert()
            elif keys[pg.K_DOWN]:
                self.t_direction = 'D'
                self.picture = pg.image.load('柴柴d.png')
                self.picture.convert()
            elif keys[pg.K_UP]:
                self.t_direction = 'U'
                self.picture = pg.image.load('柴柴u.png')
                self.picture.convert()

        def update(self):
            #確認是否跑出邊界
            if self.x <= -30:
                self.x = 570
            elif self.x >= 600:
                self.x = 0
            if self.y <= -30:
                self.y = 570
            elif self.y >= 600:
                self.y = 0
            #移動
            if self.direction == 'L':
                self.x -= self.speed
            elif self.direction == 'R':
                self.x += self.speed
            elif self.direction == 'U':
                self.y -= self.speed
            elif self.direction == 'D':
                self.y += self.speed

        def change(self):
            if self.direction == 'L':
                self.picture = pg.image.load('尾巴l.png')
                self.picture.convert()
            elif self.direction == 'R':
                self.picture = pg.image.load('尾巴r.png')
                self.picture.convert()
            elif self.direction == 'U':
                self.picture = pg.image.load('尾巴u.png')
                self.picture.convert()
            elif self.direction == 'D':
                self.picture = pg.image.load('尾巴d.png')
                self.picture.convert()

    class food:
        def __init__(self):
            self.x = random.randint(0,19)*30
            self.y = random.randint(0,19)*30
            self.picture = pg.image.load('狗骨頭.png')
            self.picture.convert()
            self.exist = True

        def draw(self):
            screen.blit(self.picture,(self.x,self.y))

        def update(self):
            self.exist = collide(self,body_list[0])

    #建立頭
    body_list = []
    head = body(300,1)
    body_list.append(head)
    t = 0
    #兩節身體
    for i in range(2):
        xx = 330+30*i
        body_list.append(body(xx,2))
    #食物list
    food_list = []
    #哭哭柴柴
    picture0 = pg.image.load('柴柴00.png')
    picture1 = pg.image.load('柴柴11.png')
    picture2 = pg.image.load('柴柴22.png')
    picture3 = pg.image.load('柴柴33.png')
    cry = [picture0,picture1,picture2,picture3]
    for i in cry:
        i.convert()

    running = True
    alive = True
    while running:
        t += 1
        screen.blit(bg,(0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        if alive:
            #確認轉向
            body_list[0].turn()
            #座標更新
            if t % 15 == 0 and t != 0:
                for i in range(-1,-len(body_list),-1):
                    body_list[i].direction = body_list[i-1].direction
                #套用轉向
                body_list[0].direction = body_list[0].t_direction
            #尾巴換圖
            body_list[-1].change()

            for i in range(0,len(body_list)):
                body_list[i].update()
                body_list[i].draw()

            if t % 200 == 0:
                Food = food()
                food_list.append(Food)

            i = 0
            while i < len(food_list):
                food_list[i].update()
                if food_list[i].exist == True:
                    food_list[i].draw()
                    i += 1
                else:
                    #新增身體
                    newbody = body(300,2)
                    newbody.direction = body_list[-1].direction
                    if newbody.direction == 'L':
                        newbody.x = body_list[-1].x + 30
                        newbody.y = body_list[-1].y
                    if newbody.direction == 'R':
                        newbody.x = body_list[-1].x - 30
                        newbody.y = body_list[-1].y
                    if newbody.direction == 'U':
                        newbody.x = body_list[-1].x
                        newbody.y = body_list[-1].y + 30
                    if newbody.direction == 'D':
                        newbody.x = body_list[-1].x
                        newbody.y = body_list[-1].y - 30
                    #將原本的尾巴換成身體
                    body_list[-1].picture = pg.image.load('身體.png')
                    body_list[-1].picture.convert()
                    #加入新身體
                    body_list.append(newbody)
                    food_list.pop(i)
            #確認是否碰撞
            for i in range(2,len(body_list)):
                if_collide = collide(body_list[0],body_list[i])
                if if_collide == False:
                    alive = False
        else:
            #畫身體
            for i in range(0,len(body_list)):
                body_list[i].draw()
            #畫哭臉
            now = t // 20 % 4
            screen.blit(cry[now],(100,30))
            #顯示分數
            score = len(body_list) - 3
            font = pg.font.SysFont("simhei",90)
            score_str = font.render(f'Your weight : {score}kg',True,(0,0,0),(255,255,200))
            screen.blit(score_str,(40,450))

        pg.display.update()

        pg.time.delay(10)