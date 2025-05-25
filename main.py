import pygame
import random
import webbrowser
import argparse
import asyncio

from settings import *
from button import *
from event import *
import roll_dice
import central_panel
import tile_panel

status_list = {"Wait For Dice Roll":1, "Dice Rolling":2 , "Event Wait Trigger":3 , "Event Trigger":4 , "Sudo":99}

def check_winner(player_list):
    for player in player_list:
        if player is None : continue
        if (player.position >= 24): return player.id
    return -1

def choose_next_player(cur , count , player_list):
    for player in player_list:
        if player is None : continue
        if (player.position >= 24): 
            print(player.id,player.name,"Won the game!")
    
    if (count == 1): return 1
    # deal with locks
    back_to_country= True
    for player in player_list:
        if player is None : continue
        if player.position < 16:
            back_to_country= False
            break
    #print(back_to_country)
    for player in player_list:
        if player is None : continue
        if (back_to_country) and player.lock:
            player.lock = False
    next = ((cur) % count) + 1
    print("Org next is",next)
    while (player_list[next].lock is True):
        next = ((next) % count) + 1
    print("Final next is",next)
    return next

async def main():

    parser = argparse.ArgumentParser()

    # Positional argument with default = None if omitted
    parser.add_argument("mode", nargs="?", default="normal", help="Run mode: 'demo' or 'normal'")

    args = parser.parse_args()
    #args.mode = "demo"
    if args.mode == "demo":
        print("Running in DEMO mode")
        # your demo behavior here
        settings.mode = 27 # demo mode
    else:
        print("Running in NORMAL mode")
        # your normal behavior here
        settings.mode = 1

    

    pygame.init()
    
    
    global_status = "Wait For Dice Roll"
    screen_status = 100
    # 畫面設定
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Monopoly NTU_EA Group 2")

    font = pygame.font.SysFont(None, 24)  # 建立字型物件（小字）

    class Tile:
        def __init__(self, name, price=0, owner=None):
            self.name = name
            self.price = price
            self.owner = owner

    class Player:
        def __init__(self,id, name, color,img_file):
            self.id = id
            self.name = name
            self.color = color
            self.money = 1500
            self.position = 1
            self.properties = []
            self.path = []
            self.has_treasure = False
            self.triggered = False
            self.lock = False
            self.img = pygame.image.load(img_file)
            if (settings.mode == 27):
                self.img = pygame.transform.smoothscale(self.img, player_size_1)
            else:
                self.img = pygame.transform.smoothscale(self.img, player_size_4)
            if (settings.mode == 27):
                self.relx = 0
                self.rely = 0
            else:
                if (id == 1):
                    self.relx = 0
                    self.rely = 5
                elif (id == 2):
                    self.relx = settings.player_space_x
                    self.rely = 5
                elif (id == 3):
                    self.relx = 0
                    self.rely= settings.player_space_y - 5
                elif (id == 4):
                    self.relx = settings.player_space_x
                    self.rely= settings.player_space_y - 5
    '''
    def roll_dice():
        return random.randint(1, 6)
    '''
    

    # 創建玩家
    player_list = []
    player_list.append(None)
    if (settings.mode == 27):
        player_count = 1
    else:
        player_count = 4
    #player1 = Player("P1", (255, 0, 0))  # 紅色
    for i in range(1,player_count+1):
        name = "P" + str(i)
        img_file = "./img/player"+str(i)+".png"
        
        player_list.append(Player(i,name, (255, 0, 0),img_file)) 
    # 設定棋盤
    tile_size = block_size  # 每格大小
    board_positions = []
    board_relative = []
    dismount = 10
    # 右邊 6 格 (0到6)
    for i in range(column_count):
        board_positions.append(((row_count - 1) * tile_size, (column_count - i) * tile_size))
        board_relative.append(((row_count - 1) * tile_size + dismount, (column_count - i) * tile_size))
    # 上邊 8 - 2 格 (7到12)
    for i in range(1,(row_count )):
        board_positions.append(((row_count - i ) * tile_size ,0))
        board_relative.append(((row_count - i ) * tile_size ,-dismount))
    # 左邊 6 格 (13到18)
    for i in range((column_count ), 0, -1):
        board_positions.append((0, (column_count - i) * tile_size)) 
        board_relative.append((0 - dismount, (column_count - i) * tile_size)) 
    for i in range(1, (row_count - 1 )):
        board_positions.append((i * tile_size, (column_count - 1)* tile_size))
        board_relative.append((i * tile_size, (column_count - 1)* tile_size + dismount))


    # 設定格子資料
    tile_data = {
        1: {"image": "./img/1.png"},
        2: {"image": "./img/2.png"},
        3: {"image": "./img/3.png"},
        4: {"image": "./img/4.png"},
        5: {"image": "./img/5.png"},
        6: {"image": "./img/6.png"},
        7: {"image": "./img/7.png"},
        8: {"image": "./img/8.png"},
        9: {"image": "./img/9.png"},
        10: {"image": "./img/10.png"},
        11: {"image": "./img/11.png"},
        12: {"image": "./img/12.png"},
        13: {"image": "./img/13.png"},
        14: {"image": "./img/14.png"},
        15: {"image": "./img/15.png"},
        16: {"image": "./img/16.png"},
        17: {"image": "./img/17.png"},
        18: {"image": "./img/18.png"},
        19: {"image": "./img/19.png"},
        20: {"image": "./img/20.png"},
        21: {"image": "./img/21.png"},
        22: {"image": "./img/22.png"},
        23: {"image": "./img/23.png"},
        24: {"image": "./img/24.png"},

    }

    # 初始化中央畫面
    g_central_panel = central_panel.Central_Panel()
    g_tile_panel = tile_panel.Tile_Panel(board_positions,tile_data)
    current_event_panel = None
    current_player = 1
    next_player = 1
    screen.fill((255, 255, 255))
    
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos_central = (mouse_pos[0] - central_panel_position[0], mouse_pos[1] - central_panel_position[1])
        mouse_pressed = pygame.mouse.get_pressed()
        event_list = pygame.event.get()

        if (screen_status == 100):
            '''
            i_temp = check_winner(player_list)
            if (i_temp  > 0):
                print(player_list[i_temp].name,"won the game")
            '''
            for event in event_list:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and global_status == "Wait For Dice Roll":
                        current_player = next_player
                        global_status = "Dice Rolling"
                        steps = await g_central_panel.roll_dice(screen)
                        
                        player_list[current_player].position = (player_list[current_player].position + steps) % len(board_positions) 
                        player_list[current_player].triggered = False
                        global_status = "Event Wait Trigger"
                        next_player = choose_next_player(current_player,player_count,player_list)

                    if event.key == pygame.K_UP:
                        player_list[current_player].position = (player_list[current_player].position + 1) % len(board_positions) 
                        player_list[current_player].triggered = False
                        global_status = "Event Wait Trigger"
                    if event.key == pygame.K_DOWN:
                        player_list[current_player].position = (player_list[current_player].position - 1) % len(board_positions) 
                        player_list[current_player].triggered = False
                        global_status = "Event Wait Trigger"    
                    if event.key == pygame.K_RETURN:
                        # 按下 Enter 鍵，檢查玩家目前站的格子有沒有連結
                        current_idx = player_list[current_player].position
                        if current_idx in tile_data and "link" in tile_data[current_idx]:
                            webbrowser.open(tile_data[current_idx]["link"])
                    if event.key == pygame.K_1:
                        print("Controlling Player 1")
                        current_player = 1
                        next_player = choose_next_player(current_player,player_count,player_list)
                    if event.key == pygame.K_2 and settings.mode != 27:
                        print("Controlling Player 2")
                        current_player = 2
                        next_player = choose_next_player(current_player,player_count,player_list)
                    if event.key == pygame.K_3 and settings.mode != 27:
                        print("Controlling Player 3")
                        current_player = 3
                        next_player = choose_next_player(current_player,player_count,player_list)
                    if event.key == pygame.K_4 and settings.mode != 27:
                        print("Controlling Player 4")
                        current_player = 4
                        next_player = choose_next_player(current_player,player_count,player_list)
                elif g_central_panel.button.is_clicked(mouse_pos_central, event_list) and (global_status == "Event Wait Trigger" or global_status == "Wait For Dice Roll"):
                    global_status = "Wait For Dice Roll"
                    
                    screen_status = player_list[current_player].position
                    print("Trigger Event",screen_status)
                    current_event_panel , screen_status = event_init(screen_status)
                elif g_central_panel.dice_button.is_clicked(mouse_pos_central, event_list) and global_status == "Wait For Dice Roll":
                    current_player = next_player
                    global_status = "Dice Rolling"
                    steps = await g_central_panel.roll_dice(screen)
                    
                    player_list[current_player].position = (player_list[current_player].position + steps) % len(board_positions) 
                    player_list[current_player].triggered = False
                    global_status = "Event Wait Trigger"
                    next_player = choose_next_player(current_player,player_count,player_list)

                    
            # 格子畫面更新
            g_tile_panel.frame_update(screen)
            
            # 中央畫面更新
            g_central_panel.frame_update(screen,mouse_pos_central, mouse_pressed,global_status)
            
            # （畫）玩家位置更新
            for i in range(1,player_count+1):

                player_pos = board_relative[player_list[i].position]
                target_pos = (player_pos[0] + player_list[i].relx, player_pos[1] + player_list[i].rely )
                
                #pygame.draw.circle(screen, player_list[current_player].color, (player_pos[0] + tile_size // 2, player_pos[1] + tile_size // 2), 20)
                screen.blit(player_list[i].img, target_pos)

        else:
            for event in event_list:
                if event.type == pygame.QUIT:
                    running = False
            await event_run(screen_status,current_event_panel,screen,mouse_pos, mouse_pressed,event_list)
            if event_button_close(screen_status,current_event_panel,mouse_pos, event_list):
                r_val = event_end(screen_status,player_list[current_player],current_event_panel)
                current_event_panel = None
                screen_status = 100
                if (r_val["TYPE"] == "Quiz" and not r_val["ANS"]):
                    global_status = "Event Wait Trigger"

                if (r_val["NPOS"] != player_list[current_player].position):
                    print(player_list[current_player].name,"Change Position to",r_val["NPOS"])
                    global_status = "Event Wait Trigger"
                player_list[current_player].position = r_val["NPOS"]
                next_player = choose_next_player(current_player,player_count,player_list)
        pygame.display.flip()
        await asyncio.sleep(0)




    pygame.quit()

if __name__ == "__main__":
    # this block runs only if the script is run directly
    asyncio.run(main())
