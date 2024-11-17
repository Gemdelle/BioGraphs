import pygame
import networkx as nx

from ui.animated_sprite import AnimatedSprite
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.graph_renderer import render_simple_node_graph
from core.fonts import *
from ui.screens.common.main_menu_button_renderer import render_main_menu_button, render_playground_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button, render_playground_map_button
from ui.screens.common.restart_button_renderer import render_playground_restart_button, render_restart_button

G = nx.Graph()

positions = {
    'A': (557, 406-60), 'B': (914, 158-60), 'C': (1266, 406-60), 'D': (1266, 684-60), 'E': (557, 684-60)
}

clovers = {
    'A': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(110, 110), frame_count=625),
    'B': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(110, 110), frame_count=625),
    'C': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(110, 110), frame_count=625),
    'D': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(110, 110), frame_count=625),
    'E': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-end/clover-end", frame_size=(110, 110), frame_count=625)
}

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A'), ('A', 'D'), ('A', 'C')
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
missing_nodes = len(clovers)

back_button_clicked_playground_5 = None
restart_button_clicked_playground_5 = None
main_menu_button_clicked_playground_5 = None

def render_playground_5(screen, font):
    from core.fonts import font_buttons
    global back_button_clicked_playground_5, restart_button_clicked_playground_5
    background_image = pygame.image.load("assets/playground-bg/bg-level-5.png").convert()
    #background_image = pygame.image.load("assets/default-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    global timer_started, start_time, path, start_node, positions, current_node, energy

    # Render the graph and energy bar
    render_simple_node_graph(screen, G, font, path, positions, clovers)

# Draw the "Back" button
    back_button_clicked_playground_5 = render_playground_map_button(screen, font_small_buttons)

    # Draw the "Restart" button
    restart_button_clicked_playground_5 = render_playground_restart_button(screen, font_small_buttons)

    # Draw the "Main Menu" button
    main_menu_button_clicked_playground_5 = render_playground_main_menu_button(screen, font_small_buttons)

    render_dialog(screen, "¿Qué querés saber?", font)

    return False

def handle_playground_5_mousedown(event, go_to_playground):
    global back_button_clicked_playground_5, restart_button_clicked_playground_5, timer_started, path, current_node
    if back_button_clicked_playground_5 is not None and back_button_clicked_playground_5.collidepoint(event.pos):
        go_to_playground()
        reset_nodes(path)
    elif restart_button_clicked_playground_5 is not None and restart_button_clicked_playground_5.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)

def reset_nodes(path):
    global current_node,G
    path.clear()
    current_node = None
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

def handle_playground_5_keydown(event):
    global current_node, clovers, won_level, G, missing_nodes
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()
        if key in G.nodes:
                current_node = key
                path.append(current_node)
                clovers[current_node] = AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=626)
                missing_nodes -= 1

                if current_node == end_node and len(path) == len(G.nodes):
                    won_level = True
                    print("Congratulations! You completed the Hamiltonian Path.")

                return True, current_node
    return False, current_node



