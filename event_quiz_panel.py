import pygame
from settings import *
import random
import button_tr_q
import button

class Quiz_Panel:
    def __init__(self, tile_num, size=(window_width, window_height), 
                 position=(0,0)):

        self.surface = pygame.Surface(size,pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=position)
        self.surface.fill((255, 255, 255))
        if (tile_num == 3):
            self.background_image = pygame.image.load('./event_img/3.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        
        if (tile_num == 11):
            self.background_image = pygame.image.load('./event_img/11.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        
        if (tile_num == 17):
            self.background_image = pygame.image.load('./event_img/17.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        
        if (tile_num == 20):
            self.background_image = pygame.image.load('./event_img/20.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        self.font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
        
        self.status = "No_ans" # "Correct" "Wrong"
        
        self.button = button.AnimatedButton(
            rect=(1200-200, 900-100, 200, 100),
            text="閉める",
            font=pygame.font.Font("./font/NotoSansJP_VariableFont_wght.ttf", 30),
            color_idle  = (206, 196, 174),
            color_hover = (230, 220, 200),  # lighter beige
            color_click = (180, 170, 150) 
        )
        self.buttonQ = []
        if (tile_num == 3):

            for i in range(4):
                self.buttonQ.append(button_tr_q.AnimatedButton(
                rect=(280, 405 + i*60, 550, 50),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)   # solid light gray on click
            ))
        
        if (tile_num == 11):

            for i in range(4):
                self.buttonQ.append(button_tr_q.AnimatedButton(
                rect=(150, 360 + i*60, 950, 50),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)   # solid light gray on click
            ))
        
        if (tile_num == 17):

            for i in range(4):
                self.buttonQ.append(button_tr_q.AnimatedButton(
                rect=(120, 360 + i*50, 900, 50),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)   # solid light gray on click
            ))
        
        if (tile_num == 20):

            for i in range(4):
                self.buttonQ.append(button_tr_q.AnimatedButton(
                rect=(70, 385 + i*53, 1080, 50),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)   # solid light gray on click
            ))
        


    def frame_update(self , screen, mouse_pos, mouse_pressed):
        
        
        self.surface.blit(self.background_image, (0, 0))
        self.button.update(mouse_pos, mouse_pressed,self.button.text)
        for i in range(4):

            self.buttonQ[i].update(mouse_pos, mouse_pressed)
        #self.surface.fill((255, 255, 255, 128),rect=pygame.Rect(0, 0, 200, 200))
        
        self.button.draw(self.surface)
        for i in range(4):
            self.buttonQ[i].draw(self.surface)
        screen.blit(self.surface, self.rect.topleft)