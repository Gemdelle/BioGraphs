import pygame
import networkx as nx

from ui.animated_sprite import AnimatedSprite
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.graph_renderer import render_simple_node_graph

G = nx.Graph()

positions = {
    'A': (1034, 147-60), 'B': (811, 223-60), 'C': (935, 311-60), 'D': (1072, 370-60), 'E': (768, 599-60)
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
    ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('C', 'D'), ('B', 'E'), ('C', 'E'), ('D', 'E')
]

for edge in edges:
    G.add_edge(edge[0], edge[1])

start_node = None
end_node = 'H'
path = []
timer_started = False
start_time = 0

current_node = None

back_button_clicked_playground_1 = None
restart_button_clicked_playground_1 = None

def render_playground_1(screen, font):
    from core.fonts import font_buttons
    global back_button_clicked_playground_1, restart_button_clicked_playground_1
    background_image = pygame.image.load("assets/playground-bg/bg-level-1.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    global timer_started, start_time, path, start_node, positions, current_node, energy

    render_simple_node_graph(screen, G, font, path, positions, clovers)

    # Dibujar el botón "Back"
    back_button_text = font.render("Back", True, (255, 255, 255))
    back_button_clicked_playground_1 = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_clicked_playground_1)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón

    # Draw the "Restart" button
    restart_button_text = font_buttons.render("RESTART", True, (0, 0, 0))
    restart_button_clicked_playground_1 = pygame.Rect(1420, 85, 200, 60)
    pygame.draw.rect(screen, (0, 0, 0), restart_button_clicked_playground_1, width=5, border_radius=15)
    screen.blit(restart_button_text, (1430, 95))

    render_dialog(screen, "¿Qué querés saber?", font)

    return False


def handle_playground_1_mousedown(event, go_to_playground):
    global back_button_clicked_playground_1, restart_button_clicked_playground_1, timer_started, path, current_node
    if back_button_clicked_playground_1 is not None and back_button_clicked_playground_1.collidepoint(event.pos):
        go_to_playground()
        reset_nodes(path)
    elif restart_button_clicked_playground_1 is not None and restart_button_clicked_playground_1.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)


def reset_nodes(path):
    global current_node,G
    path.clear()
    current_node = None
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)


def handle_playground_1_keydown(event):
    global current_node
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)

            if current_node == end_node and len(path) == len(G.nodes):
                print("Congratulations! You completed the Hamiltonian Path.")
                return True, current_node
    return False, current_node



