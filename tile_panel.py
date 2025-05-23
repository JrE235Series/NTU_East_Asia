import pygame
from settings import *

class Tile_Panel:
    def __init__(self, board_positions,tile_data,size=(window_width,window_height), 
                 position=(0,0)):

        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect(topleft=position)
        self.surface.fill((255, 255, 255))
        self.font = pygame.font.SysFont(None, 24)
        # 畫格子＋圖片或編號
        for idx, pos in enumerate(board_positions):
            rect = pygame.Rect(pos[0], pos[1], block_size,block_size)
            pygame.draw.rect(self.surface, (0, 0, 0), rect, 2)

            if idx in tile_data:
                img = pygame.image.load(tile_data[idx]["image"])
                img = pygame.transform.smoothscale(img, (block_size,block_size))
                self.surface.blit(img, (pos[0], pos[1]))
            else:
                text = self.font.render(str(idx), True, (0, 0, 0))
                self.surface.blit(text, (pos[0] + 5, pos[1] + 5))


    def frame_update(self , screen):
        
        screen.blit(self.surface, self.rect.topleft)
        


    