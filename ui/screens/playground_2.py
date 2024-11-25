import networkx as nx

from core.game_progress_playground import complete_level
from core.screens import Screens
from ui.utils.animated_sprite import AnimatedSprite
from ui.screens.common.dialogue_renderer import render_playground_dialogue
from ui.screens.common.graph_renderer import render_simple_node_graph, render_euler_graph
from ui.screens.common.main_menu_button_renderer import render_playground_main_menu_button
from ui.screens.common.map_button_renderer import render_playground_map_button
from ui.screens.common.playground_sign_renderer import render_sign
from ui.screens.common.restart_button_renderer import render_playground_restart_button
from ui.utils.fonts import *
from ui.screens.common.seed_counter_renderer import render_counter

G = nx.Graph()

positions = {
    'A': (931, 689-60),
    'B': (931, 472-60),
    'C': (752, 529-60),
    'D': (638, 389-60),
    'E': (790, 363-60),
    'F': (842, 305-60),
    'G': (931, 172-60),
    'H': (1023, 305-60),
    'I': (1101, 353-60),
    'J': (1220, 389-60),
    'K': (1077, 519-60)
}

clovers = {
    'A': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'B': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'C': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'D': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'E': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'F': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'G': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'H': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'I': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'J': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'K': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-end/clover-end", frame_size=(110, 110), frame_count=625)
}

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'B'), ('B', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'B'),
    ('B', 'I'), ('I', 'J'), ('J', 'K'), ('B', 'K')
]

for edge in edges:
    G.add_edge(edge[0], edge[1])

start_node = None
end_node = 'B'
path = []
timer_started = False
start_time = 0
visited_edges = []

current_node = None
won_level = False
lost_level = False
missing_edges = len(edges)

back_button_clicked_playground_2 = None
restart_button_clicked_playground_2 = None
main_menu_button_clicked_playground_2 = None


def render_playground_2(screen, font):
    global back_button_clicked_playground_2, restart_button_clicked_playground_2, main_menu_button_clicked_playground_2, timer_started, start_time, path, start_node, positions, current_node, energy
    if won_level:
        background_image = pygame.image.load("./assets/playground-bg/final/bg-level-2.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        render_playground_dialogue(screen,
                                   'Congratulations, what a nice kite.\nPress "RESTART" to play again or "MAP" to continue to the next level.',
                                   font, 'happy')
    else:
        background_image = pygame.image.load("./assets/playground-bg/initial/bg-level-2.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        render_playground_dialogue(screen,
                                   "Hello again! We can now build a leaf together. Let's solve this Euler path.\n- You must pass through ALL 13 edges.\n- You can repeat nodes, but NOT edges.\n- You can start anywhere, but must finish at the 4 leaf clover for luck.\nPress the letters to navigate the entire graph in order!",
                                   font, 'neutral')

    # Render the graph and energy bar
    render_simple_node_graph(screen, G, font, visited_edges, positions, clovers)

    # Draw the "Back" button
    back_button_clicked_playground_2 = render_playground_map_button(screen, font_small_buttons)

    # Draw the "Restart" button
    restart_button_clicked_playground_2 = render_playground_restart_button(screen, font_small_buttons)

    # Draw the "Main Menu" button
    main_menu_button_clicked_playground_2 = render_playground_main_menu_button(screen, font_small_buttons)

    render_counter(screen, font, missing_edges, AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(90, 90), frame_count=626))

    render_sign(screen,'euler')

    return False


def handle_playground_2_mousedown(event, go_to_level, is_screen_on_focus):
    global back_button_clicked_playground_2, restart_button_clicked_playground_2, timer_started,\
        path, current_node, main_menu_button_clicked_playground_2
    if not is_screen_on_focus:
        return

    if back_button_clicked_playground_2 is not None and back_button_clicked_playground_2.collidepoint(event.pos):
        go_to_level(Screens.PLAYGROUND)
        reset_nodes(path)
    elif restart_button_clicked_playground_2 is not None and restart_button_clicked_playground_2.collidepoint(event.pos):
        timer_started = False
        reset_nodes(path)
    elif main_menu_button_clicked_playground_2 is not None and main_menu_button_clicked_playground_2.collidepoint(event.pos):
        reset_nodes(path)
        go_to_level(Screens.MAIN)


def reset_nodes(path):
    global current_node, G, clovers, missing_edges, visited_edges, won_level, lost_level
    path.clear()
    current_node = None
    won_level = False
    lost_level = False
    visited_edges.clear()

    clovers = {
        'A': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
        'B': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
        'C': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
        'D': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
        'E': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-end/clover-end", frame_size=(110, 110), frame_count=625)
    }

    for node in G.nodes:
        G.nodes[node]['color'] = (0, 0, 0)
    missing_edges = len(edges)


def handle_playground_2_keydown(event):
    global current_node, clovers, won_level, G, missing_edges, visited_edges
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()
        if key in G.nodes:
            if current_node is None:
                current_node = key
                path.append(current_node)
                clovers[current_node] = AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(110, 110), frame_count=626)
            elif key in G.neighbors(current_node):
                # Verifica si la arista entre `current_node` y `key` ya ha sido visitada
                edge = (current_node, key)
                if edge not in visited_edges and (key, current_node) not in visited_edges:
                    visited_edges.append(edge)  # Marca la arista como visitada
                    path.append(key)  # Agrega el nodo al camino
                    clovers[key] = AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(110, 110), frame_count=626)
                    current_node = key
                    missing_edges -= 1
                    clovers[key] = AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(110, 110), frame_count=626)
                    # Revisa si completaste el camino de Euler
                    if current_node == end_node and len(visited_edges) == len(G.edges):
                        won_level = True
                        print("¡Felicidades! Has completado el Camino de Euler.")
                        complete_level('C')
            else:
                print("Movimiento no permitido: no se puede usar la misma arista dos veces.")



