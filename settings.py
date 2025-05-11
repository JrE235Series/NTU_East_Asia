import pygame

window_width = 1500
window_height = 900

block_size = 150

row_count = int(window_width / block_size)
column_count = int(window_height / block_size)

tile_count = (row_count + column_count) *2 - 4