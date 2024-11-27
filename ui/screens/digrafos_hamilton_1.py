import networkx as nx

from core.screens import Screens
from ui.screens.common.sound_player import play_button
from ui.utils.animated_bug import AnimatedBug
from ui.utils.animated_sprite import AnimatedSprite
from ui.screens.common.dialogue_renderer import render_dialogue
from ui.screens.common.digraph_renderer import render_digraph
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.screens.common.seed_counter_renderer import render_counter
from ui.screens.common.start_button_renderer import render_start_button
from ui.utils.fonts import *

# Crear un DiGraph para representar el digrafo
G = nx.DiGraph()

# Definir posiciones de los nodos
positions = {
    'A': (802, 447 - 60), 'B': (850, 270 - 60), 'C': (320, 254 - 60), 'D': (438, 550 - 60),
    'E': (1099, 617 - 60), 'F': (616, 393 - 60), 'G': (1420, 306 - 60), 'H': (947, 487 - 60)
}

seeds = {
    'A': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                        frame_count=74),
    'B': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                        frame_count=74),
    'C': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                        frame_count=74),
    'D': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                        frame_count=74),
    'E': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                        frame_count=74),
    'F': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                        frame_count=74),
    'G': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                        frame_count=74),
    'H': AnimatedBug(x_position_extra=-10, y_position_extra=5,
                     frame_path="./assets/giphs/bugs/bug-d-hamilton/d-hamilton-bug", frame_size=(120, 120),
                     frame_count=74)
}

dead_flower = AnimatedSprite(frame_path="./assets/giphs/flowers-bw/d-hamilton-flower-bw/d-hamilton-flower-bw",
                             frame_size=(480, 480), frame_count=74)
flower = AnimatedSprite(frame_path="./assets/giphs/flowers/d-hamilton-flower/d-hamilton-flower", frame_size=(480, 480),
                        frame_count=74)

missing_nodes = len(positions)

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
lost_level = False
initial_energy = 17
energy = initial_energy  # Energía inicial
start_ticks = pygame.time.get_ticks()  # Tiempo de inicio
timer_duration = 60000  # 60 segundos

back_button_clicked_digrafos_hamilton_1 = None
start_button_clicked_digrafos_hamilton_1 = None
restart_button_clicked_digrafos_hamilton_1 = None
main_menu_button_clicked_digrafos_hamilton_1 = None

time_finishing_warning_done = False


# Función de renderizado con flechas en aristas
def render_digrafos_hamilton_1(screen, font, go_to_map, events):
    from ui.utils.fonts import font_small_buttons
    global back_button_clicked_digrafos_hamilton_1, start_button_clicked_digrafos_hamilton_1, \
        restart_button_clicked_digrafos_hamilton_1, timer_started, start_time, path, start_node, \
        positions, current_node, energy, won_level, flower, missing_nodes, remaining_time, \
        main_menu_button_clicked_digrafos_hamilton_1, lost_level, time_finishing_warning_done

    current_time = pygame.time.get_ticks()
    if won_level:
        background_image_win = pygame.image.load("assets/final-bg/d-hamilton.png").convert()
        background_image_win = pygame.transform.scale(background_image_win, (1710, 1034))
        screen.blit(background_image_win, (0, 0))
        render_dialogue(screen, 'Congratulations, you have restored the local flora.\nPress '
                                '"RESTART" to play again or "MAP" to continue to the next level.', font,
                        'happy')
    elif timer_started:
        background_image = pygame.image.load("assets/initial-bg/d-hamilton.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
        render_dialogue(screen,
                        "Restore the plant 'Uchya' by solving the Hamilton path before the timer runs "
                        "out.\n- You must pass through ALL 8 nodes.\n- You can repeat edges, but NOT nodes.\n- "
                        "You can start anywhere, but must finish at the bug node so I can eat it.\nPress the letters "
                        "to navigate the entire digraph in order, REMEMBER the directions!",
                        font, 'neutral')
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

    if lost_level:
        restart_button_clicked_digrafos_hamilton_1 = render_restart_button(screen, font_small_buttons, (800, 500))
        render_dialogue(screen,
                        "Beter luck next time...",
                        font, 'angry')
    elif not timer_started:
        start_button_clicked_digrafos_hamilton_1 = render_start_button(screen, font_start, AnimatedSprite(
            frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(150, 150), frame_count=74))
    else:
        # Renderizar el grafo con flechas
        render_digraph(screen, G, font, remaining_time, path, start_node, end_node, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        if remaining_time // 1000 <= 20 and time_finishing_warning_done is False:
            play_button('timer.mp3')
            time_finishing_warning_done = True

        # Draw the "Restart" button
        restart_button_clicked_digrafos_hamilton_1 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        main_menu_button_clicked_digrafos_hamilton_1 = render_main_menu_button(screen, font_small_buttons)

        render_counter(screen, font, missing_nodes,
                       AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed",
                                      frame_size=(90, 90), frame_count=74))

        if won_level:
            flower.update_animation()
            flower.draw(screen, 1510, 680)
        else:
            dead_flower.update_animation()
            dead_flower.draw(screen, 1510, 680)

    # Verificar si se acabó el tiempo
    if remaining_time <= 0:
        play_button('lose.mp3')
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        lost_level = True
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)


