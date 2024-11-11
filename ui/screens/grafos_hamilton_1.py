import os

import pygame
import networkx as nx

from ui.characters.frog_neutral import FrogNeutral
from ui.flowers.hamilton_1_flower import Hamilton1Flower
from ui.flowers.black_white.hamilton_1_flower_black_white import Hamilton1FlowerBlackWhite
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_graph
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.seeds.disabled.hamilton_1_seed_disabled import Hamilton1SeedDisabled
from ui.seeds.enabled.hamilton_1_seed import Hamilton1Seed

G = nx.Graph()
# restarle 60 a y
positions = {
    'A': (433, 512-60),
    'B': (251, 360-60),
    'C': (584, 233-60),
    'D': (819, 446-60),
    'E': (955, 538-60),
    'F': (1145, 315-60),
    'G': (1419, 315-60),
    'H': (1293, 430-60)
}

seeds = {
    'A': Hamilton1Seed(),
    'B': Hamilton1Seed(),
    'C': Hamilton1Seed(),
    'D': Hamilton1Seed(),
    'E': Hamilton1Seed(),
    'F': Hamilton1Seed(),
    'G': Hamilton1Seed(),
    'H': Hamilton1Seed()
}

dead_flower = Hamilton1FlowerBlackWhite()
flower = Hamilton1Flower()

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(200, 0, 0))

edges = [
    ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'E'), ('C', 'D'),
    ('C', 'F'), ('D', 'F'), ('F', 'E'), ('F', 'H'), ('E', 'G'), ('G', 'H')
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

back_button_clicked_grafos_hamilton_1 = None
start_button_clicked_grafos_hamilton_1 = None
restart_button_clicked_grafos_hamilton_1 = None


def render_grafos_hamilton_1(screen, font):
    from graph import font_small_buttons
    global back_button_clicked_grafos_hamilton_1, start_button_clicked_grafos_hamilton_1, restart_button_clicked_grafos_hamilton_1,timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower

    current_time = pygame.time.get_ticks()
    if timer_started:
        background_image = pygame.image.load("assets/initial-bg/hamilton-1.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
    else:
        background_image = pygame.image.load("assets/blur/hamilton-1.png").convert()
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
    back_button_clicked_grafos_hamilton_1 = render_map_button(screen, font_small_buttons)

    if not timer_started:
        start_button_text = font_small_buttons.render("Start", True, (255, 255, 255))
        start_button_clicked_grafos_hamilton_1 = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_grafos_hamilton_1)
        screen.blit(start_button_text, (775, 415))
    else:
        # Render the graph and energy bar
        render_graph(screen, G, font, path, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_clicked_grafos_hamilton_1 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        render_main_menu_button(screen, font_small_buttons)

        render_dialog(screen, "¿Qué querés saber?", font, FrogNeutral())

        dead_flower.update_animation()
        dead_flower.draw(screen, 1200, 500)

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

def handle_grafos_hamilton_1_mousedown(event, go_to_map):
    global back_button_clicked_grafos_hamilton_1, start_button_clicked_grafos_hamilton_1, restart_button_clicked_grafos_hamilton_1, timer_started
    if back_button_clicked_grafos_hamilton_1 is not None and back_button_clicked_grafos_hamilton_1.collidepoint(event.pos):
        timer_started = False
        go_to_map()
        reset_nodes(path)
    elif start_button_clicked_grafos_hamilton_1 is not None and start_button_clicked_grafos_hamilton_1.collidepoint(event.pos):
        timer_started = True
    elif restart_button_clicked_grafos_hamilton_1 is not None and restart_button_clicked_grafos_hamilton_1.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)

def reset_nodes(path):
    global current_node,G, seeds
    path.clear()
    current_node = None
    seeds = {
        'A': Hamilton1Seed(),
        'B': Hamilton1Seed(),
        'C': Hamilton1Seed(),
        'D': Hamilton1Seed(),
        'E': Hamilton1Seed(),
        'F': Hamilton1Seed(),
        'G': Hamilton1Seed(),
        'H': Hamilton1Seed()
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

def handle_grafos_hamilton_1_keydown(event):
    global current_node, seeds, won_level
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Hamilton1SeedDisabled()
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Hamilton1SeedDisabled()

            if current_node == end_node and len(path) == len(G.nodes):
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")
                return True, current_node
    return False, current_node
