# FONTS
import os

import pygame

pygame.font.init()

font_path = 'assets/fonts/'

title_font = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 55)

font = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 32)
font_buttons = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 32)
font_small_buttons = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 28)
font_start = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 24)