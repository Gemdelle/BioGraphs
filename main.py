import pygame

from core.screens import Screens
from ui.config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui.screens.intro_euler_cycle import render_intro_euler_cycle, is_back_button_clicked_intro_euler_cicle
from ui.screens.intro_euler_path import render_intro_euler_path, is_back_button_clicked_intro_euler_path
from ui.screens.intro_hamilton_cicle import render_intro_hamilton_cicle, is_back_button_clicked_intro_hamilton_cicle
from ui.screens.intro_hamilton_path import render_intro_hamilton_path, is_back_button_clicked_intro_hamilton_path

from ui.screens.playground_1 import (render_playground_1, handle_playground_1_keydown,
                                     handle_playground_1_mousedown)
from ui.screens.playground_2 import (render_playground_2, handle_playground_2_keydown, handle_playground_2_mousedown)
from ui.screens.playground_3 import (render_playground_3, handle_playground_3_keydown,
                                     handle_playground_3_mousedown)
from ui.screens.playground_4 import (render_playground_4, handle_playground_4_keydown,
                                     handle_playground_4_mousedown)
from ui.screens.playground_5 import (render_playground_5, handle_playground_5_keydown,
                                     handle_playground_5_mousedown)

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
from ui.screens.game_modes import render_main_screen, MovingImage
from ui.screens.map import render_map
from ui.screens.playground import render_playground
from ui.screens.select_your_pet import render_select_your_pet_screen
from ui.splash_video import SplashVideo

pygame.init()

from core.fonts import title_font, font

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True

screen_selected = Screens.MAIN  # Start screen
start_ticks = pygame.time.get_ticks()
timer_duration = 30000

# FUNCTIONS
def go_to_map():
    global screen_selected
    screen_selected = Screens.MAP


def go_to_playground():
    global screen_selected
    screen_selected = Screens.PLAYGROUND


def go_to_level(screen):
    global screen_selected
    print(f"Going to level {screen}")
    screen_selected = screen


def go_to_instructions():
    global screen_selected
    screen_selected = Screens.INSTRUCTIONS


def go_to_main():
    global screen_selected
    screen_selected = Screens.MAIN


buttons = []
moving_tadpoles = [MovingImage(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(5)]
splash_video = SplashVideo(SCREEN_WIDTH, SCREEN_HEIGHT)

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

            elif (is_back_button_clicked_intro_euler_cicle(event) or
                  is_back_button_clicked_intro_euler_path(event) or
                  is_back_button_clicked_intro_hamilton_cicle(event) or
                  is_back_button_clicked_intro_hamilton_path(event)):
                go_to_instructions()

            elif is_back_button_clicked_instructions(event):
                go_to_main()

            handle_grafos_digrafos_euler_mousedown(event, go_to_level)
            handle_grafos_digrafos_hamilton_1_mousedown(event, go_to_level)
            handle_grafos_euler_1_mousedown(event, go_to_level)
            handle_grafos_euler_2_mousedown(event, go_to_level)
            handle_grafos_euler_3_mousedown(event, go_to_level)
            handle_grafos_hamilton_1_mousedown(event, go_to_level)
            handle_grafos_hamilton_2_mousedown(event, go_to_level)
            handle_grafos_hamilton_3_mousedown(event, go_to_level)
            handle_playground_1_mousedown(event, go_to_playground)
            handle_playground_2_mousedown(event, go_to_playground)
            handle_playground_3_mousedown(event, go_to_playground)
            handle_playground_4_mousedown(event, go_to_playground)
            handle_playground_5_mousedown(event, go_to_playground)

        if screen_selected == Screens.GRAFOS_EULER_1:
            handle_grafos_euler_1_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_EULER_2:
            handle_grafos_euler_2_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_EULER_3:
            handle_grafos_euler_3_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_HAMILTON_1:
            handle_grafos_hamilton_1_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_HAMILTON_2:
            handle_grafos_hamilton_2_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_HAMILTON_3:
            handle_grafos_hamilton_3_keydown(event,go_to_map)
        elif screen_selected == Screens.DIGRAFOS_EULER_1:
            handle_digrafos_euler_1_keydown(event,go_to_map)
        elif screen_selected == Screens.DIGRAFOS_HAMILTON_1:
            handle_digrafos_hamilton_1_keydown(event,go_to_map)

        elif screen_selected == Screens.PLAYGROUND_1:
            handle_playground_1_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_2:
            handle_playground_2_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_3:
            handle_playground_3_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_4:
            handle_playground_4_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_5:
            handle_playground_5_keydown(event)
        elif screen_selected == Screens.INSTRUCTIONS:
            handle_instructions_keydown(event, go_to_level)

    # Screen rendering
    if screen_selected == Screens.SPLASH:
        splash_video.play_video(screen, lambda: go_to_level(Screens.SELECT_YOUR_PET))
    elif screen_selected == Screens.SELECT_YOUR_PET:
        render_select_your_pet_screen(screen, go_to_level)
    elif screen_selected == Screens.MAIN:
        buttons = render_main_screen(screen, title_font, font, moving_tadpoles)
    elif screen_selected == Screens.MAP:
        render_map(screen, go_to_level)
    elif screen_selected == Screens.INSTRUCTIONS:
        render_instructions(screen)
    elif screen_selected == Screens.PLAYGROUND:
        render_playground(screen, go_to_level, pygame.time.get_ticks() / 150)

    elif screen_selected == Screens.PLAYGROUND_1:
        render_playground_1(screen, font)
    elif screen_selected == Screens.PLAYGROUND_2:
        render_playground_2(screen, font)
    elif screen_selected == Screens.PLAYGROUND_3:
        render_playground_3(screen, font)
    elif screen_selected == Screens.PLAYGROUND_4:
        render_playground_4(screen, font)
    elif screen_selected == Screens.PLAYGROUND_5:
        render_playground_5(screen, font)

    elif screen_selected == Screens.GRAFOS_EULER_1:
        render_grafos_euler_1(screen, font)
    elif screen_selected == Screens.GRAFOS_EULER_2:
        render_grafos_euler_2(screen, font)
    elif screen_selected == Screens.GRAFOS_EULER_3:
        render_grafos_euler_3(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_1:
        render_grafos_hamilton_1(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_2:
        render_grafos_hamilton_2(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_3:
        render_grafos_hamilton_3(screen, font)
    elif screen_selected == Screens.DIGRAFOS_EULER_1:
        render_digrafos_euler_1(screen, font)
    elif screen_selected == Screens.DIGRAFOS_HAMILTON_1:
        render_digrafos_hamilton_1(screen, font, go_to_map, pygame.event.get())
    elif screen_selected == Screens.INTRO_HAMILTON_PATH: 
        render_intro_hamilton_path(screen, font)
    elif screen_selected == Screens.INTRO_HAMILTON_CYCLE:
        render_intro_hamilton_cicle(screen, font)
    elif screen_selected == Screens.INTRO_EULER_PATH:
        render_intro_euler_path(screen, font)
    elif screen_selected == Screens.INTRO_EULER_CYCLE:
        render_intro_euler_cycle(screen, font)
    else:
        print("Screen not found")

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
