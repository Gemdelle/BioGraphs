import pygame
import networkx as nx

from ui.characters.frog_neutral import FrogNeutral
from ui.flowers.d_euler_1_flower import DEuler1Flower
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.digraph_renderer import render_digraph
from ui.seeds.disabled.digrafos_euler_1_seed_disabled import DigrafosEuler1SeedDisabled
from ui.seeds.enabled.digrafos_euler_1_seed import DigrafosEuler1Seed

G = nx.DiGraph()
positions = {
    'A': (1209, 335), 'B': (272, 283), 'C': (1407, 601), 'D': (853, 527),
    'E': (478, 557), 'F': (1078, 678)
}

seeds = {
    'A': DigrafosEuler1Seed(), 'B': DigrafosEuler1Seed(), 'C': DigrafosEuler1Seed(), 'D': DigrafosEuler1Seed(),
    'E': DigrafosEuler1Seed(), 'F': DigrafosEuler1Seed()
}

flower = DEuler1Flower()

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
def render_digrafos_euler_1(screen, font):
    from graph import fontButtons
    global back_button_clicked_digrafos_euler, start_button_clicked_digrafos_euler, restart_button_clicked_digrafos_euler, timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower

    current_time = pygame.time.get_ticks()
    if timer_started:
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


    # Dibujar el botón "Back"
    back_button_text = font.render("Back", True, (255, 255, 255))
    back_button_clicked_digrafos_euler = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_clicked_digrafos_euler)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón

    if not timer_started:
        start_button_text = fontButtons.render("Start", True, (255, 255, 255))
        start_button_clicked_digrafos_euler = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_digrafos_euler)
        screen.blit(start_button_text, (775, 415))
    else:
        # Render the graph and energy bar
        render_digraph(screen, G, font, remaining_time, path, start_node, end_node, positions, seeds)

        # Draw the energy bar
        pygame.draw.rect(screen, (200, 0, 0), (10, 10, int(energy * 20), 20))

        # Draw the timer text
        timer_text = font.render(f"Time: {remaining_time // 1000}s", True, (0, 0, 0))
        screen.blit(timer_text, (10, 40))
        # Draw the "Restart" button
        restart_button_text = fontButtons.render("RESTART", True, (0, 0, 0))
        restart_button_clicked_digrafos_euler = pygame.Rect(1420, 85, 200, 60)
        pygame.draw.rect(screen, (0, 0, 0), restart_button_clicked_digrafos_euler, width=5, border_radius=15)
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

def reset_nodes(path):
    global current_node
    path.clear()
    current_node = None
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

def handle_digrafos_euler_1_keydown(event):
    global current_node, seeds, won_level
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
                seeds[current_node] = DigrafosEuler1SeedDisabled()

                if current_node == end_node and len(path) == len(G.nodes):
                    won_level = True
                    print("Congratulations! You completed the Hamiltonian Path.")
                    return True, current_node
    return False, current_node
