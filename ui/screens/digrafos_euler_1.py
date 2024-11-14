import pygame
import networkx as nx

from ui.animated_sprite import AnimatedSprite
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.digraph_renderer import render_euler_digraph
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.screens.common.seed_counter_renderer import render_seed_counter

G = nx.DiGraph()

positions = {
    'A': (1155, 288-60), 'B': (340, 298-60), 'C': (1334, 515-60), 'D': (930, 385-60),
    'E': (482, 477-60), 'F': (1081, 580-60)
}

seeds = {
    'A': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed", frame_size=(90, 90), frame_count=74),
    'B': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed", frame_size=(90, 90), frame_count=74),
    'C': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed", frame_size=(90, 90), frame_count=74),
    'D': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed", frame_size=(90, 90), frame_count=74),
    'E': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed", frame_size=(90, 90), frame_count=74),
    'F': AnimatedSprite(frame_path="./assets/giphs/bugs/bug-d-euler/d-euler-bug", frame_size=(120, 120), frame_count=74)
}

dead_flower = AnimatedSprite(frame_path="./assets/giphs/flowers-bw/d-euler-flower-bw/d-euler-flower-bw", frame_size=(480, 480), frame_count=74)
flower = AnimatedSprite(frame_path="./assets/giphs/flowers/d-euler-flower/d-euler-flower", frame_size=(480, 480), frame_count=74)

missing_nodes = len(positions)

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('B', 'A'), ('A', 'B'), ('A', 'D'), ('A', 'C'), ('B', 'D'), ('C', 'B'), ('D', 'E'), ('E', 'F')
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

back_button_clicked_digrafos_euler = None
start_button_clicked_digrafos_euler = None
restart_button_clicked_digrafos_euler = None

visited_edges = []

def render_digrafos_euler_1(screen, font):
    from core.fonts import font_small_buttons
    global back_button_clicked_digrafos_euler, start_button_clicked_digrafos_euler, restart_button_clicked_digrafos_euler, timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower, missing_nodes, background_image_win, remaining_time

    current_time = pygame.time.get_ticks()
    if won_level:
        background_image_win = pygame.image.load("assets/final-bg/d-euler.png").convert()
        background_image_win = pygame.transform.scale(background_image_win, (1710, 1034))
        screen.blit(background_image_win, (0, 0))
    elif timer_started:
        background_image = pygame.image.load("assets/initial-bg/d-euler.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
    else:
        background_image = pygame.image.load("assets/blur/d-euler.png").convert()
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

    back_button_clicked_digrafos_euler = render_map_button(screen, font_small_buttons)

    if not timer_started:
        start_button_text = font_small_buttons.render("Start", True, (255, 255, 255))
        start_button_clicked_digrafos_euler = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_digrafos_euler)
        screen.blit(start_button_text, (775, 415))
    else:
        # Render the graph and energy bar
        render_euler_digraph(screen, G, font, remaining_time, visited_edges, start_node, end_node, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_clicked_grafos_euler_2 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        render_main_menu_button(screen, font_small_buttons)

        render_seed_counter(screen,font,missing_nodes, AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed.png", frame_size=(90, 90), frame_count=74))

        render_dialog(screen, "¿Qué querés saber?", font)

        if won_level:
            flower.update_animation()
            flower.draw(screen, 1250, 470)
        else:
            dead_flower.update_animation()
            dead_flower.draw(screen, 1250, 470)

    # Check if time is up
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Reset the color of nodes
        return False


    return False

def handle_grafos_digrafos_euler_mousedown(event, go_to_map):
    global back_button_clicked_digrafos_euler, start_button_clicked_digrafos_euler,restart_button_clicked_digrafos_euler, timer_started
    if back_button_clicked_digrafos_euler is not None and back_button_clicked_digrafos_euler.collidepoint(event.pos):
        timer_started = False
        go_to_map()
        reset_nodes(path)
    elif start_button_clicked_digrafos_euler is not None and start_button_clicked_digrafos_euler.collidepoint(event.pos):
        timer_started = True
    elif restart_button_clicked_digrafos_euler is not None and restart_button_clicked_digrafos_euler.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)

def handle_digrafos_euler_1_keydown(event):
    global current_node, seeds, won_level, G, missing_nodes, visited_edges
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                path.append(current_node)
            elif key in G.neighbors(current_node):
                # Verifica si la arista entre `current_node` y `key` ya ha sido visitada
                edge = (current_node, key)
                if edge not in visited_edges:
                    visited_edges.append(edge)  # Marca la arista como visitada
                    path.append(key)  # Agrega el nodo al camino
                    current_node = key
                    missing_nodes -= 1

                    # Revisa si completaste el camino de Euler
                    if current_node == end_node and len(visited_edges) == len(G.edges):
                        won_level = True
                        print("¡Felicidades! Has completado el Camino de Euler.")
                        return True, current_node
            else:
                print("Movimiento no permitido: no se puede usar la misma arista dos veces.")
    return False, current_node

def reset_nodes(path):
    global current_node, G, seeds, missing_nodes, visited_edges
    path.clear()
    current_node = None
    visited_edges.clear()  # Reinicia las aristas visitadas

    seeds = {
        'A': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed.png", frame_size=(90, 90), frame_count=74),
        'B': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed.png", frame_size=(90, 90), frame_count=74),
        'C': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed.png", frame_size=(90, 90), frame_count=74),
        'D': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed.png", frame_size=(90, 90), frame_count=74),
        'E': AnimatedSprite(frame_path="./assets/giphs/seeds/d-euler-seed/d-euler-seed.png", frame_size=(90, 90), frame_count=74),
        'F': AnimatedSprite(frame_path="./assets/giphs/bugs/bug-d-euler/d-euler-bug.png", frame_size=(90, 90), frame_count=74)
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

    missing_nodes = len(positions)
