import os

import pygame
import networkx as nx

from core.screens import Screens
from ui.animated_bug import AnimatedBug
from ui.animated_sprite import AnimatedSprite
from ui.characters.frog_neutral import FrogNeutral
from ui.screens.common.dialogue_renderer import render_dialogue
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_graph
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.screens.common.seed_counter_renderer import render_seed_counter
from ui.screens.common.start_button_renderer import render_start_button
from core.fonts import *

G = nx.Graph()
positions = {
    'A': (507,397-60), 'B': (379,575-60), 'C': (598,274-60), 'D': (765,496-60),
    'E': (230,465-60), 'F': (334,304-60), 'G': (1080,268-60), 'H': (805,314-60),
    'I': (1015,615-60), 'J': (1376,320-60), 'K': (1138,437-60), 'L': (1225,632-60),
}

seeds = {
    'A': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'B': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'C': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'D': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'E': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'F': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'G': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'H': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'I': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'J': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'K': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
    'L': AnimatedBug(x_position_extra=0, y_position_extra=-10,frame_path="./assets/giphs/bugs/bug-hamilton-2/hamilton-2-bug", frame_size=(120, 120), frame_count=74)
}

dead_flower = AnimatedSprite(frame_path="./assets/giphs/flowers-bw/hamilton-2-flower-bw/hamilton-2-flower-bw", frame_size=(480, 480), frame_count=74)
flower = AnimatedSprite(frame_path="./assets/giphs/flowers/hamilton-2-flower/hamilton-2-flower", frame_size=(480, 480), frame_count=74)

missing_nodes = len(positions)

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('J', 'L'), ('J', 'I'), ('I', 'B'), ('K', 'I'), ('J', 'H'),
    ('G', 'H'), ('C', 'G'), ('B', 'D'), ('E', 'D'), ('A', 'F'),
    ('E', 'F'), ('F', 'C'), ('G', 'K'), ('B', 'A'), ('C', 'A')
]

for edge in edges:
    G.add_edge(edge[0], edge[1])

start_node = None
end_node = 'H'
path = []
timer_started = False
start_time = 0

current_node = None
won_level = False
initial_energy = 17
energy = initial_energy  # Starting energy level
start_ticks = pygame.time.get_ticks()  # Start time for timer
timer_duration = 60000  # 60 seconds duration

back_button_clicked_grafos_hamilton_2 = None
start_button_clicked_grafos_hamilton_2 = None
restart_button_clicked_grafos_hamilton_2 = None
main_menu_button_clicked_grafos_hamilton_2 = None


def render_grafos_hamilton_2(screen, font):
    from core.fonts import font_small_buttons
    global back_button_clicked_grafos_hamilton_2, start_button_clicked_grafos_hamilton_2,\
        restart_button_clicked_grafos_hamilton_2, timer_started, start_time, path, start_node, positions,\
        current_node, energy, won_level, flower, missing_nodes, remaining_time, main_menu_button_clicked_grafos_hamilton_2

    current_time = pygame.time.get_ticks()
    if won_level:
        background_image_win = pygame.image.load("assets/final-bg/hamilton-2.png").convert()
        background_image_win = pygame.transform.scale(background_image_win, (1710, 1034))
        screen.blit(background_image_win, (0, 0))
    elif timer_started:
        background_image = pygame.image.load("assets/initial-bg/hamilton-2.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
    else:
        background_image = pygame.image.load("assets/blur/hamilton-2.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        start_time = pygame.time.get_ticks()
        remaining_time = 60000

    # Update energy based on remaining time
    if remaining_time > 0:
        energy = initial_energy * (remaining_time / timer_duration)
    else:
        energy = initial_energy  # Reset energy if time runs out

    # Draw the "Back" button
    back_button_clicked_grafos_hamilton_2 = render_map_button(screen, font_small_buttons)

    if not timer_started:
        start_button_clicked_grafos_hamilton_2 = render_start_button(screen, font_start, AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(150, 150), frame_count=74))

    else:
        # Render the graph and energy bar
        render_graph(screen, G, font, path, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_clicked_grafos_hamilton_2 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        main_menu_button_clicked_grafos_hamilton_2 = render_main_menu_button(screen, font_small_buttons)

        render_seed_counter(screen,font,missing_nodes, AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74))

        render_dialogue(screen, "Restore the plant 'Erlem' by solving the Hamilton graph before the timer runs out.\n- You must pass through ALL 12 nodes.\n- You can repeat edges, but NOT nodes.\n- You can start anywhere, but must finish at the bug node so I can eat it.\nPress the letters to navigate the entire graph in order!", font)

        if won_level:
            flower.update_animation()
            flower.draw(screen, 1490, 750)
        else:
            dead_flower.update_animation()
            dead_flower.draw(screen, 1490, 750)

    # Check if time is up
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)


def handle_grafos_hamilton_2_mousedown(event, go_to_level):
    global back_button_clicked_grafos_hamilton_2, start_button_clicked_grafos_hamilton_2, restart_button_clicked_grafos_hamilton_2, timer_started, main_menu_button_clicked_grafos_hamilton_2
    if back_button_clicked_grafos_hamilton_2 is not None and back_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = False
        go_to_level(Screens.MAP)
        reset_nodes(path)
    elif start_button_clicked_grafos_hamilton_2 is not None and start_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = True
    elif restart_button_clicked_grafos_hamilton_2 is not None and restart_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = True
        reset_nodes(path)
    elif main_menu_button_clicked_grafos_hamilton_2 is not None and main_menu_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = True
        reset_nodes(path)
        go_to_level(Screens.MAIN)


def reset_nodes(path):
    global current_node,G, seeds, missing_nodes
    path.clear()
    current_node = None
    seeds = {
        'A': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'B': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'C': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'D': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'E': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'F': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'G': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'H': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'I': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'J': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'K': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74),
        'L': AnimatedBug(x_position_extra=0, y_position_extra=-10,frame_path="./assets/giphs/bugs/bug-hamilton-2/hamilton-2-bug", frame_size=(120, 120), frame_count=74)
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

    missing_nodes = len(positions)

def handle_grafos_hamilton_2_keydown(event,go_to_map):
    global current_node, seeds, won_level, missing_nodes
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74)
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/hamilton-2-seed/hamilton-2-seed", frame_size=(90, 90), frame_count=74)
            missing_nodes -= 1

            if current_node == end_node and len(path) == len(G.nodes):
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")
