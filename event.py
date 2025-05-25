import pygame 
import settings
import event_treasure_panel
import event_quiz_panel
import event_info_panel
import event_dice_panel
import event_pages_panel
import webbrowser
def event_init(tile_num):

    if tile_num == 1:
        print("Video [Link]")
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 2:
        treasure_panel = event_treasure_panel.Treasure_Panel(tile_num)
        return treasure_panel,tile_num
    if tile_num == 3:
        quiz_panle = event_quiz_panel.Quiz_Panel(tile_num)
        return quiz_panle,tile_num
    if tile_num == 4:
        print("Video [Link]")
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 5:
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 6:
        print("Video [Link]")
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 7:
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 8:
        dice_panel = event_dice_panel.Dice_Panel(tile_num)
        return dice_panel,tile_num
    if tile_num == 9:
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 10:
        dice_panel = event_dice_panel.Dice_Panel(tile_num)
        return dice_panel,tile_num
    if tile_num == 11:
        quiz_panle = event_quiz_panel.Quiz_Panel(tile_num)
        return quiz_panle,tile_num
    if tile_num == 12:
        print("Video [Link]")
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 13:
        treasure_panel = event_treasure_panel.Treasure_Panel(tile_num)
        return treasure_panel,tile_num
    if tile_num == 14:
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 15:
        pages_panel = event_pages_panel.Pages_Panel(tile_num)
        return pages_panel,tile_num
    if tile_num == 16:
        return None,100
    if tile_num == 17:
        quiz_panle = event_quiz_panel.Quiz_Panel(tile_num)
        return quiz_panle,tile_num
    if tile_num == 18:
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 19:
        pages_panel = event_pages_panel.Pages_Panel(tile_num)
        return pages_panel,tile_num
    if tile_num == 20:
        quiz_panle = event_quiz_panel.Quiz_Panel(tile_num)
        return quiz_panle,tile_num
    if tile_num == 21:
        print("Video [Link]")
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    if tile_num == 22:
        pages_panel = event_pages_panel.Pages_Panel(tile_num)
        return pages_panel,tile_num
    if tile_num == 23:
        pages_panel = event_pages_panel.Pages_Panel(tile_num)
        return pages_panel,tile_num
    if tile_num == 24:
        print("Video [Link]")
        info_panel = event_info_panel.Info_Panel(tile_num)
        return info_panel,tile_num
    else :return None,100

