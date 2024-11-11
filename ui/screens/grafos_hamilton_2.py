import os

import pygame
import networkx as nx

from ui.characters.frog_neutral import FrogNeutral
from ui.flowers.hamilton_2_flower import Hamilton2Flower
from ui.flowers.black_white.hamilton_2_flower_black_white import Hamilton2FlowerBlackWhite
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_graph
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.seeds.disabled.hamilton_2_seed_disabled import Hamilton2SeedDisabled
from ui.seeds.enabled.hamilton_2_seed import Hamilton2Seed

G = nx.Graph()
positions = {
    'A': (507,397-60), 'B': (379,575-60), 'C': (598,274-60), 'D': (765,496-60),
    'E': (230,465-60), 'F': (334,304-60), 'G': (1080,268-60), 'H': (805,314-60),
    'I': (1015,615-60), 'J': (1376,320-60), 'K': (1138,437-60), 'L': (1225,632-60),
}

seeds = {
    'A': Hamilton2Seed(), 'B': Hamilton2Seed(), 'C': Hamilton2Seed(), 'D': Hamilton2Seed(),
    'E': Hamilton2Seed(), 'F': Hamilton2Seed(), 'G': Hamilton2Seed(), 'H': Hamilton2Seed(),
    'I': Hamilton2Seed(), 'J': Hamilton2Seed(), 'K': Hamilton2Seed(), 'L': Hamilton2Seed(),
}

dead_flower = Hamilton2FlowerBlackWhite()
flower = Hamilton2Flower()

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


def render_grafos_hamilton_2(screen, font):
    from graph import font_small_buttons
    global back_button_clicked_grafos_hamilton_2, start_button_clicked_grafos_hamilton_2, restart_button_clicked_grafos_hamilton_2, timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower

    current_time = pygame.time.get_ticks()
    if timer_started:
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
        start_button_text = font_small_buttons.render("Start", True, (255, 255, 255))
        start_button_clicked_grafos_hamilton_2 = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_grafos_hamilton_2)
        screen.blit(start_button_text, (775, 415))
    else:
        # Render the graph and energy bar
        render_graph(screen, G, font, path, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_clicked_grafos_hamilton_2 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        render_main_menu_button(screen, font_small_buttons)

        render_dialog(screen, "¿Qué querés saber?", font, FrogNeutral())

        dead_flower.update_animation()
        dead_flower.draw(screen, 1250, 500)

    # Check if time is up
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Reset the color of nodes
        return False
    if won_level:
        flower.update_animation()
        flower.draw(screen, 1200, 500)

    return False


def handle_grafos_hamilton_2_mousedown(event, go_to_map):
    global back_button_clicked_grafos_hamilton_2, start_button_clicked_grafos_hamilton_2, restart_button_clicked_grafos_hamilton_2, timer_started
    if back_button_clicked_grafos_hamilton_2 is not None and back_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = False
        go_to_map()
        reset_nodes(path)
    elif start_button_clicked_grafos_hamilton_2 is not None and start_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = True
    elif restart_button_clicked_grafos_hamilton_2 is not None and restart_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = True
        reset_nodes(path)


def reset_nodes(path):
    global current_node,G, seeds
    path.clear()
    current_node = None
    seeds = {
        'A': Hamilton2Seed(), 'B': Hamilton2Seed(), 'C': Hamilton2Seed(), 'D': Hamilton2Seed(),
        'E': Hamilton2Seed(), 'F': Hamilton2Seed(), 'G': Hamilton2Seed(), 'H': Hamilton2Seed(),
        'I': Hamilton2Seed(), 'J': Hamilton2Seed(), 'K': Hamilton2Seed(), 'L': Hamilton2Seed(),
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)


def handle_grafos_hamilton_2_keydown(event):
    global current_node, seeds, won_level
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Hamilton2SeedDisabled()
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Hamilton2SeedDisabled()

            if current_node == end_node and len(path) == len(G.nodes):
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")
                return True, current_node
    return False, current_node
