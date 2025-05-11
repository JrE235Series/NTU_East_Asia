import pygame
import settings
import random

class Dice_Panel:
    def __init__(self, size=(600, 400), position=(settings.block_size, settings.block_size)):

        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect(topleft=position)
        self.background_image = pygame.image.load('graphics/background2.png')
        self.font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
        self.roll_message_rolling = self.font.render("Dice Rolling...", True, (255, 235, 193))
        self.roll_message_val = self.font.render("", True, (255, 235, 193))
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

    def frame_update(self , screen):
        self.surface.blit(self.background_image, (0, 0))
        self.surface.blit(self.dice_images[self.rand_num], (250, 150))
        self.roll_message_val = self.font.render(str(self.rand_num + 1), True, (255, 235, 193))
        self.surface.blit(self.roll_message_val, (50, 300))
        screen.blit(self.surface, self.rect.topleft)


    def roll_dice(self , screen):
        
        if  self.is_rolling is False:
            self.is_rolling = True
            self.rolling_aud.play()
            self.rand_num = random.randint(0, 5)
            dice_num_image = self.dice_images[self.rand_num]
            self.surface.blit(self.dice_rolling_images[self.rolling_images_counter], (250, 150))
            self.rolling_images_counter += 1
            self.first = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.surface.blit(self.background_image, (0, 0))
            self.surface.blit(self.roll_message_rolling, (50, 300))

            
            

            # start rolling and calculate dice num
            
            if self.is_rolling:
                # showing rolling animation images
                self.surface.blit(self.dice_rolling_images[self.rolling_images_counter], (250, 150))
                self.rolling_images_counter += 1
                if self.rolling_images_counter >= 8:
                    self.is_rolling = False
                    self.rolling_images_counter = 0

            else:
                self.surface.blit(dice_num_image, (250, 150))
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