import networkx as nx

from core.screens import Screens
from ui.screens.common.sound_player import play_button
from ui.utils.animated_bug import AnimatedBug
from ui.utils.animated_sprite import AnimatedSprite
from ui.screens.common.dialogue_renderer import render_playground_dialogue
from ui.screens.common.energy_timer_renderer import render_energy_and_timer
from ui.screens.common.graph_renderer import render_graph
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.common.map_button_renderer import render_map_button
from ui.screens.common.restart_button_renderer import render_restart_button
from ui.screens.common.seed_counter_renderer import render_counter
from ui.screens.common.start_button_renderer import render_start_button
from ui.utils.fonts import *

G = nx.Graph()
# restarle 60 a y
positions = {
    'A': (433, 512-60),
    'B': (251, 360-60),
    'C': (584, 233-60),
    'D': (819, 446-60),
    'E': (955, 538-60),
    'F': (1145, 315-60),
    'G': (1419, 315-60),
    'H': (1293, 430-60)
}

seeds = {
    'A': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
    'B': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
    'C': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
    'D': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
    'E': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
    'F': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
    'G': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
    'H': AnimatedBug(-5,-20,frame_path="./assets/giphs/bugs/bug-hamilton-1/hamilton-1-bug", frame_size=(120, 120), frame_count=74)
}

dead_flower = AnimatedSprite(frame_path="./assets/giphs/flowers-bw/hamilton-1-flower-bw/hamilton-1-flower-bw", frame_size=(480, 480), frame_count=74)
flower = AnimatedSprite(frame_path="./assets/giphs/flowers/hamilton-1-flower/hamilton-1-flower", frame_size=(480, 480), frame_count=74)

missing_nodes = len(positions)

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(200, 0, 0))

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
remaining_time = None

current_node = None
won_level = False
lost_level = False
click_locked = False

initial_energy = 17
energy = initial_energy  # Starting energy level
start_ticks = pygame.time.get_ticks()  # Start time for timer
timer_duration = 60000  # 60 seconds duration

back_button_clicked_grafos_hamilton_1 = None
start_button_clicked_grafos_hamilton_1 = None
restart_button_clicked_grafos_hamilton_1 = None
main_menu_button_clicked_grafos_hamilton_1 = None

time_finishing_warning_done = False
def render_grafos_hamilton_1(screen, font):
    from ui.utils.fonts import font_small_buttons
    global back_button_clicked_grafos_hamilton_1, start_button_clicked_grafos_hamilton_1,\
        restart_button_clicked_grafos_hamilton_1,timer_started, start_time, path, start_node, positions,\
        current_node, energy, won_level, flower, missing_nodes, remaining_time, main_menu_button_clicked_grafos_hamilton_1, lost_level, time_finishing_warning_done

    current_time = pygame.time.get_ticks()
    if won_level:
        background_image_win = pygame.image.load("assets/final-bg/hamilton-1.png").convert()
        background_image_win = pygame.transform.scale(background_image_win, (1710, 1034))
        screen.blit(background_image_win, (0, 0))
        render_playground_dialogue(screen, 'Congratulations, what a nice kite.\nPress "RESTART" to play again or "MAP" to continue to the next level.', font, 'happy')
    elif timer_started:
        background_image = pygame.image.load("assets/initial-bg/hamilton-1.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        elapsed_time = current_time - start_time
        remaining_time = max(0, 60000 - elapsed_time)  # 1 minute (60000 ms)
        render_playground_dialogue(screen,
                                   "Restore the plant 'Erlem' by solving the Hamilton path before the timer runs out.\n- You must pass through ALL 8 nodes.\n- You can repeat edges, but NOT nodes.\n- You can start anywhere, but must finish at the bug node so I can eat it.\nPress the letters to navigate the entire graph in order!",
                                   font, 'neutral')
    else:
        background_image = pygame.image.load("assets/blur/hamilton-1.png").convert()
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
    back_button_clicked_grafos_hamilton_1 = render_map_button(screen, font_small_buttons)

    if lost_level:
        restart_button_clicked_grafos_hamilton_1 = render_restart_button(screen, font_small_buttons, (800, 500))
        render_playground_dialogue(screen,
                                   "Beter luck next time",
                                   font, 'angry')
    elif not timer_started:
        start_button_clicked_grafos_hamilton_1 = render_start_button(screen, font_start, AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(150, 150), frame_count=74))
    else:
        # Render the graph and energy bar
        render_graph(screen, G, font, path, positions, seeds)

        # Render energy bar and timer
        render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time)

        if remaining_time // 1000 <= 20 and time_finishing_warning_done is False:
            play_button('timer.mp3')
            time_finishing_warning_done = True

        # Draw the "Restart" button
        restart_button_clicked_grafos_hamilton_1 = render_restart_button(screen, font_small_buttons)

        # Draw the "Main Menu" button
        main_menu_button_clicked_grafos_hamilton_1 = render_main_menu_button(screen, font_small_buttons)

        render_counter(screen,font,missing_nodes, AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74))

        if won_level:
            flower.update_animation()
            flower.draw(screen, 1520, 750)
        else:
            dead_flower.update_animation()
            dead_flower.draw(screen, 1520, 750)

    # Check if time is up
    if timer_started and remaining_time <= 0:
        play_button('lose.mp3')
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        won_level = False
        timer_started = False
        lost_level = True

