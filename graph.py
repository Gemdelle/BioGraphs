import pygame

from core.screens import Screens
from ui.characters.euler_1_flower import Euler1Flower
from ui.config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui.screens.intro_euler_cicle import render_intro_euler_cicle, is_back_button_clicked_intro_euler_cicle
from ui.screens.intro_euler_path import render_intro_euler_path, is_back_button_clicked_intro_euler_path
from ui.screens.intro_hamilton_cicle import render_intro_hamilton_cicle, is_back_button_clicked_intro_hamilton_cicle
from ui.screens.intro_hamilton_path import render_intro_hamilton_path, is_back_button_clicked_intro_hamilton_path

from ui.screens.playground_1 import (render_playground_1, handle_playground_1_keydown,
                                     handle_playground_1_mousedown)
from ui.screens.playground_2 import (render_playground_2, handle_playground_2_keydown,
                                     is_back_button_clicked_playground_2)
from ui.screens.playground_3 import (render_playground_3, handle_playground_3_keydown,
                                     is_back_button_clicked_playground_3)
from ui.screens.playground_4 import (render_playground_4, handle_playground_4_keydown,
                                     is_back_button_clicked_playground_4)
from ui.screens.playground_5 import (render_playground_5, handle_playground_5_keydown,
                                     is_back_button_clicked_playground_5)

from ui.screens.digrafos_euler_1 import (render_digrafos_euler_1, handle_digrafos_euler_1_keydown,
                                         handle_grafos_digrafos_euler_mousedown)
from ui.screens.digrafos_hamilton_1 import (render_digrafos_hamilton_1, handle_digrafos_hamilton_1_keydown,
                                            handle_grafos_digrafos_hamilton_1_mousedown)
from ui.screens.grafos_euler_1 import (render_grafos_euler_1, handle_grafos_euler_1_keydown,
                                       handle_grafos_euler_1_mousedown)
from ui.screens.grafos_euler_2 import (render_grafos_euler_2, handle_grafos_euler_2_keydown,
                                       handle_grafos_euler_2_mousedown)
from ui.screens.grafos_euler_3 import (render_grafos_euler_3, handle_grafos_euler_3_keydown,
                                       handle_grafos_euler_3_mousedown)
from ui.screens.grafos_hamilton_1 import (render_grafos_hamilton_1, handle_grafos_hamilton_1_keydown,
                                          handle_grafos_hamilton_1_mousedown)
from ui.screens.grafos_hamilton_2 import (render_grafos_hamilton_2, handle_grafos_hamilton_2_keydown,
                                          handle_grafos_hamilton_2_mousedown)
from ui.screens.grafos_hamilton_3 import (render_grafos_hamilton_3, handle_grafos_hamilton_3_keydown,
                                          handle_grafos_hamilton_3_mousedown)
from ui.screens.instructions import render_instructions, handle_instructions_keydown, is_back_button_clicked_instructions
from ui.screens.main import render_main_screen
from ui.screens.map import render_map
from ui.screens.playground import render_playground
from ui.screens.splash import render_splash

pygame.init()
pygame.font.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
current_node = None
completed = False

font = pygame.font.SysFont(None, 36)
fontButtons = pygame.font.SysFont(None, 56)

screen_selected = Screens.MAIN  # Start at MAIN screen
start_ticks = pygame.time.get_ticks()
timer_duration = 30000

#euler_1_flower = Euler1Flower()

def go_to_map():
    global screen_selected
    screen_selected = Screens.MAP


def go_to_playground():
    global screen_selected
    screen_selected = Screens.PLAYGROUND


def go_to_level(screen):
    global screen_selected
    screen_selected = screen

def go_to_instructions():
    global screen_selected
    screen_selected = Screens.INSTRUCTIONS

def go_to_main():
    global screen_selected
    screen_selected = Screens.MAIN

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

            elif (handle_playground_1_mousedown(event, go_to_playground) or
                  is_back_button_clicked_playground_2(event) or
                  is_back_button_clicked_playground_3(event) or
                  is_back_button_clicked_playground_4(event) or
                  is_back_button_clicked_playground_5(event)):
                go_to_playground()

            elif (is_back_button_clicked_intro_euler_cicle(event) or
                  is_back_button_clicked_intro_euler_path(event) or
                  is_back_button_clicked_intro_hamilton_cicle(event) or
                  is_back_button_clicked_intro_hamilton_path(event)):
                go_to_instructions()

            elif is_back_button_clicked_instructions(event):
                go_to_main()

            handle_grafos_digrafos_euler_mousedown(event, go_to_map)
            handle_grafos_digrafos_hamilton_1_mousedown(event, go_to_map)
            handle_grafos_euler_1_mousedown(event, go_to_map)
            handle_grafos_euler_2_mousedown(event, go_to_map)
            handle_grafos_euler_3_mousedown(event, go_to_map)
            handle_grafos_hamilton_1_mousedown(event, go_to_map)
            handle_grafos_hamilton_2_mousedown(event, go_to_map)
            handle_grafos_hamilton_3_mousedown(event, go_to_map)

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

        elif screen_selected == Screens.PLAYGROUND_1:
            completed, current_node = handle_playground_1_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_2:
            completed, current_node = handle_playground_2_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_3:
            completed, current_node = handle_playground_3_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_4:
            completed, current_node = handle_playground_4_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_5:
            completed, current_node = handle_playground_5_keydown(event)
        elif screen_selected == Screens.INSTRUCTIONS:
            handle_instructions_keydown(event, go_to_level)

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

    elif screen_selected == Screens.PLAYGROUND_1:
        completed = render_playground_1(screen, font)
    elif screen_selected == Screens.PLAYGROUND_2:
        completed = render_playground_2(screen, font)
    elif screen_selected == Screens.PLAYGROUND_3:
        completed = render_playground_3(screen, font)
    elif screen_selected == Screens.PLAYGROUND_4:
        completed = render_playground_4(screen, font)
    elif screen_selected == Screens.PLAYGROUND_5:
        completed = render_playground_5(screen, font)

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
    elif screen_selected == Screens.INTRO_HAMILTON_PATH:
        render_intro_hamilton_path(screen, font)
    elif screen_selected == Screens.INTRO_HAMILTON_CICLE:
        render_intro_hamilton_cicle(screen, font)
    elif screen_selected == Screens.INTRO_EULER_PATH:
        render_intro_euler_path(screen, font)
    elif screen_selected == Screens.INTRO_EULER_CICLE:
        render_intro_euler_cicle(screen, font)
    else:
        print("Screen not found")

    if completed:
        screen_selected = Screens.MAP

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
