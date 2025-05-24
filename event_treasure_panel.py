import pygame
from settings import *
import random
import button_tr
import button

class Treasure_Panel:
    def __init__(self, tile_num, size=(window_width, window_height), 
                 position=(0,0)):

        self.surface = pygame.Surface(size,pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=position)
        self.surface.fill((255, 255, 255))
        if (tile_num == 2):
            self.background_image = pygame.image.load('./event_img/2.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        if (tile_num == 13):
            self.background_image = pygame.image.load('./event_img/13.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        self.font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
        self.roll_message_rolling = self.font.render("Dice Rolling...", True, (255, 235, 193))
        self.roll_message_val = self.font.render("", True, (255, 235, 193))
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
        screen.blit(self.surface, self.rect.topleft)