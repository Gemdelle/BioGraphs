import pygame

from core.screens import Screens
from ui.screens.digrafos_euler_1 import render_digrafos_euler_1, handle_digrafos_euler_1_keydown, is_back_button_clicked_digrafos_euler
from ui.screens.digrafos_hamilton_1 import render_digrafos_hamilton_1, handle_digrafos_hamilton_1_keydown, is_back_button_clicked_hamilton_1
from ui.screens.grafos_euler_1 import render_grafos_euler_1, handle_grafos_euler_1_keydown, is_back_button_clicked_grafos_euler_1
from ui.screens.grafos_euler_2 import render_grafos_euler_2, handle_grafos_euler_2_keydown, is_back_button_clicked_grafos_euler_2
from ui.screens.grafos_euler_3 import render_grafos_euler_3, handle_grafos_euler_3_keydown, is_back_button_clicked_grafos_euler_3
from ui.screens.grafos_hamilton_1 import render_grafos_hamilton_1, handle_grafos_hamilton_1_keydown, is_back_button_clicked_grafos_hamilton_1
from ui.screens.grafos_hamilton_2 import render_grafos_hamilton_2, handle_grafos_hamilton_2_keydown, is_back_button_clicked_grafos_hamilton_2
from ui.screens.grafos_hamilton_3 import render_grafos_hamilton_3, handle_grafos_hamilton_3_keydown, is_back_button_clicked_grafos_hamilton_3
from ui.screens.instructions import render_instructions
from ui.screens.main import render_main_screen
from ui.screens.map import render_map
from ui.screens.playground import render_playground
from ui.screens.splash import render_splash

pygame.init()
pygame.font.init()

# CONFIGURACIÓN DE PANTALLA
SCREEN_WIDTH = 1710
SCREEN_HEIGHT = 1034
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
current_node = None
completed = False

font = pygame.font.SysFont(None, 36)

screen_selected = Screens.MAIN  # Start at MAIN screen
start_ticks = pygame.time.get_ticks()
timer_duration = 30000


def go_to_map():
    global screen_selected
    screen_selected = Screens.MAP


def go_to_level(screen):
    global screen_selected
    screen_selected = screen

buttons = []
# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if screen_selected == Screens.MAIN:
                for text, btn_rect in buttons:
                    if btn_rect.collidepoint(mouse_pos):
                        if text == "Instructions":
                            screen_selected = Screens.INSTRUCTIONS
                        elif text == "Playground":
                            screen_selected = Screens.PLAYGROUND
                        elif text == "Map":
                            go_to_map()

            elif (is_back_button_clicked_digrafos_euler(event) or
                  is_back_button_clicked_hamilton_1(event) or
                  is_back_button_clicked_grafos_euler_1(event) or
                  is_back_button_clicked_grafos_euler_2(event) or
                  is_back_button_clicked_grafos_euler_3(event) or
                  is_back_button_clicked_grafos_hamilton_1(event) or
                  is_back_button_clicked_grafos_hamilton_2(event) or
                  is_back_button_clicked_grafos_hamilton_3(event)):
                go_to_map()

        if screen_selected == Screens.GRAFOS_EULER_1:
            completed, current_node = handle_grafos_euler_1_keydown(event)
        elif screen_selected == Screens.GRAFOS_EULER_2:
            completed, current_node = handle_grafos_euler_2_keydown(event)
        elif screen_selected == Screens.GRAFOS_EULER_3:
            completed, current_node = handle_grafos_euler_3_keydown(event)
        elif screen_selected == Screens.GRAFOS_HAMILTON_1:
            completed, current_node = handle_grafos_hamilton_1_keydown(event)
        elif screen_selected == Screens.GRAFOS_HAMILTON_2:
            completed, current_node = handle_grafos_hamilton_2_keydown(event)
        elif screen_selected == Screens.GRAFOS_HAMILTON_3:
            completed, current_node = handle_grafos_hamilton_3_keydown(event)
        elif screen_selected == Screens.DIGRAFOS_EULER_1:
            completed, current_node = handle_digrafos_euler_1_keydown(event)
        elif screen_selected == Screens.DIGRAFOS_HAMILTON_1:
            completed, current_node = handle_digrafos_hamilton_1_keydown(event)

    # Screen rendering
    if screen_selected == Screens.SPLASH:
        render_splash(screen, go_to_map)
    elif screen_selected == Screens.MAIN:
        buttons = render_main_screen(screen, font)
    elif screen_selected == Screens.MAP:
        render_map(screen, go_to_level)
    elif screen_selected == Screens.INSTRUCTIONS:
        render_instructions(screen)
    elif screen_selected == Screens.PLAYGROUND:
        render_playground(screen, go_to_level)
    elif screen_selected == Screens.GRAFOS_EULER_1:
        completed = render_grafos_euler_1(screen, font)
    elif screen_selected == Screens.GRAFOS_EULER_2:
        completed = render_grafos_euler_2(screen, font)
    elif screen_selected == Screens.GRAFOS_EULER_3:
        completed = render_grafos_euler_3(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_1:
        completed = render_grafos_hamilton_1(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_2:
        completed = render_grafos_hamilton_2(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_3:
        completed = render_grafos_hamilton_3(screen, font)
    elif screen_selected == Screens.DIGRAFOS_EULER_1:
        completed = render_digrafos_euler_1(screen, font)
    elif screen_selected == Screens.DIGRAFOS_HAMILTON_1:
        completed = render_digrafos_hamilton_1(screen, font, go_to_map, pygame.event.get())
    else:
        print("Screen not found")

    if completed:
        screen_selected = Screens.MAP

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
