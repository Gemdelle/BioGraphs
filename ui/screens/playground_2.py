import pygame
import networkx as nx

from ui.screens.graph_renderer import render_graph

G = nx.Graph()

positions = {
    'A': (854, 683),
    'B': (854, 470),
    'C': (692, 518),
    'D': (591, 395),
    'E': (720, 397),
    'F': (781, 320),
    'G': (854, 213),
    'H': (930, 320),
    'I': (978, 397),
    'J': (1123, 395),
    'K': (1020, 518)
}


for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'B'), ('B', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'B'),
    ('B', 'I'), ('I', 'J'), ('J', 'K'), ('B', 'K')
]

for edge in edges:
    G.add_edge(edge[0], edge[1])

start_node = None
end_node = 'H'
path = []
timer_started = False
start_time = 0

current_node = None

back_button_clicked_playground_2 = None


def render_playground_2(screen, font):
    global back_button_clicked_playground_2
    background_image = pygame.image.load("assets/pg-2.png").convert()
    background_image = pygame.image.load("assets/default-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    global timer_started, start_time, path, start_node, positions, current_node, energy

    # Render the graph and energy bar
    render_graph(screen, G, font, path, positions)

    # Dibujar el botón "Back"
    back_button_text = font.render("Back", True, (255, 255, 255))
    back_button_clicked_playground_2 = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_clicked_playground_2)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón
    return False


def is_back_button_clicked_playground_2(event):
    global back_button_clicked_playground_2
    return back_button_clicked_playground_2 is not None and back_button_clicked_playground_2.collidepoint(event.pos)


def handle_playground_2_keydown(event):
    global current_node
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)

                if current_node == end_node and len(path) == len(G.nodes):
                    print("Congratulations! You completed the Hamiltonian Path.")
                    return True, current_node
    return False, current_node