def handle_grafos_digrafos_hamilton_1_mousedown(event, go_to_level, is_screen_on_focus):
    global back_button_clicked_digrafos_hamilton_1, start_button_clicked_digrafos_hamilton_1, \
        restart_button_clicked_digrafos_hamilton_1, timer_started
    if not is_screen_on_focus:
        return

    if (back_button_clicked_digrafos_hamilton_1 is not None and
            back_button_clicked_digrafos_hamilton_1.collidepoint(
            event.pos)):
        play_button('button.mp3')
        timer_started = False
        go_to_level(Screens.MAP)
        reset_nodes(path)
    elif (start_button_clicked_digrafos_hamilton_1 is not None and
          start_button_clicked_digrafos_hamilton_1.collidepoint(
            event.pos)):
        play_button('button.mp3')
        timer_started = True
    elif (restart_button_clicked_digrafos_hamilton_1 is not None and
          restart_button_clicked_digrafos_hamilton_1.collidepoint(
            event.pos)):
        play_button('button.mp3')
        timer_started = False
        reset_nodes(path)
    elif (main_menu_button_clicked_digrafos_hamilton_1 is not None and
          main_menu_button_clicked_digrafos_hamilton_1.collidepoint(
            event.pos)):
        play_button('button.mp3')
        timer_started = False
        reset_nodes(path)
        go_to_level(Screens.MAIN)


def reset_nodes(path):
    global current_node, G, seeds, missing_nodes, lost_level, time_finishing_warning_done
    path.clear()
    current_node = None
    lost_level = False
    time_finishing_warning_done = False
    seeds = {
        'A': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                            frame_count=74),
        'B': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                            frame_count=74),
        'C': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                            frame_count=74),
        'D': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                            frame_count=74),
        'E': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                            frame_count=74),
        'F': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                            frame_count=74),
        'G': AnimatedSprite(frame_path="./assets/giphs/seeds/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                            frame_count=74),
        'H': AnimatedSprite(frame_path="./assets/giphs/bugs/bug-d-hamilton/d-hamilton-bug", frame_size=(120, 120),
                            frame_count=74)
    }

    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

    missing_nodes = len(positions)


# Función para renderizar el grafo con flechas
def render_graph_with_arrows(screen, G, font, positions):
    # screen.fill((255, 255, 255))  # Fondo blanco
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
def handle_digrafos_hamilton_1_keydown(event, go_to_map):
    global current_node, seeds, won_level, missing_nodes
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                play_button('node.mp3')
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = AnimatedSprite(
                    frame_path="./assets/giphs/seeds-b&w/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                    frame_count=74)
            elif key in G.successors(current_node):  # Solo moverse a nodos sucesores válidos
                G.nodes[current_node]['color'] = (0, 100, 0)
                play_button('node.mp3')
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = AnimatedSprite(
                    frame_path="./assets/giphs/seeds-b&w/d-hamilton-seed/d-hamilton-seed", frame_size=(90, 90),
                    frame_count=74)
            missing_nodes -= 1

            # Verificar si el camino hamiltoniano está completo
            if current_node == end_node and len(path) == len(G.nodes):
                play_button('victory.mp3')
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")
