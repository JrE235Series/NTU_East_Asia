import pygame
import random
import webbrowser

import settings
import roll_dice

def main():
    pygame.init()
    
    # 畫面設定
    screen = pygame.display.set_mode((settings.window_width, settings.window_height))
    pygame.display.set_caption("大富翁電子版")

    font = pygame.font.SysFont(None, 24)  # 建立字型物件（小字）

    class Tile:
        def __init__(self, name, price=0, owner=None):
            self.name = name
            self.price = price
            self.owner = owner

    class Player:
        def __init__(self, name, color):
            self.name = name
            self.color = color
            self.money = 1500
            self.position = 0
            self.properties = []
    '''
    def roll_dice():
        return random.randint(1, 6)
    '''
    

    # 創建玩家
    player1 = Player("小明", (255, 0, 0))  # 紅色

    # 設定棋盤
    tile_size = settings.block_size  # 每格大小
    board_positions = []

    # 上邊 10 格 (0到9)
    for i in range(settings.row_count):
        board_positions.append((i * tile_size, 0))

    # 右邊 6 - 2格 (1到4)
    for i in range(1, (settings.column_count - 1)):
        board_positions.append(((settings.row_count - 1) * tile_size, i * tile_size))

    # 下邊 10格 (9到0)
    for i in range((settings.row_count - 1), -1, -1):
        board_positions.append((i * tile_size, (settings.column_count - 1) * tile_size))

    # 左邊 6 - 2 格 (4到1)
    for i in range((settings.column_count - 2), 0, -1):
        board_positions.append((0, i * tile_size))

    # 設定格子資料
    tile_data = {
        5: {"image": "./img/chopper.png", "link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
    }

    # 初始化骰子畫面
    dice_panel = roll_dice.Dice_Panel()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    steps = dice_panel.roll_dice(screen)
                    player1.position = (player1.position + steps) % len(board_positions)
                elif event.key == pygame.K_RETURN:
                    # 按下 Enter 鍵，檢查玩家目前站的格子有沒有連結
                    current_idx = player1.position
                    if current_idx in tile_data and "link" in tile_data[current_idx]:
                        webbrowser.open(tile_data[current_idx]["link"])

        screen.fill((255, 255, 255))

        # 畫格子＋圖片或編號
        for idx, pos in enumerate(board_positions):
            rect = pygame.Rect(pos[0], pos[1], tile_size, tile_size)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)

            if idx in tile_data:
                img = pygame.image.load(tile_data[idx]["image"])
                img = pygame.transform.scale(img, (tile_size, tile_size))
                screen.blit(img, (pos[0], pos[1]))
            else:
                text = font.render(str(idx), True, (0, 0, 0))
                screen.blit(text, (pos[0] + 5, pos[1] + 5))

        # 畫玩家
        player_pos = board_positions[player1.position]
        pygame.draw.circle(screen, player1.color, (player_pos[0] + tile_size // 2, player_pos[1] + tile_size // 2), 20)

        # 畫骰子
        dice_panel.frame_update(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    # this block runs only if the script is run directly
    main()

