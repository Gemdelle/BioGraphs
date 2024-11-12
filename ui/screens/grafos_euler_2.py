import os

import pygame
import networkx as nx

from ui.animated_sprite import AnimatedSprite
from ui.characters.frog_neutral import FrogNeutral
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_graph
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.screens.common.seed_counter_renderer import render_seed_counter
from ui.seeds.disabled.euler_2_seed_disabled import Euler2SeedDisabled
from ui.seeds.enabled.euler_2_seed import Euler2Seed

G = nx.Graph()
# restarle 60 a y
positions = {
    'A': (1294,440-60),
    'B': (1433,565-60),
    'C': (1045,259-60),
    'D': (851,592-60),
    'E': (1124,552-60),
    'F': (730,370-60),
    'G': (358,556-60),
    'H': (250,307-60)
}

seeds = {
    'A': Euler2Seed(),
    'B': Euler2Seed(),
    'C': Euler2Seed(),
    'D': Euler2Seed(),
    'E': Euler2Seed(),
    'F': Euler2Seed(),
    'G': Euler2Seed(),
    'H': Euler2Seed()
}

missing_nodes = len(positions)
dead_flower = AnimatedSprite(frame_path="./assets/giphs/flowers-bw/euler-2-flower/euler-2-flower-bw", frame_size=(480, 480), frame_count=74)
flower = AnimatedSprite(frame_path="./assets/giphs/flowers/euler-2-flower/euler-2-flower", frame_size=(480, 480), frame_count=74)

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(200, 0, 0))

edges = [
    ('H', 'C'),('C', 'A'),('A', 'D'),('D', 'E'),('E', 'B'),('B', 'D'),('D', 'G'),('H', 'C'),('G', 'F'),('F', 'C'),
    ('G', 'C'),('A', 'D'),('D', 'E'),('E', 'B'),
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

back_button_clicked_grafos_euler_2 = None
start_button_clicked_grafos_euler_2 = None
restart_button_clicked_grafos_euler_2 = None


def render_grafos_euler_2(screen, font):
    from main import font_small_buttons
    global back_button_clicked_grafos_euler_2, start_button_clicked_grafos_euler_2, restart_button_clicked_grafos_euler_2, timer_started, start_time, path, start_node, positions, current_node, energy, flower, won_level, remaining_time

    current_time = pygame.time.get_ticks()
    if won_level:
        background_image_win = pygame.image.load("assets/final-bg/euler-2.png").convert()
        background_image_win = pygame.transform.scale(background_image_win, (1710, 1034))
        screen.blit(background_image_win, (0, 0))
    elif timer_started:
        background_image = pygame.image.load("assets/initial-bg/euler-2.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
    else:
        background_image = pygame.image.load("assets/blur/euler-2.png").convert()
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
    back_button_clicked_grafos_euler_2 = render_map_button(screen, font_small_buttons)

    if not timer_started:
        start_button_text = font_small_buttons.render("Start", True, (255, 255, 255))
        start_button_clicked_grafos_euler_2 = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_grafos_euler_2)
        screen.blit(start_button_text, (775, 415))
    else:
        # Render the graph and energy bar
        render_graph(screen, G, font, path, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_clicked_grafos_euler_2 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        render_main_menu_button(screen, font_small_buttons)

        render_seed_counter(screen,font,missing_nodes,Euler2Seed())

        render_dialog(screen, "¿Qué querés saber?", font)

        if won_level:
            flower.update_animation()
            flower.draw(screen, 1200, 300)
        else:
            dead_flower.update_animation()
            dead_flower.draw(screen, 1200, 300)

    # Check if time is up
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Reset the color of nodes
        return False

    return False


def handle_grafos_euler_2_mousedown(event, go_to_map):
    global back_button_clicked_grafos_euler_2, start_button_clicked_grafos_euler_2, restart_button_clicked_grafos_euler_2, timer_started
    if back_button_clicked_grafos_euler_2 is not None and back_button_clicked_grafos_euler_2.collidepoint(event.pos):
        timer_started = False
        go_to_map()
        reset_nodes(path)
    elif start_button_clicked_grafos_euler_2 is not None and start_button_clicked_grafos_euler_2.collidepoint(event.pos):
        timer_started = True
    elif restart_button_clicked_grafos_euler_2 is not None and restart_button_clicked_grafos_euler_2.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)


def reset_nodes(path):
    global current_node,G, seeds, missing_nodes
    path.clear()
    current_node = None
    seeds = {
        'A': Euler2Seed(),
        'B': Euler2Seed(),
        'C': Euler2Seed(),
        'D': Euler2Seed(),
        'E': Euler2Seed(),
        'F': Euler2Seed(),
        'G': Euler2Seed(),
        'H': Euler2Seed()
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)
    
    missing_nodes = len(positions)


def handle_grafos_euler_2_keydown(event):
    global current_node, seeds, won_level, G, missing_nodes
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()
        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Euler2SeedDisabled()
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Euler2SeedDisabled()
            missing_nodes -= 1

            if current_node == end_node and len(path) == len(G.nodes):
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")
                return True, current_node
    return False, current_node
