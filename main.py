import pygame
from moviepy.video.io.VideoFileClip import VideoFileClip

from core.screens import Screens
from ui.screens.common.sound_player import play_button, play_sound
from ui.screens.intro_diagraphs import render_intro_diagraphs
from ui.screens.intro_euler_path import render_intro_euler_path
from ui.screens.intro_graphs import render_intro_graphs
from ui.screens.intro_hamilton_path import render_intro_hamilton_path
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT

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
from ui.screens.instructions import render_instructions, handle_instructions_mouse_down
from ui.screens.game_modes import render_main_screen, MovingImage
from ui.screens.map import render_map, handle_map_mousedown
from ui.screens.playground import render_playground, handle_playground_mousedown
from ui.screens.select_your_pet import render_select_your_pet_screen
from ui.utils.video import Video

pygame.init()

from ui.utils.fonts import title_font, font

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
mousedown_processing = False

screen_selected = Screens.SELECT_YOUR_PET  # Start screen
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
splash_video = Video(SCREEN_WIDTH, SCREEN_HEIGHT, "./assets/splash/splash.mp4")




# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mousedown_processing:
                continue
            mousedown_processing = True
            try:
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

                handle_map_mousedown(go_to_level, screen_selected==Screens.MAP)
                handle_playground_mousedown(go_to_level, screen_selected==Screens.PLAYGROUND)
                handle_grafos_digrafos_euler_mousedown(event, go_to_level, screen_selected==Screens.DIGRAFOS_EULER_1)
                handle_grafos_digrafos_hamilton_1_mousedown(event, go_to_level, screen_selected==Screens.DIGRAFOS_HAMILTON_1)
                handle_grafos_euler_1_mousedown(event, go_to_level, screen_selected==Screens.GRAFOS_EULER_1)
                handle_grafos_euler_2_mousedown(event, go_to_level, screen_selected==Screens.GRAFOS_EULER_2)
                handle_grafos_euler_3_mousedown(event, go_to_level, screen_selected==Screens.GRAFOS_EULER_3)
                handle_grafos_hamilton_1_mousedown(event, go_to_level, screen_selected==Screens.GRAFOS_HAMILTON_1)
                handle_grafos_hamilton_2_mousedown(event, go_to_level, screen_selected==Screens.GRAFOS_HAMILTON_2)
                handle_grafos_hamilton_3_mousedown(event, go_to_level, screen_selected==Screens.GRAFOS_HAMILTON_3)
                handle_playground_1_mousedown(event, go_to_level, screen_selected==Screens.PLAYGROUND_1)
                handle_playground_2_mousedown(event, go_to_level, screen_selected==Screens.PLAYGROUND_2)
                handle_playground_3_mousedown(event, go_to_level, screen_selected==Screens.PLAYGROUND_3)
                handle_playground_4_mousedown(event, go_to_level, screen_selected==Screens.PLAYGROUND_4)
                handle_playground_5_mousedown(event, go_to_level, screen_selected==Screens.PLAYGROUND_5)
                handle_instructions_mouse_down(event, go_to_level, screen_selected == Screens.INSTRUCTIONS)

            finally:
                mousedown_processing = False

        if screen_selected == Screens.GRAFOS_EULER_1:
            play_sound('map-levels-bg.mp3')
            handle_grafos_euler_1_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_EULER_2:
            play_sound('map-levels-bg.mp3')
            handle_grafos_euler_2_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_EULER_3:
            play_sound('map-levels-bg.mp3')
            handle_grafos_euler_3_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_HAMILTON_1:
            play_sound('map-levels-bg.mp3')
            handle_grafos_hamilton_1_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_HAMILTON_2:
            play_sound('map-levels-bg.mp3')
            handle_grafos_hamilton_2_keydown(event,go_to_map)
        elif screen_selected == Screens.GRAFOS_HAMILTON_3:
            play_sound('map-levels-bg.mp3')
            handle_grafos_hamilton_3_keydown(event,go_to_map)
        elif screen_selected == Screens.DIGRAFOS_EULER_1:
            play_sound('map-levels-bg.mp3')
            handle_digrafos_euler_1_keydown(event,go_to_map)
        elif screen_selected == Screens.DIGRAFOS_HAMILTON_1:
            play_sound('map-levels-bg.mp3')
            handle_digrafos_hamilton_1_keydown(event,go_to_map)

        elif screen_selected == Screens.PLAYGROUND_1:
            play_sound('playground-levels-bg.mp3',0.2)
            handle_playground_1_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_2:
            play_sound('playground-levels-bg.mp3',0.2)
            handle_playground_2_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_3:
            play_sound('playground-levels-bg.mp3',0.2)
            handle_playground_3_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_4:
            play_sound('playground-levels-bg.mp3',0.2)
            handle_playground_4_keydown(event)
        elif screen_selected == Screens.PLAYGROUND_5:
            play_sound('playground-levels-bg.mp3',0.2)
            handle_playground_5_keydown(event)

    # Screen rendering
    if screen_selected == Screens.SPLASH:
        splash_video.play_video(screen, lambda: go_to_level(Screens.SELECT_YOUR_PET))
    elif screen_selected == Screens.SELECT_YOUR_PET:
        play_sound('menu-background.mp3')
        render_select_your_pet_screen(screen, go_to_level)
    elif screen_selected == Screens.MAIN:
        play_sound('menu-background.mp3')
        buttons = render_main_screen(screen, title_font, font, moving_tadpoles)
    elif screen_selected == Screens.MAP:
        play_sound('maps-background.mp3')
        render_map(screen, go_to_level)
    elif screen_selected == Screens.INSTRUCTIONS:
        play_sound('maps-background.mp3')
        render_instructions(screen)
    elif screen_selected == Screens.PLAYGROUND:
        play_sound('maps-background.mp3')
        render_playground(screen, pygame.time.get_ticks() / 150)

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
    elif screen_selected == Screens.INTRO_DIGRAPHS:
        render_intro_diagraphs(screen, go_to_level)
    elif screen_selected == Screens.INTRO_HAMILTON_PATH:
        render_intro_hamilton_path(screen, go_to_level)
    elif screen_selected == Screens.INTRO_GRAPHS:
        render_intro_graphs(screen, go_to_level)
    elif screen_selected == Screens.INTRO_EULER_PATH:
        render_intro_euler_path(screen, go_to_level)
    else:
        print("Screen not found")

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
