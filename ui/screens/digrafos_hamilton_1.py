import pygame
import networkx as nx

from ui.characters.frog_neutral import FrogNeutral
from ui.flowers.d_hamilton_1_flower import DHamilton1Flower
from ui.flowers.black_white.d_hamilton_1_flower_black_white import DHamilton1FlowerBlackWhite
from ui.screens.common.dialog_renderer import render_dialog
from ui.screens.common.digraph_renderer import render_digraph
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.seeds.disabled.digrafos_hamilton_1_seed_disabled import DigrafosHamilton1SeedDisabled
from ui.seeds.enabled.digrafos_hamilton_1_seed import DigrafosHamilton1Seed

# Crear un DiGraph para representar el digrafo
G = nx.DiGraph()

# Definir posiciones de los nodos
positions = {
    'A': (802, 447-60), 'B': (850, 270), 'C': (320, 254-60), 'D': (438, 550-60),
    'E': (1099, 617-60), 'F': (616, 393-60), 'G': (1420, 306-60), 'H': (947, 487-60)
}

seeds = {
    'A': DigrafosHamilton1Seed(), 'B': DigrafosHamilton1Seed(), 'C': DigrafosHamilton1Seed(), 'D': DigrafosHamilton1Seed(),
    'E': DigrafosHamilton1Seed(), 'F': DigrafosHamilton1Seed(), 'G': DigrafosHamilton1Seed(), 'H': DigrafosHamilton1Seed()
}

dead_flower = DHamilton1FlowerBlackWhite()
flower = DHamilton1Flower()

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

# Definir múltiples aristas con direcciones específicas para formar un camino hamiltoniano en el digrafo
edges = [
    ('A', 'B'), ('B', 'C'), ('B', 'G'), ('F', 'G'), ('G', 'H'), ('E', 'G'), ('D', 'E'), ('E', 'F'), ('D', 'F'),
    ('C', 'D'), ('C', 'F')
]

for edge in edges:
    G.add_edge(edge[0], edge[1])

# Variables para el juego
start_node = None
end_node = 'J'
path = []
timer_started = False
start_time = 0

current_node = None
won_level = False
initial_energy = 17
energy = initial_energy  # Energía inicial
start_ticks = pygame.time.get_ticks()  # Tiempo de inicio
timer_duration = 60000  # 60 segundos

back_button_clicked_digrafos_hamilton_1 = None
start_button_clicked_digrafos_hamilton_1 = None
restart_button_clicked_digrafos_hamilton_1 = None

# Función de renderizado con flechas en aristas
def render_digrafos_hamilton_1(screen, font, go_to_map, events):
    from graph import font_small_buttons
    global back_button_clicked_digrafos_hamilton_1, start_button_clicked_digrafos_hamilton_1, restart_button_clicked_digrafos_hamilton_1, timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower

    current_time = pygame.time.get_ticks()
    if timer_started:
        background_image = pygame.image.load("assets/initial-bg/d-hamilton.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
    else:
        background_image = pygame.image.load("assets/blur/d-hamilton.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        start_time = pygame.time.get_ticks()
        remaining_time = 60000

    # Actualizar energía en función del tiempo restante
    if remaining_time > 0:
        energy = initial_energy * (remaining_time / timer_duration)
    else:
        energy = initial_energy  # Resetear energía si se acaba el tiempo

    # Draw the "Back" button
    back_button_clicked_digrafos_hamilton_1 = render_map_button(screen, font_small_buttons)

    if not timer_started:
        start_button_text = font_small_buttons.render("Start", True, (255, 255, 255))
        start_button_clicked_digrafos_hamilton_1 = pygame.Rect(750, 400, 160, 80)
        pygame.draw.rect(screen, (0, 0, 0), start_button_clicked_digrafos_hamilton_1)
        screen.blit(start_button_text, (775, 415))
    else:
        # Renderizar el grafo con flechas
        render_digraph(screen, G, font, remaining_time, path, start_node, end_node, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_clicked_grafos_euler_2 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        render_main_menu_button(screen, font_small_buttons)

        render_dialog(screen, "¿Qué querés saber?", font, FrogNeutral())

        dead_flower.update_animation()
        dead_flower.draw(screen, 1250, 470)

    # Verificar si se acabó el tiempo
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Resetear color de los nodos
        return False

    if won_level:
        flower.update_animation()
        flower.draw(screen, 1250, 470)

    return False

def handle_grafos_digrafos_hamilton_1_mousedown(event, go_to_map):
    global back_button_clicked_digrafos_hamilton_1, start_button_clicked_digrafos_hamilton_1, restart_button_clicked_digrafos_hamilton_1, timer_started
    if back_button_clicked_digrafos_hamilton_1 is not None and back_button_clicked_digrafos_hamilton_1.collidepoint(event.pos):
        timer_started = False
        go_to_map()
        reset_nodes(path)
    elif start_button_clicked_digrafos_hamilton_1 is not None and start_button_clicked_digrafos_hamilton_1.collidepoint(event.pos):
        timer_started = True
    elif restart_button_clicked_digrafos_hamilton_1 is not None and restart_button_clicked_digrafos_hamilton_1.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)

def reset_nodes(path):
    global current_node,G, seeds
    path.clear()
    current_node = None
    seeds = {
        'A': DigrafosHamilton1Seed(), 'B': DigrafosHamilton1Seed(), 'C': DigrafosHamilton1Seed(), 'D': DigrafosHamilton1Seed(),
        'E': DigrafosHamilton1Seed(), 'F': DigrafosHamilton1Seed(), 'G': DigrafosHamilton1Seed(), 'H': DigrafosHamilton1Seed()
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

# Función para renderizar el grafo con flechas
def render_graph_with_arrows(screen, G, font, positions):
    #screen.fill((255, 255, 255))  # Fondo blanco
    for u, v in G.edges():
        start_pos = positions[u]
        end_pos = positions[v]
        # Dibujar flechas
        pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 2)
        draw_arrow(screen, start_pos, end_pos)  # Función auxiliar para flechas

    for node, pos in positions.items():
        color = G.nodes[node]['color']
        pygame.draw.circle(screen, color, pos, 20)
        node_text = font.render(node, True, (255, 255, 255))
        screen.blit(node_text, (pos[0] - 10, pos[1] - 10))


# Función auxiliar para dibujar una flecha en una línea
def draw_arrow(screen, start, end):
    # Calcular dirección y longitud del vector de la flecha
    arrow_length = 10
    angle = pygame.math.Vector2(end[0] - start[0], end[1] - start[1]).angle_to((1, 0))
    arrow_vector = pygame.math.Vector2(arrow_length, 0).rotate(angle)

    # Calcular los puntos para la flecha
    arrow_pos1 = (end[0] - arrow_vector.x - arrow_vector.y, end[1] - arrow_vector.y + arrow_vector.x)
    arrow_pos2 = (end[0] - arrow_vector.x + arrow_vector.y, end[1] - arrow_vector.y - arrow_vector.x)

    pygame.draw.polygon(screen, (0, 0, 0), [end, arrow_pos1, arrow_pos2])


# Función para manejar eventos de teclas en el digrafo de Hamilton
def handle_digrafos_hamilton_1_keydown(event):
    global current_node, seeds, won_level
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = DigrafosHamilton1SeedDisabled()
            elif key in G.successors(current_node):  # Solo moverse a nodos sucesores válidos
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = DigrafosHamilton1SeedDisabled()

            # Verificar si el camino hamiltoniano está completo
            if current_node == end_node and len(path) == len(G.nodes):
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")
                return True, current_node
    return False, current_node
