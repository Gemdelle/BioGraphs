import pygame
import networkx as nx

from ui.screens.graph_renderer import render_graph

G = nx.Graph()
positions = {
    'A': (560,470-60), 'B': (311,704-60), 'C': (558,327-60), 'D': (775,576-60),
    'E': (195,519-60), 'F': (360,434-60), 'G': (1095,308-60), 'H': (711,431-60),
    'I': (1033,705-60), 'J': (1416,360-60), 'K': (1160,508-60), 'L': (1521,698-60),
}
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

initial_energy = 17
energy = initial_energy  # Starting energy level
start_ticks = pygame.time.get_ticks()  # Start time for timer
timer_duration = 60000  # 60 seconds duration

back_button_clicked_grafos_hamilton_2 = None
start_button_clicked_grafos_hamilton_2 = None
def render_grafos_hamilton_2(screen, font):
    from graph import fontButtons
    global back_button_clicked_grafos_hamilton_2, start_button_clicked_grafos_hamilton_2, timer_started, start_time, path, start_node, positions, current_node, energy
    background_image = pygame.image.load("assets/G-hamilton-2.png").convert()
    background_image = pygame.image.load("assets/default-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))
    current_time = pygame.time.get_ticks()
    if timer_started:
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
    else:
        start_time = pygame.time.get_ticks()
        remaining_time = 60000

    # Update energy based on remaining time
    if remaining_time > 0:
        energy = initial_energy * (remaining_time / timer_duration)
    else:
        energy = initial_energy  # Reset energy if time runs out

    # Render the graph and energy bar
    render_graph(screen, G, font, remaining_time, path, start_node, end_node, positions)

    # Draw the energy bar
    pygame.draw.rect(screen, (200, 0, 0), (10, 10, int(energy * 20), 20))

    # Draw the timer text
    timer_text = font.render(f"Time: {remaining_time // 1000}s", True, (0, 0, 0))
    screen.blit(timer_text, (10, 40))

    # Dibujar el botón "Back"
    back_button_text = font.render("Back", True, (255, 255, 255))
    back_button_clicked_grafos_hamilton_2 = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_clicked_grafos_hamilton_2)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón

    if not timer_started:
        graph_frame_blur_image = pygame.image.load("assets/UB_logo.jpg").convert()
        graph_frame_blur_image = pygame.transform.scale(graph_frame_blur_image, (1500, 500))
        screen.blit(graph_frame_blur_image, (100, 200))

        start_button_text = fontButtons.render("Start", True, (255, 255, 255))
        start_button_clicked_grafos_hamilton_2 = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_grafos_hamilton_2)
        screen.blit(start_button_text, (775, 415))

    # Check if time is up
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Reset the color of nodes
        return False

    return False
def handle_grafos_hamilton_2_mousedown(event, go_to_map):
    global back_button_clicked_grafos_hamilton_2, start_button_clicked_grafos_hamilton_2, timer_started
    if back_button_clicked_grafos_hamilton_2 is not None and back_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = False
        go_to_map()
    elif start_button_clicked_grafos_hamilton_2 is not None and start_button_clicked_grafos_hamilton_2.collidepoint(event.pos):
        timer_started = True

def handle_grafos_hamilton_2_keydown(event):
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