def event_run(tile_num,panel,screen,mouse_pos, mouse_pressed,event_list):

    if (tile_num == 1):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 2):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 3):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        #quiz
        for i in range(4):

            if (panel.buttonQ[i].is_clicked(mouse_pos, event_list)):
                if (i == 1):
                    panel.status = "Correct"
                    for j in range(4):
                        if (j == 1): 
                            panel.buttonQ[j].update_ans(True,False)
                        else:
                            panel.buttonQ[j].update_ans(False,False)
                else:
                    panel.status = "Wrong"
                    for j in range(4):
                        if (j == 1): 
                            panel.buttonQ[j].update_ans(True,False)
                        elif (j == i):
                            panel.buttonQ[j].update_ans(False,True)
                        else:
                            panel.buttonQ[j].update_ans(False,False)
    
    if (tile_num == 4):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 5):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 6):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 7):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 8):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        for event in event_list:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                panel.roll_dice(screen)
    if (tile_num == 9):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 10):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        for event in event_list:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                panel.roll_dice(screen)
    if (tile_num == 11):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        #quiz
        for i in range(4):

            if (panel.buttonQ[i].is_clicked(mouse_pos, event_list)):
                if (i == 1):
                    panel.status = "Correct"
                    for j in range(4):
                        if (j == 1): 
                            panel.buttonQ[j].update_ans(True,False)
                        else:
                            panel.buttonQ[j].update_ans(False,False)
                else:
                    panel.status = "Wrong"
                    for j in range(4):
                        if (j == 1): 
                            panel.buttonQ[j].update_ans(True,False)
                        elif (j == i):
                            panel.buttonQ[j].update_ans(False,True)
                        else:
                            panel.buttonQ[j].update_ans(False,False)

    if (tile_num == 12):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 13):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 14):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 15):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        if (panel.button_link.is_clicked(mouse_pos, event_list)):
            webbrowser.open(settings.magazine_link_m_p1)
    #16 pass
    if (tile_num == 17):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        #quiz
        for i in range(4):

            if (panel.buttonQ[i].is_clicked(mouse_pos, event_list)):
                if (i == 2):
                    panel.status = "Correct"
                    for j in range(4):
                        if (j == 2): 
                            panel.buttonQ[j].update_ans(True,False)
                        else:
                            panel.buttonQ[j].update_ans(False,False)
                else:
                    panel.status = "Wrong"
                    for j in range(4):
                        if (j == 2): 
                            panel.buttonQ[j].update_ans(True,False)
                        elif (j == i):
                            panel.buttonQ[j].update_ans(False,True)
                        else:
                            panel.buttonQ[j].update_ans(False,False)
    if (tile_num == 18):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 19):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        if (panel.button_link.is_clicked(mouse_pos, event_list)):
            webbrowser.open(settings.magazine_link_m_v2)
    if (tile_num == 20):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        #quiz
        for i in range(4):

            if (panel.buttonQ[i].is_clicked(mouse_pos, event_list)):
                if (i == 2):
                    panel.status = "Correct"
                    for j in range(4):
                        if (j == 2): 
                            panel.buttonQ[j].update_ans(True,False)
                        else:
                            panel.buttonQ[j].update_ans(False,False)
                else:
                    panel.status = "Wrong"
                    for j in range(4):
                        if (j == 2): 
                            panel.buttonQ[j].update_ans(True,False)
                        elif (j == i):
                            panel.buttonQ[j].update_ans(False,True)
                        else:
                            panel.buttonQ[j].update_ans(False,False)
    if (tile_num == 21):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 22):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
        if (panel.button_link.is_clicked(mouse_pos, event_list)):
            webbrowser.open(settings.magazine_link_m_v1)
    if (tile_num == 23):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
    if (tile_num == 24):
        panel.frame_update(screen,mouse_pos, mouse_pressed)
                            
