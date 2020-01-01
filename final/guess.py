#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import pygame as pg

def main():
    ansbase=[]
    guess = []
    #減小答案庫範圍
    def think(a,b):
        ref=[]
        for i in range(4):
            ref.append(guess[i])
        for i in range(len(ansbase)):
            target = ansbase[i]
            aa=0
            bb=0
            for j in range(4):
                for k in range(4):
                    if target[j]==ref[k]:
                        if j==k:
                            aa+=1
                        else:
                            bb+=1
            if aa!=a or bb!=b:
                ansbase[i]=[-1]
        c=ansbase.count([-1])

        for i in range(c):
            ansbase.remove([-1])

        if len(ansbase) == 1:
            return 1
        elif len(ansbase) == 0:
            return 2
        else:
            return 0
    
    #建立答案庫
    for i in range(10000):
        x = 10
        num_list = []
        for j in range(4):
            num_list.insert(0,i % x)
            i = i //x
        num_list_set = set(num_list)
        if len(num_list_set) == 4:
            ansbase.append(num_list)
        
    bingo = 0
    #建立視窗
    width,height = 560,300
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("猜數字")
    #建立畫面
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255,255,200))
    #建立時間元件
    clock = pg.time.Clock()
    #規則
    rule1 = 'Just give me the A,B value'
    rule2 = 'I will know what you\'re thinking!'
    q = '(having two or more same numbers are forbidden)'
    font = pg.font.SysFont("simhei", 40)
    font2 = pg.font.SysFont("simhei", 25)
    font3 = pg.font.SysFont("simhei", 70)
    guess_word = 'I guess ...'
    success_word = 'l know it! You\'re think...'
    lie_word = 'You\'re a liar'
    a = 'A:'
    b = 'B:'
    #寫規則
    show_rule1 = font.render(rule1, True, (100,100,0), (255,255,200))
    show_rule2 = font.render(rule2, True, (100,100,0), (255,255,200))
    show_q = font2.render(q, True, (100,100,0), (255,255,200))
    show_guess = font3.render(guess_word, True, (0,0,0), (255,255,200))
    show_a = font3.render(a, True, (0,0,0), (255,255,200))
    show_b = font3.render(b, True, (0,0,0), (255,255,200))
    show_success = font3.render(success_word, True, (0,0,0), (255,255,200))
    show_lie = font3.render(lie_word, True, (0,0,0), (255,255,200))
    hint = pg.image.load('提示.png')
    hint.convert()

    bg.blit(show_rule1,(100,20))
    bg.blit(show_rule2,(100,50))
    bg.blit(show_q,(100,80))
    bg.blit(show_guess,(20,120))
    bg.blit(show_a,(320,210))
    bg.blit(show_b,(430,210))
    bg.blit(hint,(310,140))
    #匯入柴柴圖
    picture1 = pg.image.load('柴柴_3.png')
    picture1.convert()
    picture2 = pg.image.load('柴柴_2.png')
    picture2.convert()
    #格子
    block_list = []
    class block:
        def __init__(self,x):
            self.x = x
            self.y = 190
            self.width = 60
            self.value = 0
            self.color = (240,240,240)
            self.color1 = (240,240,240)
            self.color2 = (255,200,200)
            self.font = pg.font.SysFont("simhei", 100)
            self.block = pg.Surface((self.width,80))#建立繪圖區
            self.block.fill((255,255,255))
            self.word = self.font.render(str(self.value), True, (100,0,100),self.color)

        def draw(self):
            self.word = self.font.render(str(self.value), True, (100,0,100),self.color)
            pg.draw.rect(self.block,self.color,[0,0,self.width,80],0)
            self.block.blit(self.word,(10,10))
            screen.blit(self.block,(self.x,self.y))

        def choose(self):
            self.color = self.color2
            self.word = self.font.render(str(self.value), True, (100,0,100),self.color)

        def un_choose(self):
            self.color = self.color1
            self.word = self.font.render(str(self.value), True, (100,0,100),self.color)

    for i in range(4):
        Block = block(20+80*i)
        block_list.append(Block)

    for i in range(2):
        Block = block(370+110*i)
        block_list.append(Block)

    T = 0#時間
    state = 1#現在狀態
    ready = False#是否確認AB值
    choose = 4#現在改的方塊
    #猜第一次
    randnum=random.randint(0,len(ansbase)-1)
    guess = ansbase[randnum]
    for i in range(4):
        block_list[i].value = guess[i]

    running = True
    while running:
        T += 1
        #關閉
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        #換臉
        bg.blit(picture2,(10,15))

        screen.blit(bg,(0,0))
        #正在猜
        if bingo == 0:
            #是否在輸入A、B值
            if ready == False:
                keys = pg.key.get_pressed()
                num_list = [pg.K_0,pg.K_1,pg.K_2,pg.K_3,pg.K_4]

                for i in range(len(num_list)):
                    if keys[num_list[i]]:
                        block_list[choose].value = i

                if keys[pg.K_LEFT]:
                    block_list[choose].un_choose()
                    choose = 4
                    block_list[choose].choose()

                if keys[pg.K_RIGHT]:
                    block_list[choose].un_choose()
                    choose = 5
                    block_list[choose].choose()

                if keys[pg.K_RETURN]:
                    block_list[choose].un_choose()
                    ready = True
                    pg.time.delay(500)

            else:                                                   
                a,b = block_list[4].value,block_list[5].value
                bingo = think(a,b)
                ready = False
                if bingo != 2:
                    randnum = random.randint(0,len(ansbase)-1)
                    guess = ansbase[randnum]
                    for i in range(4):
                        block_list[i].value = guess[i]

            for i in block_list:
                i.draw()
        #猜到後
        if bingo == 1:
            pg.draw.rect(bg,(255,255,200),[10,15,80,80],0)
            if T // 10 % 2 == 0:
                bg.blit(picture1,(10,15))
            else:
                bg.blit(picture2,(10,15))

            screen.blit(bg,(0,0))
            bg.blit(show_success,(20,120))
            screen.blit(bg,(0,0))
            for i in block_list:
                i.draw()
                
        #錯誤
        if bingo == 2:
            pg.draw.rect(bg,(255,255,200),[10,15,80,80],0)
            if T // 10 % 2 == 0:
                bg.blit(picture1,(10,15))
            else:
                bg.blit(picture2,(10,15))

            screen.blit(bg,(0,0))
            bg.blit(show_lie,(20,120))
            screen.blit(bg,(0,0))
            for i in block_list:
                i.draw()

        pg.display.update()
        pg.time.delay(50)