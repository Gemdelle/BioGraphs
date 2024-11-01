import pygame

from core.screens import Screens
from ui.screens.digrafos_euler_1 import render_digrafos_euler_1, handle_digrafos_euler_1_keydown
from ui.screens.digrafos_hamilton_1 import render_digrafos_hamilton_1, handle_digrafos_hamilton_1_keydown
from ui.screens.grafos_euler_1 import render_grafos_euler_1, handle_grafos_euler_1_keydown
from ui.screens.grafos_hamilton_1 import render_grafos_hamilton_1, handle_grafos_hamilton_1_keydown
from ui.screens.grafos_hamilton_2 import render_grafos_hamilton_2, handle_grafos_hamilton_2_keydown
from ui.screens.grafos_hamilton_3 import render_grafos_hamilton_3, handle_grafos_hamilton_3_keydown
from ui.screens.main import render_main
from ui.screens.splash import render_splash

pygame.init()
pygame.font.init()

# CONFIGURACIÓN DE PANTALLA
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
current_node = None
completed = False

font = pygame.font.SysFont(None, 36)

screen_selected = Screens.SPLASH
start_ticks = pygame.time.get_ticks()
timer_duration = 30000

def goToMain():
    global screen_selected
    screen_selected = Screens.MAIN
def goToLevel(screen):
    global screen_selected
    screen_selected = screen

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if screen_selected == Screens.GRAFOS_EULER_1:
            completed, current_node = handle_grafos_euler_1_keydown(event)
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

    if screen_selected == Screens.SPLASH:
        render_splash(screen, goToMain)
    elif screen_selected == Screens.MAIN:
        render_main(screen, goToLevel)
    elif screen_selected == Screens.GRAFOS_EULER_1:
        completed = render_grafos_euler_1(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_1:
        completed = render_grafos_hamilton_1(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_2:
        completed = render_grafos_hamilton_2(screen, font)
    elif screen_selected == Screens.GRAFOS_HAMILTON_3:
        completed = render_grafos_hamilton_3(screen, font)
    elif screen_selected == Screens.DIGRAFOS_EULER_1:
        completed = render_digrafos_euler_1(screen, font)
    elif screen_selected == Screens.DIGRAFOS_HAMILTON_1:
        completed = render_digrafos_hamilton_1(screen, font)
    else:
        print("Screen not found")

    if completed:
        screen_selected = Screens.MAIN

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
