import networkx as nx

from core.game_progress_map import complete_level
from core.screens import Screens
from ui.screens.common.sound_player import play_button
from ui.utils.animated_bug import AnimatedBug
from ui.utils.animated_sprite import AnimatedSprite
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.dialogue_renderer import render_dialogue
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_euler_graph
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.screens.common.seed_counter_renderer import render_counter
from ui.screens.common.start_button_renderer import render_start_button
from ui.utils.fonts import *

G = nx.Graph()
positions = {
    'A': (891, 254 - 60), 'B': (1084, 371 - 60), 'C': (1028, 546 - 60), 'D': (752, 595 - 60),
    'E': (235, 525 - 60), 'F': (484, 410 - 60)
}

seeds = {
    'A': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                        frame_count=74),
    'B': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                        frame_count=74),
    'C': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                        frame_count=74),
    'D': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                        frame_count=74),
    'E': AnimatedBug(x_position_extra=-25, y_position_extra=-5,
                     frame_path="./assets/giphs/bugs/bug-euler-1/euler-1-bug", frame_size=(120, 120), frame_count=74),
    'F': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                        frame_count=74)
}

dead_flower = AnimatedSprite(frame_path="./assets/giphs/flowers-bw/euler-1-flower-bw/euler-1-flower-bw",
                             frame_size=(480, 480), frame_count=74)
flower = AnimatedSprite(frame_path="./assets/giphs/flowers/euler-1-flower/euler-1-flower", frame_size=(480, 480),
                        frame_count=74)

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D'), ('F', 'D'), ('A', 'F'), ('D', 'E')
]

missing_edges = len(edges)

for edge in edges:
    G.add_edge(edge[0], edge[1])

start_node = None
end_node = 'E'
path = []
timer_started = False
start_time = 0
remaining_time = None

current_node = None
won_level = False
lost_level = False
click_locked = False
time_finishing_warning_done = False

initial_energy = 17
energy = initial_energy  # Starting energy level
start_ticks = pygame.time.get_ticks()  # Start time for timer
timer_duration = 60000  # 60 seconds duration

back_button_clicked_grafos_euler_1 = None
start_button_clicked_grafos_euler_1 = None
restart_button_clicked_grafos_euler_1 = None
main_menu_button_clicked_grafos_euler_1 = None
visited_edges = []


