import pygame
import networkx as nx

from ui.characters.frog_neutral import FrogNeutral
from ui.flowers.hamilton_3_flower import Hamilton3Flower
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_graph
from ui.seeds.disabled.hamilton_3_seed_disabled import Hamilton3SeedDisabled
from ui.seeds.enabled.hamilton_3_seed import Hamilton3Seed

G = nx.Graph()
positions = {
    'A': (1010, 525), 'B': (1500, 465), 'C': (1105, 218), 'D': (1200, 597),
    'E': (1247, 429), 'F': (932, 255), 'G': (824, 383), 'H': (1357, 280),
    'I': (804, 570), 'J': (481, 395), 'K': (363, 240), 'L': (741, 204),
    'M': (575, 314), 'N': (573, 601), 'O': (347, 485), 'P': (221, 394)
}

seeds = {
    'A': Hamilton3Seed(), 'B': Hamilton3Seed(), 'C': Hamilton3Seed(), 'D': Hamilton3Seed(),
    'E': Hamilton3Seed(), 'F': Hamilton3Seed(), 'G': Hamilton3Seed(), 'H': Hamilton3Seed(),
    'I': Hamilton3Seed(), 'J': Hamilton3Seed(), 'K': Hamilton3Seed(), 'L': Hamilton3Seed(),
    'M': Hamilton3Seed(), 'N': Hamilton3Seed(), 'O': Hamilton3Seed(), 'P': Hamilton3Seed()
}
flower = Hamilton3Flower()
for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('O', 'P'), ('J', 'K'), ('L', 'K'), ('L', 'M'), ('L', 'G'),
    ('F', 'G'), ('C', 'D'), ('B', 'C'), ('A', 'B'),
    ('E', 'D'), ('I', 'D'), ('O', 'I'), ('N', 'G'), ('O', 'N'),
    ('O', 'J'), ('M', 'N'), ('M', 'I'), ('I', 'J'), ('E', 'J'),
    ('A', 'F'), ('C', 'D'), ('H', 'I'), ('E', 'F'), ('G', 'H'),
    ('B', 'E')
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

back_button_clicked_grafos_hamilton_3 = None
start_button_clicked_grafos_hamilton_3 = None
restart_button_clicked_grafos_hamilton_3 = None

def render_grafos_hamilton_3(screen, font):
    from graph import fontButtons
    global back_button_clicked_grafos_hamilton_3, start_button_clicked_grafos_hamilton_3, restart_button_clicked_grafos_hamilton_3, timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower

    current_time = pygame.time.get_ticks()
    if timer_started:
        background_image = pygame.image.load("assets/initial-bg/hamilton-3.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
    else:
        background_image = pygame.image.load("assets/blur/hamilton-3.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        start_time = pygame.time.get_ticks()
        remaining_time = 60000

    # Update energy based on remaining time
    if remaining_time > 0:
        energy = initial_energy * (remaining_time / timer_duration)
    else:
        energy = initial_energy  # Reset energy if time runs out

    # Dibujar el botón "Back"
    back_button_text = font.render("Back", True, (255, 255, 255))
    back_button_clicked_grafos_hamilton_3 = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_clicked_grafos_hamilton_3)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón

    if not timer_started:
        start_button_text = fontButtons.render("Start", True, (255, 255, 255))
        start_button_clicked_grafos_hamilton_3 = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_grafos_hamilton_3)
        screen.blit(start_button_text, (775, 415))
    else:
        # Render the graph and energy bar
        render_graph(screen, G, font, path, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_text = fontButtons.render("RESTART", True, (0, 0, 0))
        restart_button_clicked_grafos_hamilton_3 = pygame.Rect(1420, 85, 200, 60)
        pygame.draw.rect(screen, (0, 0, 0), restart_button_clicked_grafos_hamilton_3, width=5, border_radius=15)
        screen.blit(restart_button_text, (1430, 95))

    render_dialog(screen, "¿Qué querés saber?", font, FrogNeutral())

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
        flower.draw(screen, 1450, 780)

    return False

def handle_grafos_hamilton_3_mousedown(event, go_to_map):
    global back_button_clicked_grafos_hamilton_3, start_button_clicked_grafos_hamilton_3, restart_button_clicked_grafos_hamilton_3, timer_started
    if back_button_clicked_grafos_hamilton_3 is not None and back_button_clicked_grafos_hamilton_3.collidepoint(event.pos):
        timer_started = False
        go_to_map()
        reset_nodes(path)
    elif start_button_clicked_grafos_hamilton_3 is not None and start_button_clicked_grafos_hamilton_3.collidepoint(event.pos):
        timer_started = True
    elif restart_button_clicked_grafos_hamilton_3 is not None and restart_button_clicked_grafos_hamilton_3.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)

def reset_nodes(path):
    global current_node,G, seeds
    path.clear()
    current_node = None
    seeds = {
        'A': Hamilton3Seed(), 'B': Hamilton3Seed(), 'C': Hamilton3Seed(), 'D': Hamilton3Seed(),
        'E': Hamilton3Seed(), 'F': Hamilton3Seed(), 'G': Hamilton3Seed(), 'H': Hamilton3Seed(),
        'I': Hamilton3Seed(), 'J': Hamilton3Seed(), 'K': Hamilton3Seed(), 'L': Hamilton3Seed(),
        'M': Hamilton3Seed(), 'N': Hamilton3Seed(), 'O': Hamilton3Seed(), 'P': Hamilton3Seed()
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

def handle_grafos_hamilton_3_keydown(event):
    global current_node, seeds, won_level
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Hamilton3SeedDisabled()
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Hamilton3SeedDisabled()

            if current_node == end_node and len(path) == len(G.nodes):
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")
                return True, current_node
    return False, current_node
