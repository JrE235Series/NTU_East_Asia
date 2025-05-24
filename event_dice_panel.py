import pygame
from settings import *
import random
import button_tr
import button

pos_dice = (550,720)
pos_message = (50,800)
class Dice_Panel:
    def __init__(self, tile_num, size=(window_width, window_height), 
                 position=(0,0)):

        self.surface = pygame.Surface(size,pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=position)
        self.surface.fill((255, 255, 255))
        if (tile_num == 8):
            self.background_image = pygame.image.load('./event_img/8.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        if (tile_num == 10):
            self.background_image = pygame.image.load('./event_img/10.png')
            self.background_image = pygame.transform.smoothscale(self.background_image, (window_width, window_height))
        
        
        self.font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
        self.roll_message_rolling = self.font.render("Dice Rolling...", True, (206, 196, 174))
        self.roll_message_val = self.font.render("", True, (206, 196, 174))
        self.clock = pygame.time.Clock()

        self.dice_images = []
        self.dice_rolling_images = []

        # since there are 6 dice images
        for num in range(1, 7):
            dice_image = pygame.image.load('graphics/dice/' + str(num) + '.png')
            self.dice_images.append(dice_image)

        # since there are 8 rolling dice images
        for num in range(1, 9):
            dice_rolling_image = pygame.image.load('graphics/animation/roll' + str(num) + '.png')
            self.dice_rolling_images.append(dice_rolling_image)
        
        self.rolling_aud = pygame.mixer.Sound('audio/roll_aud.mp3')
        self.rolling_stop_aud = pygame.mixer.Sound('audio/roll_stop_aud.mp3')

        self.is_rolling = False
        self.rolling_images_counter = 0
        self.dice_num_image = self.dice_images[0]
        self.first = True
        self.rand_num = 0
        self.final_num = 0
        self.diced = False
        self.button = button.AnimatedButton(
            rect=(1200-200, 900-100, 200, 100),
            text="閉める",
            font=pygame.font.Font("./font/NotoSansJP_VariableFont_wght.ttf", 30),
            color_idle  = (206, 196, 174),
            color_hover = (230, 220, 200),  # lighter beige
            color_click = (180, 170, 150) 
        )


    

    def frame_update(self , screen, mouse_pos, mouse_pressed):
        
        self.button.update(mouse_pos, mouse_pressed,self.button.text)
        self.surface.blit(self.background_image, (0, 0))
        
        self.surface.blit(self.dice_images[self.rand_num], pos_dice)
        if (self.diced):
            self.roll_message_val = self.font.render(str(self.rand_num + 1), True, (206, 196, 174))
            self.surface.blit(self.roll_message_val, (150,800))
        else:
            self.roll_message_val = self.font.render("Press Space to Roll", True, (206, 196, 174))
            self.surface.blit(self.roll_message_val, pos_message)
        self.button.draw(self.surface)
        screen.blit(self.surface, self.rect.topleft)
    
    def roll_dice(self , screen):
        if self.diced : return
        self.diced = True
        if  self.is_rolling is False:
            self.is_rolling = True
            self.rolling_aud.play()
            #self.rand_num = random.randint(0, 5)
            self.rand_num = random.randint(0, random.randint(0,5))
            self.final_num = self.rand_num + 1
            dice_num_image = self.dice_images[self.rand_num]
            self.surface.blit(self.dice_rolling_images[self.rolling_images_counter],pos_dice)
            self.rolling_images_counter += 1
            self.first = True
        while True:
           
            self.surface.blit(self.background_image, (0, 0))
            
            self.button.draw(self.surface)
            #self.surface.fill((255, 255, 255, 128),rect=pygame.Rect(0, 0, 200, 200))
            self.surface.blit(self.roll_message_rolling, pos_message)

            
            

            # start rolling and calculate dice num
            
            if self.is_rolling:
                # showing rolling animation images
                
                self.surface.blit(self.dice_rolling_images[self.rolling_images_counter], pos_dice)
                self.rolling_images_counter += 1
                if self.rolling_images_counter >= 8:
                    self.is_rolling = False
                    self.rolling_images_counter = 0

            else:
                
                self.surface.blit(dice_num_image, pos_dice)
                if self.first:
                    self.rolling_stop_aud.play()
                    self.first = False
                # show the dice which contains a number
            screen.blit(self.surface, self.rect.topleft)
            pygame.display.update()
            self.clock.tick(13)
            if (not self.first):
                break
        return self.rand_num+1