import pygame
import networkx as nx

from ui.characters.frog_neutral import FrogNeutral
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.graph_renderer import render_simple_node_graph

G = nx.Graph()
positions = {
    'A': (685, 429), 'B': (851, 242), 'C': (1032, 429), 'D': (1032, 669), 'E': (685, 669)
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

back_button_clicked_playground_5 = None
restart_button_clicked_playground_5 = None
def render_playground_5(screen, font):
    from graph import font_buttons
    global back_button_clicked_playground_5, restart_button_clicked_playground_5
    background_image = pygame.image.load("assets/playground-bg/bg-level-5.png").convert()
    #background_image = pygame.image.load("assets/default-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    global timer_started, start_time, path, start_node, positions, current_node, energy

    # Render the graph and energy bar
    render_simple_node_graph(screen, G, font, path, positions)

    # Dibujar el botón "Back"
    back_button_text = font.render("Back", True, (255, 255, 255))
    back_button_clicked_playground_5 = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_clicked_playground_5)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón

    # Draw the "Restart" button
    restart_button_text = font_buttons.render("RESTART", True, (0, 0, 0))
    restart_button_clicked_playground_5 = pygame.Rect(1420, 85, 200, 60)
    pygame.draw.rect(screen, (0, 0, 0), restart_button_clicked_playground_5, width=5, border_radius=15)
    screen.blit(restart_button_text, (1430, 95))
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



