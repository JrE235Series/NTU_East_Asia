import pygame

window_width = 1200
window_height = 900

block_size = 150

row_count = int(window_width / block_size)
column_count = int(window_height / block_size)

tile_count = (row_count + column_count) *2 - 4

dice_panel_width = 600
dice_panel_height = 400
dice_panel_positon = [block_size, block_size]

score_panel_width = 600
score_panel_height = 600
score_panel_position = [window_width - block_size - score_panel_width, block_size]

central_panel_width = 900
central_panel_height = 600
central_panel_position = [block_size, block_size]

mode = -1

demo_dice_val = [3,2,4,3,3,2,2,3,2]  #last 2 is to get back to block 1
demo_dice_count = len(demo_dice_val)

player_size_4 = (77,77)
player_size_1 = (140,140)
player_space_x = 75
player_space_y = 75

magazine_link = "https://drive.google.com/file/d/12IlPm0GuwmGAPIBkbdrxv_xv2q_jvyy8/preview#page=10"
magazine_link_m = "https://mozilla.github.io/pdf.js/web/viewer.html?file=https://jre235series.github.io/NTU_East_Asia/%E5%BC%95%E6%8F%9A%E5%91%A8%E5%88%8A.pdf"

magazine_link_m_v1 = "https://mozilla.github.io/pdf.js/web/viewer.html?file=https://jre235series.github.io/NTU_East_Asia/%E5%BC%95%E6%8F%9A%E5%91%A8%E5%88%8A.pdf#page=3"

magazine_link_m_v2 = "https://mozilla.github.io/pdf.js/web/viewer.html?file=https://jre235series.github.io/NTU_East_Asia/%E5%BC%95%E6%8F%9A%E5%91%A8%E5%88%8A.pdf#page=4"

magazine_link_m_p1 = "https://mozilla.github.io/pdf.js/web/viewer.html?file=https://jre235series.github.io/NTU_East_Asia/%E5%BC%95%E6%8F%9A%E5%91%A8%E5%88%8A.pdf#page=6"

magazine_link_5 = magazine_link_m + "#page=11"
magazine_link_6 = magazine_link_m + "#page=13"
magazine_link_7 = magazine_link_m + "#page=11"
magazine_link_10 = magazine_link_m + "#page=13"
magazine_link_12 = magazine_link_m + "#page=12"
magazine_link_21_1 = magazine_link_m + "#page=10"
magazine_link_21_2 = magazine_link_m + "#page=8"

video_link_1 = "https://drive.google.com/file/d/1FE-ANme8tCisRsK4FK_mP3BAJPznVkbM/view?usp=drive_link"
video_link_4 = "https://drive.google.com/file/d/1yKGGTZHWZT6KPwUzwAlLKUbNdAp-yfMP/view?usp=drive_link"
video_link_6 = "https://drive.google.com/file/d/11KUxgQPgjNw0nz_t-Gf9QjGDmPpiiMbS/view?usp=drive_link"
video_link_12 = "https://drive.google.com/file/d/1BFVaO0-xFX9jPlfakrr5Un9ImoFHoNHr/view?usp=drive_link"
video_link_21 = "https://drive.google.com/file/d/19aCwEM8Tv_BCIhFCYphC-VB1fKA7Ou64/view?usp=drive_link"
video_link_24 = "https://drive.google.com/file/d/1-0bIvuCUyUIBxQ-KscXBQOAa4XMjJpsx/view?usp=drive_link"