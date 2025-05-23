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