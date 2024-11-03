import pygame
import networkx as nx

from ui.screens.graph_renderer import render_graph

G = nx.Graph()

positions = {
    'A': (833, 225), 'B': (680, 372), 'C': (833, 372), 'D': (970, 372), 'E': (833, 670)
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

initial_energy = 17
energy = initial_energy  # Starting energy level
start_ticks = pygame.time.get_ticks()  # Start time for timer
timer_duration = 60000  # 60 seconds duration

back_button_clicked_intro_euler_cicle = None

def render_intro_euler_cicle(screen, font):
    global back_button_clicked_intro_euler_cicle
    background_image = pygame.image.load("assets/pg-1.png").convert()
    background_image = pygame.image.load("assets/default-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    global timer_started, start_time, path, start_node, positions, current_node, energy

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
    pygame.draw.rect(screen, (200, 0, 0), (160, 80, int(energy * 40), 50))

    # Draw the timer text
    timer_text = font.render(f"{remaining_time // 1000}", True, (0, 0, 0))
    screen.blit(timer_text, (100, 100))

    # Dibujar el botón "Back"
    back_button_text = font.render("Back", True, (255, 255, 255))
    back_button_clicked_intro_euler_cicle = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_clicked_intro_euler_cicle)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón

    # Check if time is up
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Reset the color of nodes

    return False


def is_back_button_clicked_intro_euler_cicle(event):
    global back_button_clicked_intro_euler_cicle
    return back_button_clicked_intro_euler_cicle is not None and back_button_clicked_intro_euler_cicle.collidepoint(event.pos)




