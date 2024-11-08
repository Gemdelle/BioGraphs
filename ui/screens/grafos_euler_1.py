import pygame
import networkx as nx

from ui.characters.frog_neutral import FrogNeutral
from ui.flowers.euler_1_flower import Euler1Flower
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_graph
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.seeds.disabled.euler_1_seed_disabled import Euler1SeedDisabled
from ui.seeds.enabled.euler_1_seed import Euler1Seed
import warnings
warnings.filterwarnings("ignore")

G = nx.Graph()
positions = {
    'A': (891, 254-60), 'B': (1339, 371-60), 'C': (1447, 546-60), 'D': (752, 595-60),
    'E': (235, 525-60), 'F': (484, 410-60)
}
seeds = {
    'A': Euler1Seed(), 'B': Euler1Seed(), 'C': Euler1Seed(), 'D': Euler1Seed(),
    'E': Euler1Seed(), 'F': Euler1Seed()
}

flower = Euler1Flower()

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('A', 'B'),('B', 'C'),('C', 'D'),('B', 'D'),('A', 'D'),('F', 'D'),('A', 'F'),('D', 'E')
]

for edge in edges:
    G.add_edge(edge[0], edge[1])

start_node = None
end_node = 'E'
path = []
timer_started = False
start_time = 0

current_node = None
won_level = False

initial_energy = 17
energy = initial_energy  # Starting energy level
start_ticks = pygame.time.get_ticks()  # Start time for timer
timer_duration = 60000  # 60 seconds duration

back_button_clicked_grafos_euler_1 = None
start_button_clicked_grafos_euler_1 = None
restart_button_clicked_grafos_euler_1 = None

def render_grafos_euler_1(screen, font):
    from graph import fontButtons
    global back_button_clicked_grafos_euler_1, start_button_clicked_grafos_euler_1,restart_button_clicked_grafos_euler_1, timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower

    current_time = pygame.time.get_ticks()
    if timer_started:
        background_image = pygame.image.load("assets/initial-bg/euler-1.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
    else:
        background_image = pygame.image.load("assets/blur/euler-1.png").convert()
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
    back_button_clicked_grafos_euler_1 = render_map_button(screen, font, fontButtons)

    if not timer_started:
        start_button_text = fontButtons.render("Start", True, (255, 255, 255))
        start_button_clicked_grafos_euler_1 = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_grafos_euler_1)
        screen.blit(start_button_text, (775, 415))
    else:
        # Render the graph
        render_graph(screen, G, font, path, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_clicked_grafos_euler_1 = render_restart_button(screen, font, fontButtons)

        # Draw the "Main Menu" button
        render_main_menu_button(screen, font, fontButtons)

        render_dialog(screen, "¿Qué querés saber?", font, FrogNeutral())


    # Check if time is up
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Reset the color of nodes

    if won_level:
        flower.update_animation()
        flower.draw(screen, 1450, 780)

    return False

def handle_grafos_euler_1_mousedown(event, go_to_map):
    global back_button_clicked_grafos_euler_1, start_button_clicked_grafos_euler_1, restart_button_clicked_grafos_euler_1, timer_started
    if back_button_clicked_grafos_euler_1 is not None and back_button_clicked_grafos_euler_1.collidepoint(event.pos):
        timer_started = False
        go_to_map()
        reset_nodes(path)
    elif start_button_clicked_grafos_euler_1 is not None and start_button_clicked_grafos_euler_1.collidepoint(event.pos):
        timer_started = True
    elif restart_button_clicked_grafos_euler_1 is not None and restart_button_clicked_grafos_euler_1.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)

def reset_nodes(path):
    global current_node,G, seeds
    path.clear()
    current_node = None
    seeds = {
        'A': Euler1Seed(), 'B': Euler1Seed(), 'C': Euler1Seed(), 'D': Euler1Seed(),
        'E': Euler1Seed(), 'F': Euler1Seed()
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

def handle_grafos_euler_1_keydown(event):
    global current_node, seeds, won_level, G
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()
        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Euler1SeedDisabled()
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = Euler1SeedDisabled()

            if current_node == end_node and len(path) == len(G.nodes):
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")

                return True, current_node
    return False, current_node
