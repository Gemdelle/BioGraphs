import networkx as nx

from core.screens import Screens
from ui.utils.animated_bug import AnimatedBug
from ui.utils.animated_sprite import AnimatedSprite
from ui.screens.common.dialogue_renderer import render_playground_dialogue
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_euler_graph
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.screens.common.seed_counter_renderer import render_counter
from ui.screens.common.start_button_renderer import render_start_button
from ui.utils.fonts import *

G = nx.Graph()
# restarle 60 a y
positions = {
    'A': (298, 295-60), 'B': (732, 245-60), 'C': (308, 533-60), 'D': (558, 514-60),
    'E': (1070, 280-60), 'F': (708, 608-60), 'G': (929, 424-60), 'H': (1000, 620-60),
    'I': (1480, 375-60), 'J': (1238, 477-60)
}

seeds = {
    'A': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'B': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'C': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'D': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'E': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'F': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'G': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'H': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'I': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
    'J': AnimatedBug(-15, -10, frame_path="./assets/giphs/bugs/bug-euler-3/euler-3-bug", frame_size=(130, 130), frame_count=74)
}

dead_flower = AnimatedSprite(frame_path="./assets/giphs/flowers-bw/euler-3-flower-bw/euler-3-flower-bw", frame_size=(480, 480), frame_count=74)
flower = AnimatedSprite(frame_path="./assets/giphs/flowers/euler-3-flower/euler-3-flower", frame_size=(480, 480), frame_count=74)

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(200, 0, 0))

edges = [
    ('H', 'G'),
    ('I', 'H'),
    ('I', 'J'),
    ('G', 'I'),
    ('E', 'I'),
    ('F', 'G'),
    ('E', 'F'), #6
    ('D', 'E'),
    ('D', 'F'),
    ('B', 'F'),
    ('C', 'D'),
    ('B', 'C'),
    ('A', 'D'),
    ('A', 'B'),
    ('E', 'G')
]

missing_edges = len(edges)

curve_intensities = {
    edges[0]: 50,
    edges[1]: 350,
    edges[2]: 50,
    edges[3]: 50,
    edges[4]: 50,
    edges[5]: 50,
    edges[6]: -30,
    edges[7]: -20,
    edges[8]: 50,
    edges[9]: 50,
    edges[10]: 50,
    edges[11]: 50,
    edges[12]: 50,
    edges[13]: 50,
    edges[14]: 50
}

for edge in edges:
    G.add_edge(edge[0], edge[1])

start_node = None
end_node = 'H'
path = []
timer_started = False
start_time = 0
remaining_time = None

current_node = None
won_level = False
lost_level = False
click_locked = False

initial_energy = 17
energy = initial_energy  # Starting energy level
start_ticks = pygame.time.get_ticks()  # Start time for timer
timer_duration = 60000  # 60 seconds duration

back_button_clicked_grafos_euler_3 = None
start_button_clicked_grafos_euler_3 = None
restart_button_clicked_grafos_euler_3 = None
main_menu_button_clicked_grafos_euler_3 = None
visited_edges = []

