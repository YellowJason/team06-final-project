#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame as pg
import random
def main():
    #初始化
    pg.init()
    #建立視窗
    width,height = 450,700
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("下樓梯")        
    #建立畫面
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg_color_r = 200
    bg_color_g = 200
    bg.fill((bg_color_r,bg_color_g,0))
    #建立刺
    knife = pg.image.load('刺.png')
    knife2 = pg.image.load('刺2.png')
    knife.convert()
    knife2.convert()
    bg.blit(knife,(-5,675))
    bg.blit(knife2,(-5,-30))
    #建立血量
    heart = pg.image.load('愛心.png')
    heart.convert()
    blood = 3
    font = pg.font.SysFont("simhei",70)
    heart_font = font.render(f"X {blood}",True,(0,0,0),(bg_color_r,bg_color_g,0))
    #建立時間元件
    clock = pg.time.Clock()
    #樓梯list
    box_list = []
    #時間
    T = 0
    #起始速度
    speed = 3
    #樓梯
    class boxs:
        def __init__(self):
            self.x = random.randint(-70,380)
            self.y = 680
            self.width = random.randint(120,160)
            self.box = pg.Surface((self.width,20))#建立繪圖區
            self.box.fill((255,255,255))
            pg.draw.rect(self.box,(100,100,100),[0,0,self.width,20],30)#畫樓梯

        def draw(self):
            screen.blit(self.box,(self.x,self.y))

        def update(self):
            self.y -= speed
    #柴柴
    class kids:
        def __init__(self):
            self.picture = ['柴柴.png','柴柴2.png','柴柴3.png','柴柴4.png']
            self.x = box_list[0].x + 60
            self.y = 625
            self.up = False
            self.blood = blood
            self.kid = pg.image.load(self.picture[0])
            self.kid.convert()

        def draw(self):
            screen.blit(self.kid,(self.x,self.y))

        def change_picture(self):
            i = 3 - self.blood
            self.kid = pg.image.load(self.picture[i])
            self.kid.convert()

        def y_update(self):
            #確認是否在樓梯上
            self.up = False
            for i in box_list:
                if 40 < i.y - self.y < 60 and (i.x - 40) <= self.x <= (i.x + i.width -10):
                    self.up = True
            #垂直移動
            if self.up:
                self.y -= speed
            else:
                self.y += speed
            #是否超出邊界
            if self.y <= -10:
                self.blood -= 1
                self.y += 20
            elif self.y >= 680:
                self.y = 200
                self.blood -= 1

        def x_update(self):
            keys = pg.key.get_pressed()#按鍵dict
            #確認是否按方向鍵
            if keys[pg.K_LEFT] and keys[pg.K_RIGHT]:
                pass
            elif keys[pg.K_LEFT]:
                self.x -= speed
            elif keys[pg.K_RIGHT]:
                self.x += speed
            #確認是否跑出邊界
            if self.x <= -60:
                self.x = 390
            elif self.x >= 450:
                self.x = 0

    #建立第一個樓梯
    box = boxs()
    box_list.append(box)
    #建立柴柴
    kid = kids()
    #分數
    score = 0
    #程式運行
    running = True
    while running:
        #算時間
        T += 1
        #幀數
        clock.tick(60)
        #樓梯出現時間
        period = int(100/speed)
        #關閉程式
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        #新增樓梯        
        if T % period == 0:
            box = boxs()
            box_list.append(box)

        if kid.blood > 0:
            if speed <= 9:
                if T % 600 == 0:
                    speed += 1#加速
                    bg_color_r += 5#加深顏色
                    bg_color_g -= 20
                    bg.fill((bg_color_r,bg_color_g,0))
                    bg.blit(knife,(-5,675))
                    bg.blit(knife2,(-5,-30))

            screen.blit(bg,(0,0))#重繪視窗

            for i in box_list:#每個樓梯畫一次
                i.update()
                if i.y < 10:
                    box_list.remove(i)
                i.draw()

            kid.x_update()#更新柴柴座標
            kid.y_update()

            screen.blit(heart,(0,10))#畫愛心
            heart_font = font.render(f"X {kid.blood}",True,(0,0,0),(bg_color_r,bg_color_g,0))#顯示血量
            screen.blit(heart_font, (70,20))

            kid.change_picture()#確認圖片狀態
            kid.draw()#畫柴柴

            score = int(T / 60)
        else:
            x = (T // 15) % 4
            kid.kid = pg.image.load(kid.picture[x])
            kid.kid.convert()
            kid.draw()
            font = pg.font.SysFont("simhei",90)
            score_font = font.render(f"Score : {score}",True,(0,0,0),(bg_color_r,bg_color_g,0))
            screen.blit(score_font,(70,500))

        pg.display.update()#更新視窗