def render_grafos_euler_1(screen, font):
    from ui.utils.fonts import font_small_buttons
    global back_button_clicked_grafos_euler_1, start_button_clicked_grafos_euler_1, restart_button_clicked_grafos_euler_1, \
        timer_started, start_time, path, start_node, positions, current_node, energy, won_level, flower, \
        missing_edges, main_menu_button_clicked_grafos_euler_1, lost_level, remaining_time, time_finishing_warning_done

    current_time = pygame.time.get_ticks()
    if won_level:
        background_image_win = pygame.image.load("assets/final-bg/euler-1.png").convert()
        background_image_win = pygame.transform.scale(background_image_win, (1710, 1034))
        screen.blit(background_image_win, (0, 0))
        render_dialogue(screen,
                        'Congratulations, you have restored the local flora.\nPress "RESTART" to play again or "MAP" to continue to the next level.',
                        font, 'happy')
    elif timer_started:
        background_image = pygame.image.load("assets/initial-bg/euler-1.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
        render_dialogue(screen,
                        "Restore the plant 'Erlem' by solving the Euler path before the timer runs out.\n- You must pass through ALL 7 edges.\n- You can repeat nodes, but NOT edges.\n- You can start anywhere, but must finish at the bug node so I can eat it.\nPress the letters to navigate the entire graph in order!",
                        font, 'neutral')
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
    back_button_clicked_grafos_euler_1 = render_map_button(screen, font_small_buttons)

    if lost_level:
        restart_button_clicked_grafos_euler_1 = render_restart_button(screen, font_small_buttons, (800, 500))
        render_dialogue(screen,
                        "Better luck next time...",
                        font, 'angry')
    elif not timer_started:
        start_button_clicked_grafos_euler_1 = render_start_button(screen, font_start, AnimatedSprite(
            frame_path="./assets/giphs/seeds/euler-1-seed/euler-1-seed", frame_size=(150, 150), frame_count=74))
    else:
        # Render the graph
        render_euler_graph(screen, G, font, visited_edges, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        if remaining_time // 1000 <= 20 and time_finishing_warning_done is False:
            play_button('timer.mp3')
            time_finishing_warning_done = True

        # Draw the "Restart" button
        restart_button_clicked_grafos_euler_1 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        main_menu_button_clicked_grafos_euler_1 = render_main_menu_button(screen, font_small_buttons)

        render_counter(screen, font, missing_edges,
                       AnimatedSprite(frame_path="./assets/giphs/seeds/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                                      frame_count=74))

        if won_level:
            flower.update_animation()
            flower.draw(screen, 1430, 500)
        else:
            dead_flower.update_animation()
            dead_flower.draw(screen, 1430, 500)

    if timer_started and remaining_time <= 0:
        play_button('lose.mp3')
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        won_level = False
        timer_started = False
        lost_level = True


def handle_grafos_euler_1_mousedown(event, go_to_level, is_screen_on_focus):
    global back_button_clicked_grafos_euler_1, start_button_clicked_grafos_euler_1, \
        restart_button_clicked_grafos_euler_1
    global main_menu_button_clicked_grafos_euler_1, timer_started
    if not is_screen_on_focus:
        return
    if back_button_clicked_grafos_euler_1 is not None and back_button_clicked_grafos_euler_1.collidepoint(event.pos):
        play_button('button.mp3')
        go_to_level(Screens.MAP)
        reset_nodes(path)
    elif restart_button_clicked_grafos_euler_1 is not None and restart_button_clicked_grafos_euler_1.collidepoint(
            event.pos):
        play_button('button.mp3')
        reset_nodes(path)
    elif start_button_clicked_grafos_euler_1 is not None and start_button_clicked_grafos_euler_1.collidepoint(
            event.pos):
        play_button('button.mp3')
        timer_started = True
    elif main_menu_button_clicked_grafos_euler_1 is not None and main_menu_button_clicked_grafos_euler_1.collidepoint(
            event.pos):
        play_button('button.mp3')
        reset_nodes(path)
        go_to_level(Screens.MAIN)


def handle_grafos_euler_1_keydown(event, go_to_map):
    global current_node, seeds, won_level, G, missing_edges, visited_edges, remaining_time, timer_started

    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            # Actualiza todos los nodos a blanco y negro excepto el nodo final
            for node in G.nodes:
                if node != end_node:
                    seeds[node] = AnimatedSprite(
                        frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed",
                        frame_size=(90, 90), frame_count=74
                    )

            # El nodo final no cambia su imagen, se mantiene como está
            # Aquí no se modifica el sprite del nodo final

            if current_node is None:
                # Selecciona el primer nodo
                play_button('node.mp3')
                current_node = key
                path.append(current_node)
                if current_node != end_node:
                    seeds[current_node] = AnimatedSprite(
                        frame_path="./assets/giphs/seeds/euler-1-seed/euler-1-seed",
                        frame_size=(90, 90), frame_count=74
                    )
            elif key in G.neighbors(current_node):
                edge = (current_node, key)

                if edge not in visited_edges and (key, current_node) not in visited_edges:
                    # Marca la arista como visitada y actualiza el camino
                    visited_edges.append(edge)
                    path.append(key)

                    # Cambia el nodo actual a color si no es el nodo final
                    if key != end_node:
                        seeds[key] = AnimatedSprite(
                            frame_path="./assets/giphs/seeds/euler-1-seed/euler-1-seed",
                            frame_size=(90, 90), frame_count=74
                        )

                    # Actualiza el nodo actual y los bordes restantes
                    play_button('node.mp3')
                    current_node = key
                    missing_edges -= 1

                    # Verifica si completaste el nivel
                    if current_node == end_node and len(visited_edges) == len(G.edges):
                        play_button('victory.mp3')
                        won_level = True
                        print("¡Felicidades! Has completado el Camino de Euler.")
                        complete_level('Erlem')
                        remaining_time = 60000
            else:
                print("Movimiento no permitido: no se puede usar la misma arista dos veces.")


def reset_nodes(path):
    global current_node, G, seeds, missing_edges, visited_edges, won_level, timer_started, lost_level, remaining_time, \
        time_finishing_warning_done
    path.clear()
    current_node = None
    remaining_time = None
    won_level = False
    timer_started = False
    lost_level = False
    time_finishing_warning_done = False
    visited_edges.clear()

    seeds = {
        'A': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                            frame_count=74),
        'B': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                            frame_count=74),
        'C': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                            frame_count=74),
        'D': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                            frame_count=74),
        'E': AnimatedBug(x_position_extra=-25, y_position_extra=-5,
                         frame_path="./assets/giphs/bugs/bug-euler-1/euler-1-bug", frame_size=(120, 120),
                         frame_count=74),
        'F': AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/euler-1-seed/euler-1-seed", frame_size=(90, 90),
                            frame_count=74)
    }

    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)
    missing_edges = len(edges)
