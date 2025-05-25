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