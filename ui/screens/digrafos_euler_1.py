import pygame
import networkx as nx

from ui.screens.graph_renderer import render_graph

G = nx.Graph()
positions = {
    'A': (100, 300), 'B': (50, 100), 'C': (200, 100), 'D': (150, 250),
    'E': (50, 400), 'F': (150, 450), 'G': (250, 400), 'H': (300, 300)
}
for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

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

initial_energy = 17
energy = initial_energy  # Starting energy level
start_ticks = pygame.time.get_ticks()  # Start time for timer
timer_duration = 60000  # 60 seconds duration

back_button_clicked_digrafos_euler = None

def render_digrafos_euler_1(screen, font):
    global timer_started, start_time, path, start_node, positions, current_node, energy
    background_image = pygame.image.load("assets/D-euler.png").convert()
    # background_image = pygame.image.load("assets/default-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    if not timer_started:
        start_time = pygame.time.get_ticks()
        timer_started = True

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)

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
    back_button_rect = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_rect)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón

    # Check if time is up
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Reset the color of nodes
        return False

    return False

def is_back_button_clicked_digrafos_euler(event):
    global back_button_clicked_digrafos_euler
    return back_button_clicked_digrafos_euler is not None and back_button_clicked_digrafos_euler.collidepoint(event.pos)

def handle_digrafos_euler_1_keydown(event):
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
