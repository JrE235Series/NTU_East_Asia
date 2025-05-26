import pygame
from settings import *
import random
import button_tr
import button
import button_tr_p

class Info_Panel:
    def __init__(self, tile_num, size=(window_width, window_height), 
                 position=(0,0)):

        self.surface = pygame.Surface(size,pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=position)
        self.surface.fill((255, 255, 255))
        self.video_button = None
        self.mag_button = None
        self.mag_button1 = None
        self.mag_button2 = None
        self.mag_button_l = None
        if (tile_num == 1):
            self.background_image = pygame.image.load('./event_img/1.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
            self.video_button = button_tr.AnimatedButton(
                rect=(100, 625, 185, 100),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)
            )
        if (tile_num == 4):
            self.background_image = pygame.image.load('./event_img/4.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
            self.video_button = button_tr.AnimatedButton(
                rect=(100, 625, 185, 100),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)
            )
        if (tile_num == 5):
            self.background_image = pygame.image.load('./event_img/5.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
            self.mag_button_l = button_tr_p.AnimatedButton(
                rect=(750, 715, 410, 35),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(200, 200, 200),  # shown as semi-transparent white
                color_click=(150, 150, 150)
            )

        if (tile_num == 6):
            self.background_image = pygame.image.load('./event_img/6.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
            self.video_button = button_tr.AnimatedButton(
                rect=(100, 625, 185, 100),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)
            )
            self.mag_button = button.AnimatedButton(
                rect=(0, 900-100, 200, 100),
                text="週刊",
                font=pygame.font.Font("./font/NotoSansJP_VariableFont_wght.ttf", 30),
                color_idle  = (206, 196, 174),
                color_hover = (230, 220, 200),  # lighter beige
                color_click = (180, 170, 150) 
            )
        if (tile_num == 7):
            self.background_image = pygame.image.load('./event_img/7.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
            self.mag_button_l = button_tr_p.AnimatedButton(
                rect=(675, 715, 485, 35),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(200, 200, 200),  # shown as semi-transparent white
                color_click=(150, 150, 150)
            )
        if (tile_num == 9):
            self.background_image = pygame.image.load('./event_img/9.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        if (tile_num == 12):
            self.background_image = pygame.image.load('./event_img/12.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
            self.video_button = button_tr.AnimatedButton(
                rect=(100, 625, 185, 100),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)
            )
            self.mag_button = button.AnimatedButton(
                rect=(0, 900-100, 200, 100),
                text="週刊",
                font=pygame.font.Font("./font/NotoSansJP_VariableFont_wght.ttf", 30),
                color_idle  = (206, 196, 174),
                color_hover = (230, 220, 200),  # lighter beige
                color_click = (180, 170, 150) 
            )
        if (tile_num == 14):
            self.background_image = pygame.image.load('./event_img/14.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        if (tile_num == 18):
            self.background_image = pygame.image.load('./event_img/18.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        if (tile_num == 21):
            self.background_image = pygame.image.load('./event_img/21.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
            self.video_button = button_tr.AnimatedButton(
                rect=(100, 625, 185, 100),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)
            )
            self.mag_button1 = button.AnimatedButton(
                rect=(0, 900-100, 200, 100),
                text="週刊一",
                font=pygame.font.Font("./font/NotoSansJP_VariableFont_wght.ttf", 30),
                color_idle  = (206, 196, 174),
                color_hover = (230, 220, 200),  # lighter beige
                color_click = (180, 170, 150) 
            )
            self.mag_button2 = button.AnimatedButton(
                rect=(205, 900-100, 200, 100),
                text="週刊二",
                font=pygame.font.Font("./font/NotoSansJP_VariableFont_wght.ttf", 30),
                color_idle  = (206, 196, 174),
                color_hover = (230, 220, 200),  # lighter beige
                color_click = (180, 170, 150) 
            )
        if (tile_num == 24):
            self.background_image = pygame.image.load('./event_img/24.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
            self.video_button = button_tr.AnimatedButton(
                rect=(100, 625, 185, 100),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(255, 255, 255),  # shown as semi-transparent white
                color_click=(200, 200, 200)
            )

            
        self.font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
        
        self.clock = pygame.time.Clock()

        
        
        self.button = button.AnimatedButton(
            rect=(1200-200, 900-100, 200, 100),
            text="閉める",
            font=pygame.font.Font("./font/NotoSansJP_VariableFont_wght.ttf", 30),
            color_idle  = (206, 196, 174),
            color_hover = (230, 220, 200),  # lighter beige
            color_click = (180, 170, 150) 
        )


    def frame_update(self , screen, mouse_pos, mouse_pressed):
        
        
        self.surface.blit(self.background_image, (0, 0))
        self.button.update(mouse_pos, mouse_pressed,self.button.text)
        #self.surface.fill((255, 255, 255, 128),rect=pygame.Rect(0, 0, 200, 200))
        
        self.button.draw(self.surface)
        
        if (self.video_button is not None):
            self.video_button.update(mouse_pos, mouse_pressed)
            self.video_button.draw(self.surface)
        if (self.mag_button is not None):
            self.mag_button.update(mouse_pos, mouse_pressed,self.mag_button.text)
            self.mag_button.draw(self.surface)
        
        if (self.mag_button1 is not None):
            self.mag_button1.update(mouse_pos, mouse_pressed,self.mag_button1.text)
            self.mag_button1.draw(self.surface)

        if (self.mag_button2 is not None):
            self.mag_button2.update(mouse_pos, mouse_pressed,self.mag_button2.text)
            self.mag_button2.draw(self.surface)
        
        if (self.mag_button_l is not None):
            self.mag_button_l.update(mouse_pos, mouse_pressed)
            self.mag_button_l.draw(self.surface)
        screen.blit(self.surface, self.rect.topleft)