def event_end(tile_num,player,panel):

    r_val = {"TYPE":"","ANS":None,"NPOS":player.position,"LOCK":False}
    if (tile_num == 2):
        if not player.triggered:
            print(player.name,"First Triggered Event Add Treasure",tile_num)
            player.has_treasure = True
            player.triggered = True
        else:
            print(player.name,"Already Triggered Event",tile_num)
        print("Event End",tile_num)
    
    if (tile_num == 3):
        r_val["TYPE"] = "Quiz"
        if (panel.status == "No_ans"): r_val["ANS"] = False
        else : 
            r_val["ANS"] = True
            if (panel.status == "Correct"): 
                r_val["NPOS"] = (player.position + 2)% settings.tile_count
        print("Quiz",tile_num,panel.status)
    
    if (tile_num == 5):
        
        if (player.has_treasure): 
            player.has_treasure = False
            r_val["NPOS"] = 16% settings.tile_count
            print(player.name,"has treasure, jump to 16")
        else : 
            print(player.name,"has no treasure, maintain")
    if (tile_num == 6):
        if (player.has_treasure): 
            player.has_treasure = False
            r_val["NPOS"] = 16% settings.tile_count
            print(player.name,"has treasure, jump to 16")
        else : 
            r_val["NPOS"] = (player.position -1)% settings.tile_count
            print(player.name,"has no treasure, jump -1")  
    if (tile_num == 7):
        r_val["NPOS"] = 16% settings.tile_count
    
    if (tile_num == 8):
        if (panel.final_num <= 5):
            r_val["NPOS"] = 1
        else:
            r_val["NPOS"] = 16
    if (tile_num == 9):
        if (settings.mode == 27):
            r_val["NPOS"] = player.position
            print("Demo mode no move")
        else:
            r_val["NPOS"] = 16% settings.tile_count
            player.lock = True
            print(player.name,"is locked at 16")
            r_val["LOCK"] = True
    if (tile_num == 10):
        if (1 <= panel.final_num <= 3):
            r_val["NPOS"] = (player.position - 1) % settings.tile_count
        elif (4 <= panel.final_num <= 5):
            r_val["NPOS"] = (player.position + 1) % settings.tile_count
        else:
            r_val["NPOS"] = (player.position + 3) % settings.tile_count
    if (tile_num == 11):
        r_val["TYPE"] = "Quiz"
        if (panel.status == "No_ans"): r_val["ANS"] = False
        else : 
            r_val["ANS"] = True
            if (panel.status == "Correct"): 
                r_val["NPOS"] = (player.position + 2)% settings.tile_count
        print("Quiz",tile_num,panel.status)
    if (tile_num == 12):
        if (settings.mode == 27):
            r_val["NPOS"] = player.position
            print("Demo mode no move")
        else:
            r_val["NPOS"] = (player.position - 1)% settings.tile_count
    if (tile_num == 13):
        if not player.triggered:
            print(player.name,"First Triggered Event Add Treasure",tile_num)
            player.has_treasure = True
            player.triggered = True
        else:
            print(player.name,"Already Triggered Event",tile_num)
        print("Event End",tile_num)
    if (tile_num == 14):
        r_val["NPOS"] = 16% settings.tile_count
        player.lock = True
        print(player.name,"is locked at 16")
        r_val["LOCK"] = True
    if (tile_num == 15):
        pass
    #16 pass
    if (tile_num == 17):
        r_val["TYPE"] = "Quiz"
        if (panel.status == "No_ans"): r_val["ANS"] = False
        else : 
            r_val["ANS"] = True
            if (panel.status == "Correct"): 
                r_val["NPOS"] = (player.position + 2)% settings.tile_count
        print("Quiz",tile_num,panel.status)
    if (tile_num == 18):
        if (player.has_treasure): 
            player.has_treasure = False
            r_val["NPOS"] = player.position
            print(player.name,"has treasure, maintain")
        else : 
            r_val["NPOS"] = (player.position -1)% settings.tile_count
            print(player.name,"has no treasure, jump -1")  
    if (tile_num == 19):
        pass
    if (tile_num == 20):
        r_val["TYPE"] = "Quiz"
        if (panel.status == "No_ans"): r_val["ANS"] = False
        else : 
            r_val["ANS"] = True
            if (panel.status == "Correct"): 
                r_val["NPOS"] = (player.position + 2)% settings.tile_count
        print("Quiz",tile_num,panel.status)
    if (tile_num == 21):
        if (settings.mode == 27):
            r_val["NPOS"] = player.position
            print("Demo mode no move")
        else:
            r_val["NPOS"] = (player.position - 2)% settings.tile_count
    if (tile_num == 22):
        pass
    if (tile_num == 23):
        pass
    if (tile_num == 24):
        pass
    return r_val
        
    

def event_button_close(tile_num,panel,mouse_pos, event_list):

    if (tile_num == 1):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 2):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 3):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 4):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 5):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 6):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 7):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 8):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 9):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 10):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 11):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 12):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 13):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 14):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 15):
        if (panel.button.is_clicked(mouse_pos, event_list)):
            if (panel.current_page >= panel.page_count - 1): return True
            else:
                panel.flip_page()
    # 16 pass
    if (tile_num == 17):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 18):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 19):
        if (panel.button.is_clicked(mouse_pos, event_list)):
            if (panel.current_page >= panel.page_count - 1): return True
            else:
                panel.flip_page()
    if (tile_num == 20):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 21):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True
    if (tile_num == 22):
        if (panel.button.is_clicked(mouse_pos, event_list)):
            if (panel.current_page >= panel.page_count - 1): return True
            else:
                panel.flip_page()
    if (tile_num == 23):
        if (panel.button.is_clicked(mouse_pos, event_list)):
            if (panel.current_page >= panel.page_count - 1): return True
            else:
                panel.flip_page()   
    if (tile_num == 24):
        if (panel.button.is_clicked(mouse_pos, event_list)): return True