def handle_grafos_hamilton_1_mousedown(event, go_to_level, is_screen_on_focus):
    global back_button_clicked_grafos_hamilton_1, start_button_clicked_grafos_hamilton_1,\
        restart_button_clicked_grafos_hamilton_1, timer_started, main_menu_button_clicked_grafos_hamilton_1, click_locked, timer_started

    if not is_screen_on_focus:
        return

    if back_button_clicked_grafos_hamilton_1 is not None and back_button_clicked_grafos_hamilton_1.collidepoint(event.pos):
        play_button('button.mp3')
        go_to_level(Screens.MAP)
        reset_nodes(path)
    elif restart_button_clicked_grafos_hamilton_1 is not None and restart_button_clicked_grafos_hamilton_1.collidepoint(event.pos):
        play_button('button.mp3')
        reset_nodes(path)
    elif start_button_clicked_grafos_hamilton_1 is not None and start_button_clicked_grafos_hamilton_1.collidepoint(event.pos):
        play_button('button.mp3')
        timer_started = True
    elif main_menu_button_clicked_grafos_hamilton_1 is not None and main_menu_button_clicked_grafos_hamilton_1.collidepoint(event.pos):
        play_button('button.mp3')
        reset_nodes(path)
        go_to_level(Screens.MAIN)

def reset_nodes(path):
    global current_node,G, seeds, missing_nodes, won_level,timer_started,lost_level, remaining_time, time_finishing_warning_done
    path.clear()
    current_node = None
    remaining_time = None
    won_level = False
    timer_started = False
    lost_level = False
    time_finishing_warning_done = False
    seeds = {
        'A': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
        'B': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
        'C': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
        'D': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
        'E': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
        'F': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
        'G': AnimatedSprite(frame_path="./assets/giphs/seeds/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74),
        'H': AnimatedBug(-5,-20,frame_path="./assets/giphs/bugs/bug-hamilton-1/hamilton-1-bug", frame_size=(120, 120), frame_count=74)
    }
    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)

    missing_nodes = len(positions)

def handle_grafos_hamilton_1_keydown(event,go_to_map):
    global current_node, seeds, won_level, missing_nodes
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                play_button('node.mp3')
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74)
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                play_button('node.mp3')
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)
                seeds[current_node] = AnimatedSprite(frame_path="./assets/giphs/seeds-b&w/hamilton-1-seed/hamilton-1-seed", frame_size=(90, 90), frame_count=74)
                missing_nodes -= 1

            if current_node == end_node and len(path) == len(G.nodes):
                play_button('victory.mp3')
                won_level = True
                print("Congratulations! You completed the Hamiltonian Path.")
