import pygame
from settings import *
import random
import button_tr
import settings
import asyncio

class Central_Panel:
    def __init__(self, size=(central_panel_width, central_panel_height), 
                 position=(central_panel_position[0], central_panel_position[1])):

        self.surface = pygame.Surface(size,pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=position)
        #self.surface.fill((255, 255, 255, 128))
        self.background_image = pygame.image.load('./img/main_bg.png')
        self.dice_overlay = pygame.Surface((200, 200), pygame.SRCALPHA)
        pygame.draw.rect(
            self.dice_overlay,
            (255, 255, 255, 63),  # RGBA: white, 25% transparent
            self.dice_overlay.get_rect(),
            border_radius=10      # Rounded corners radius
        )
        self.font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
        self.roll_message_rolling = self.font.render("Dice Rolling...", True, (255, 235, 193))
        self.roll_message_val = self.font.render("", True, (255, 235, 193))
        self.clock = pygame.time.Clock()
        self.demo_dice_index = 0
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
        
        self.rolling_aud = pygame.mixer.Sound('audio/roll_aud.ogg')
        self.rolling_stop_aud = pygame.mixer.Sound('audio/roll_stop_aud.ogg')

        self.is_rolling = False
        self.rolling_images_counter = 0
        self.dice_num_image = self.dice_images[0]
        self.first = True
        self.rand_num = 0

        self.button = button_tr.AnimatedButton(
            rect=(central_panel_width-300, 0, 300, 100),
            text="Click Me",
            font=pygame.font.SysFont(None, 36),
            color_idle=(0, 0, 0),  # unused, but required
            color_hover=(255, 255, 255),  # shown as semi-transparent white
            color_click=(200, 200, 200)   # solid light gray on click
        )
        self.dice_button = button_tr.AnimatedButton(
            rect=(0, 0, 200, 200),
            text="",
            font=pygame.font.SysFont(None, 36),
            color_idle=(0, 0, 0),  # unused, but required
            color_hover=(255, 255, 255),  # shown as semi-transparent white
            color_click=(200, 200, 200)   # solid light gray on click
        )


    def frame_update(self , screen, mouse_pos, mouse_pressed ,text):
        self.button.set_text(text)
        self.button.update(mouse_pos, mouse_pressed)
        self.dice_button.update(mouse_pos, mouse_pressed)
        self.surface.blit(self.background_image, (0, 0))
        #self.surface.fill((255, 255, 255, 128),rect=pygame.Rect(0, 0, 200, 200))
        self.surface.blit(self.dice_overlay,(0,0))
        self.dice_button.draw(self.surface)
        self.surface.blit(self.dice_images[self.rand_num], (50, 50))
        self.roll_message_val = self.font.render(str(self.rand_num + 1), True, (255, 235, 193))
        self.surface.blit(self.roll_message_val, (50, 530))
        self.button.draw(self.surface)
        screen.blit(self.surface, self.rect.topleft)
        


    async def roll_dice(self , screen):
        
        if  self.is_rolling is False:
            self.is_rolling = True
            self.rolling_aud.play()
            #self.rand_num = random.randint(0, 5)
            if (settings.mode == 27):
                self.rand_num = settings.demo_dice_val[(self.demo_dice_index%settings.demo_dice_count)]
                self.rand_num -= 1
                self.demo_dice_index += 1
            else:
                self.rand_num = random.randint(0, random.randint(0,5))
            dice_num_image = self.dice_images[self.rand_num]
            self.surface.blit(self.dice_rolling_images[self.rolling_images_counter], (50, 50))
            self.rolling_images_counter += 1
            self.first = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.surface.blit(self.background_image, (0, 0))
            self.surface.blit(self.dice_overlay,(0,0))
            self.button.draw(self.surface)
            #self.surface.fill((255, 255, 255, 128),rect=pygame.Rect(0, 0, 200, 200))
            self.surface.blit(self.roll_message_rolling, (50, 530))

            
            

            # start rolling and calculate dice num
            
            if self.is_rolling:
                # showing rolling animation images
                
                self.surface.blit(self.dice_rolling_images[self.rolling_images_counter], (50, 50))
                self.rolling_images_counter += 1
                if self.rolling_images_counter >= 8:
                    self.is_rolling = False
                    self.rolling_images_counter = 0

            else:
                
                self.surface.blit(dice_num_image, (50, 50))
                if self.first:
                    self.rolling_stop_aud.play()
                    self.first = False
                # show the dice which contains a number
            screen.blit(self.surface, self.rect.topleft)
            pygame.display.update()
            #self.clock.tick(13)
            if (not self.first):
                break
            await asyncio.sleep(1/16)
        return self.rand_num+1