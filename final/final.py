#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame as pg
import jump
import guess
import guess2
import eating

def total():
    pg.init()
    #建立視窗
    width,height = 450,550
    screen2 = pg.display.set_mode((width, height))
    pg.display.set_caption("柴柴的奇幻冒險")
    #建立畫面
    bg_picture = pg.image.load('柴柴_背景.png')
    bg_picture.convert()
    title = pg.image.load('柴柴的奇幻冒險1.png')
    title.convert
    #顯示
    x = -100
    #建立時間元件
    clock = pg.time.Clock()
    T = 0
    
    file = 'jojo.mp3'
    pg.mixer.init()
    pg.mixer.music.load(file)
    pg.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.
    
    class button:
            def __init__(self,y,game,name):
                self.x = 110
                self.y = y
                self.width = 230
                self.color = (255,250,200)
                self.button = pg.Surface((self.width,50))#建立繪圖區
                self.button.fill(self.color)
                self.game = game
                self.name = name
                self.font = pg.font.SysFont("simhei", 40)
                self.word = self.font.render(self.name, True, (100,0,100),self.color)

            def draw(self):
                self.word = self.font.render(self.name, True, (100,0,100),self.color)
                self.button.blit(self.word,(10,15))
                screen2.blit(self.button,(self.x,self.y))

            def update(self):
                #確認滑鼠位置
                buttons = pg.mouse.get_pressed()
                location = pg.mouse.get_pos()

                if self.x <= location[0] <= self.x + 230 and self.y <= location[1] <= self.y + 50:
                    self.color = (255,200,200)
                    self.button.fill(self.color)
                    if buttons[0]:
                        self.game()
                        screen2 = pg.display.set_mode((width, height))
                        pg.display.set_caption("柴柴的奇幻冒險")
                else:
                    self.color = (255,255,200)
                    self.button.fill(self.color)

    button1 = button(240,jump.main,'Jumping!')
    button2 = button(310,guess2.main,'You Guess!')
    button3 = button(380,guess.main,'Chychy Guess!')
    button4 = button(450,eating.main,'Eating')

    running1 = True
    while running1:
        
        T += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running1 = False
        #移動背景
        x += 2
        if x >= 0:
            x = -100

        screen2.blit(bg_picture,(x,0))
        screen2.blit(title,(75,50))

        button1.update()
        button1.draw()
        button2.update()
        button2.draw()
        button3.update()
        button3.draw()
        button4.update()
        button4.draw()

        pg.display.update()
        pg.time.delay(10)

    pg.quit()


# In[2]:


total()

