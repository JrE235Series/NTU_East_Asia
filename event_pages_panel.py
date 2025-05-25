import pygame
from settings import *
import random
import button_tr_p
import button

class Pages_Panel:
    def __init__(self, tile_num, size=(window_width, window_height), 
                 position=(0,0)):

        self.surface = pygame.Surface(size,pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=position)
        self.surface.fill((255, 255, 255))
        self.pages = []
        self.current_page = 0
        self.page_count = 0
        self.button_link = None
        self.button_link_page = 0
        if (tile_num == 15):
            temp_image = pygame.image.load('./event_img/15_0.png')
            temp_image = pygame.transform.smoothscale(temp_image, (window_width, window_height))
            self.pages.append(temp_image)

            temp_image = pygame.image.load('./event_img/15_1.png')
            temp_image = pygame.transform.smoothscale(temp_image, (window_width, window_height))
            self.pages.append(temp_image)
            self.page_count = 2

            self.button_link = button_tr_p.AnimatedButton(
                rect=(640, 640, 530, 35),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(200, 200, 200),  # shown as semi-transparent white
                color_click=(150, 150, 150)
            )
            self.button_link_page = 1

        if (tile_num == 19):
            temp_image = pygame.image.load('./event_img/19_0.png')
            temp_image = pygame.transform.smoothscale(temp_image, (window_width, window_height))
            self.pages.append(temp_image)

            temp_image = pygame.image.load('./event_img/19_1.png')
            temp_image = pygame.transform.smoothscale(temp_image, (window_width, window_height))
            self.pages.append(temp_image)
            self.page_count = 2
            self.button_link = button_tr_p.AnimatedButton(
                rect=(420, 640, 750, 35),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(200, 200, 200),  # shown as semi-transparent white
                color_click=(150, 150, 150)
            )
            self.button_link_page = 1

        if (tile_num == 22):
            temp_image = pygame.image.load('./event_img/22_0.png')
            temp_image = pygame.transform.smoothscale(temp_image, (window_width, window_height))
            self.pages.append(temp_image)

            temp_image = pygame.image.load('./event_img/22_1.png')
            temp_image = pygame.transform.smoothscale(temp_image, (window_width, window_height))
            self.pages.append(temp_image)
            self.page_count = 2
            self.button_link = button_tr_p.AnimatedButton(
                rect=(440, 640, 730, 35),
                text="",
                font=pygame.font.SysFont(None, 36),
                color_idle=(0, 0, 0),  # unused, but required
                color_hover=(200, 200, 200),  # shown as semi-transparent white
                color_click=(150, 150, 150)
            )
            self.button_link_page = 1
        if (tile_num == 23):
            temp_image = pygame.image.load('./event_img/23_0.png')
            temp_image = pygame.transform.smoothscale(temp_image, (window_width, window_height))
            self.pages.append(temp_image)

            temp_image = pygame.image.load('./event_img/23_1.png')
            temp_image = pygame.transform.smoothscale(temp_image, (window_width, window_height))
            self.pages.append(temp_image)
            self.page_count = 2

        
        self.font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
        
        self.clock = pygame.time.Clock()
        self.button_msg = ""
        if (self.current_page < self.page_count - 1): self.button_msg = "次のページ"
        else: self.button_msg = "閉める"
        self.button = button.AnimatedButton(
            rect=(1200-200, 900-100, 200, 100),
            text=self.button_msg,
            font=pygame.font.Font("./font/NotoSansJP_VariableFont_wght.ttf", 30),
            color_idle  = (206, 196, 174),
            color_hover = (230, 220, 200),  # lighter beige
            color_click = (180, 170, 150) 
        )


    def frame_update(self , screen, mouse_pos, mouse_pressed):
        
        
        self.surface.blit(self.pages[self.current_page], (0, 0))
        self.button.update(mouse_pos, mouse_pressed,self.button_msg)
        #self.surface.fill((255, 255, 255, 128),rect=pygame.Rect(0, 0, 200, 200))
        
        self.button.draw(self.surface)
        if ((self.button_link is not None ) and self.button_link_page == self.current_page):
            self.button_link.update(mouse_pos, mouse_pressed)
            self.button_link.draw(self.surface)
        screen.blit(self.surface, self.rect.topleft)
    
    def flip_page(self):
        if (self.current_page >= self.page_count - 1) :return

        self.current_page += 1
        if (self.current_page < self.page_count - 1): self.button_msg = "次のページ"
        else: self.button_msg = "閉める"


