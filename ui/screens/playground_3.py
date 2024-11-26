import networkx as nx

from core.game_progress_playground import complete_level
from core.screens import Screens
from ui.screens.common.sound_player import play_button
from ui.utils.animated_sprite import AnimatedSprite
from ui.screens.common.dialogue_renderer import render_playground_dialogue
from ui.screens.common.graph_renderer import render_simple_node_graph
from ui.screens.common.main_menu_button_renderer import render_playground_main_menu_button
from ui.screens.common.map_button_renderer import render_playground_map_button
from ui.screens.common.playground_sign_renderer import render_sign
from ui.screens.common.restart_button_renderer import render_playground_restart_button
from ui.utils.fonts import *
from ui.screens.common.seed_counter_renderer import render_counter

G = nx.Graph()

positions = {
    'A': (551, 349-60), 'B': (1167, 349-60), 'C': (686, 676-60), 'D': (862, 143-60), 'E': (1040, 676-60)
}

clovers = {
    'A': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-end/clover-end", frame_size=(110, 110), frame_count=625),
    'B': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'C': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'D': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625),
    'E': AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(110, 110), frame_count=625)
}

for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')
]

for edge in edges:
    G.add_edge(edge[0], edge[1])

start_node = None
end_node = 'A'
path = []
timer_started = False
start_time = 0
visited_edges = []

current_node = None
won_level = False
lost_level = False
missing_edges = len(edges)

back_button_clicked_playground_3 = None
restart_button_clicked_playground_3 = None
main_menu_button_clicked_playground_3 = None


def render_playground_3(screen, font):
    global back_button_clicked_playground_3, restart_button_clicked_playground_3, main_menu_button_clicked_playground_3, timer_started, start_time, path, start_node, positions, current_node, energy
    if won_level:
        background_image = pygame.image.load("./assets/playground-bg/final/bg-level-3.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        render_playground_dialogue(screen,
                                   'Congratulations, what a nice kite.\nPress "RESTART" to play again or "MAP" to continue to the next level.',
                                   font, 'happy')
    else:
        background_image = pygame.image.load("./assets/playground-bg/initial/bg-level-3.png").convert()
        background_image = pygame.transform.scale(background_image, (1710, 1034))
        screen.blit(background_image, (0, 0))
        render_playground_dialogue(screen,
                                   "Look at this star! It looks like we can build it using an Euler path.\n- You must pass through ALL 5 edges.\n- You can repeat nodes, but NOT edges.\n- You can start anywhere, but must finish at the 4 leaf clover for luck.\nPress the letters to navigate the entire graph in order!",
                                   font, 'neutral')

    # Render the graph and energy bar
    render_simple_node_graph(screen, G, font, visited_edges, positions, clovers)

    # Draw the "Back" button
    back_button_clicked_playground_3 = render_playground_map_button(screen, font_small_buttons)

    # Draw the "Restart" button
    restart_button_clicked_playground_3 = render_playground_restart_button(screen, font_small_buttons)

    # Draw the "Main Menu" button
    main_menu_button_clicked_playground_3 = render_playground_main_menu_button(screen, font_small_buttons)

    render_counter(screen, font, missing_edges, AnimatedSprite(frame_path="./assets/giphs/playground-node/clover/clover", frame_size=(90, 90), frame_count=626))

    render_sign(screen,'euler')
    
    return False

def handle_playground_3_mousedown(event, go_to_level, is_screen_on_focus):
    global back_button_clicked_playground_3, restart_button_clicked_playground_3, timer_started, path,\
        current_node, main_menu_button_clicked_playground_3
    if not is_screen_on_focus:
        return

    if back_button_clicked_playground_3 is not None and back_button_clicked_playground_3.collidepoint(event.pos):
        play_button('button.mp3')
        go_to_level(Screens.PLAYGROUND)
        reset_nodes(path)
    elif restart_button_clicked_playground_3 is not None and restart_button_clicked_playground_3.collidepoint(event.pos):
        play_button('button.mp3')
        timer_started = False
        reset_nodes(path)
    elif main_menu_button_clicked_playground_3 is not None and main_menu_button_clicked_playground_3.collidepoint(event.pos):
        play_button('button.mp3')
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

def handle_playground_3_keydown(event):
    global current_node, clovers, won_level, G, missing_edges, visited_edges

    if event.type != pygame.KEYDOWN:
        return

    key = pygame.key.name(event.key).upper()

    if key not in G.nodes:
        play_button('leaf.mp3')
        print("Tecla no válida: el nodo no existe.")
        return

    def update_node_sprite(node, color='color'):
        """Actualiza el sprite del nodo según el estado."""
        frame_path = (
            "./assets/giphs/playground-node/clover/clover"
            if color == 'color' else
            "./assets/giphs/playground-node/clover-b&w/clover"
        )
        clovers[node] = AnimatedSprite(frame_path=frame_path, frame_size=(110, 110), frame_count=626)

    if current_node is None:
        # Selecciona el primer nodo
        current_node = key
        path.append(current_node)
        if current_node != end_node:
            update_node_sprite(current_node, 'color')
        return

    if key not in G.neighbors(current_node):
        print("Movimiento no permitido: no es vecino del nodo actual.")
        return

    edge = (current_node, key)

    if edge in visited_edges or (key, current_node) in visited_edges:
        print("Movimiento no permitido: no se puede usar la misma arista dos veces.")
        return

    # Marca la arista como visitada y actualiza el camino
    visited_edges.append(edge)
    path.append(key)

    # Actualiza el sprite del nodo actual y cambia al siguiente nodo
    if current_node != end_node:
        update_node_sprite(current_node, 'b&w')
    current_node = key

    if current_node != end_node:
        update_node_sprite(current_node, 'color')

    # Reduce el conteo de aristas restantes
    missing_edges -= 1

    # Verifica si se completó el nivel
    if current_node == end_node and len(visited_edges) == len(G.edges):
        play_button('victory.mp3')
        won_level = True
        print("¡Felicidades! Has completado el Camino de Euler.")
        complete_level('D')