def render_grafos_euler_3(screen, font):
    from ui.utils.fonts import font_small_buttons
    global back_button_clicked_grafos_euler_3, start_button_clicked_grafos_euler_3, restart_button_clicked_grafos_euler_3,\
        timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower,\
        missing_edges, remaining_time, main_menu_button_clicked_grafos_euler_3, lost_level

    current_time = pygame.time.get_ticks()
    if won_level:
        background_image_win = pygame.image.load("assets/final-bg/euler-3.png").convert()
        background_image_win = pygame.transform.scale(background_image_win, (1710, 1034))
        screen.blit(background_image_win, (0, 0))
        render_playground_dialogue(screen, 'Congratulations, what a nice kite.\nPress "RESTART" to play again or "MAP" to continue to the next level.', font, 'happy')
    elif timer_started:
        background_image = pygame.image.load("assets/initial-bg/euler-3.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
        render_playground_dialogue(screen,
                                   "Restore the plant 'Erlem' by solving the Euler path before the timer runs out.\n- You must pass through ALL 16 edges.\n- You can repeat nodes, but NOT edges.\n- You can start anywhere, but must finish at the bug node so I can eat it.\nPress the letters to navigate the entire graph in order!",
                                   font, 'neutral')
    else:
        background_image = pygame.image.load("assets/blur/euler-1.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        start_time = pygame.time.get_ticks()
        remaining_time = 120000

    # Update energy based on remaining time
    if remaining_time > 0:
        energy = initial_energy * (remaining_time / timer_duration)
    else:
        energy = initial_energy  # Reset energy if time runs out

    # Draw the "Back" button

    back_button_clicked_grafos_euler_3 = render_map_button(screen, font_small_buttons)

    if lost_level:
        restart_button_clicked_grafos_euler_3 = render_restart_button(screen, font_small_buttons, (800, 500))
        render_playground_dialogue(screen,
                                   "Beter luck next time",
                                   font, 'angry')
    elif not timer_started:
        start_button_clicked_grafos_euler_3 = render_start_button(screen, font_start, AnimatedSprite(frame_path="./assets/giphs/seeds/euler-3-seed/euler-3-seed", frame_size=(150, 150), frame_count=74))
    else:
        # Render the graph and energy bar
        render_euler_graph(screen, G, font, visited_edges, positions, seeds, curve_intensities)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        # Draw the "Restart" button
        restart_button_clicked_grafos_euler_3 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        main_menu_button_clicked_grafos_euler_3 = render_main_menu_button(screen, font_small_buttons)

        render_counter(screen,font,missing_edges,AnimatedSprite(frame_path="./assets/giphs/seeds/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74))

        if won_level:
            flower.update_animation()
            flower.draw(screen, 1540, 750)
        else:
            dead_flower.update_animation()
            dead_flower.draw(screen, 1540, 750)

    # Check if time is up
    if timer_started and remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        won_level = False
        timer_started = False
        lost_level = True


def handle_grafos_euler_3_mousedown(event, go_to_level, is_screen_on_focus):
    global back_button_clicked_grafos_euler_3, start_button_clicked_grafos_euler_3, restart_button_clicked_grafos_euler_3,\
        timer_started, main_menu_button_clicked_grafos_euler_3

    if not is_screen_on_focus:
        return

    if back_button_clicked_grafos_euler_3 is not None and back_button_clicked_grafos_euler_3.collidepoint(event.pos):
        go_to_level(Screens.MAP)
        reset_nodes(path)
    elif restart_button_clicked_grafos_euler_3 is not None and restart_button_clicked_grafos_euler_3.collidepoint(event.pos):
        reset_nodes(path)
    elif start_button_clicked_grafos_euler_3 is not None and start_button_clicked_grafos_euler_3.collidepoint(event.pos):
        timer_started = True
    elif main_menu_button_clicked_grafos_euler_3 is not None and main_menu_button_clicked_grafos_euler_3.collidepoint(event.pos):
        reset_nodes(path)
        go_to_level(Screens.MAIN)


def handle_grafos_euler_3_keydown(event,go_to_map):
    global current_node, seeds, won_level, G, missing_edges, visited_edges
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()
        if key in G.nodes:
            if current_node is None:
                current_node = key
                path.append(current_node)
                seeds[current_node] = AnimatedSprite(frame_path="./assets/giphs/seeds/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74)
            elif key in G.neighbors(current_node):
                # Verifica si la arista entre `current_node` y `key` ya ha sido visitada
                edge = (current_node, key)
                if edge not in visited_edges and (key, current_node) not in visited_edges:
                    visited_edges.append(edge)  # Marca la arista como visitada
                    path.append(key)  # Agrega el nodo al camino
                    seeds[current_node] = AnimatedSprite(frame_path="./assets/giphs/seeds/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74)
                    current_node = key
                    missing_edges -= 1
                    seeds[current_node] = AnimatedSprite(frame_path="./assets/giphs/seeds/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74)
                    # Revisa si completaste el camino de Euler
                    if current_node == end_node and len(visited_edges) == len(G.edges):
                        won_level = True
                        print("¡Felicidades! Has completado el Camino de Euler.")
            else:
                print("Movimiento no permitido: no se puede usar la misma arista dos veces.")

def reset_nodes(path):
    global current_node, G, seeds, missing_edges, visited_edges, won_level,timer_started,lost_level, remaining_time
    path.clear()
    current_node = None
    remaining_time = None
    won_level = False
    timer_started = False
    lost_level = False
    visited_edges.clear()

    seeds = {
        'A': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'B': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'C': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'D': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'E': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'F': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'G': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'H': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'I': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-3-seed/euler-3-seed", frame_size=(90, 90), frame_count=74),
        'J': AnimatedBug(-15, -10, frame_path="./assets/giphs/bugs/bug-euler-3/euler-3-bug", frame_size=(130, 130), frame_count=74)
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

    missing_edges = len(edges)