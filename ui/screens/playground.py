import os

from ui.screens.common.sound_player import play_button, play_sound
from ui.utils.fonts import font_small_buttons
from core.pet import get_selected_pet
from core.screens import Screens
from core.game_progress_playground import game_playground_progress

import pygame
import math

from ui.utils.animated_sprite import AnimatedSprite
from ui.screens.common.main_menu_button_renderer import render_playground_main_menu_button
from ui.screens.common.map_counter_renderer import counter_renderer

main_menu_button_clicked_playground = None
nodes = {
    'Frog': {'pos': (141+60, 602), 'color': (0, 0, 0)},  # Negro
    'B': {'pos': (597+20, 641), 'color': (255, 255, 255)},  # Amarillo
    'C': {'pos': (927+20, 709), 'color': (255, 255, 255)},  # Lila
    'D': {'pos': (600+20, 234), 'color': (255, 255, 255)},  # Celeste
    'E': {'pos': (994+20, 347), 'color': (255, 255, 255)},  # Rosa
    'F': {'pos': (1305+20, 485), 'color': (255, 255, 255)},  # Verde
}

total_nodes = len(nodes)
missing_nodes = len(nodes)-1

edges = [
    ('Frog', 'B'), ('B', 'C'), ('C', 'D'),
    ('D', 'E'), ('E', 'F')
]

node_screens = {
    'B': Screens.PLAYGROUND_1,
    'C': Screens.PLAYGROUND_2,
    'D': Screens.PLAYGROUND_3,
    'E': Screens.PLAYGROUND_4,
    'F': Screens.PLAYGROUND_5
}
def render_playground(screen, time):
    global main_menu_button_clicked_playground, edges, total_nodes, missing_nodes, nodes
    # Fondo de mapa con movimiento flotante
    background_image = pygame.image.load("assets/playground-bg/map.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))

    # NODE IMG
    done_node_image = pygame.image.load('./assets/map-nodes/done-node.png').convert_alpha()
    done_node_image = pygame.transform.scale(done_node_image,(130, 130))
    undone_node_image = pygame.image.load('./assets/map-nodes/undone-node.png').convert_alpha()
    undone_node_image = pygame.transform.scale(undone_node_image,(130,130))

    # FONTS
    font_path = 'assets/fonts/'
    font = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 32)
    font_title = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 45)
    font_subtitle = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 28)

    # Movimiento flotante suave
    float_offset = math.sin(time * 0.3) * 3  # Reduce la frecuencia (0.3) y amplitud (3) para suavizar
    screen.blit(background_image, (0, float_offset))

    # Nubes estáticas
    background_clouds = pygame.image.load("assets/playground-bg/static-clouds.png").convert_alpha()
    background_clouds = pygame.transform.scale(background_clouds, (1710, 1034))
    screen.blit(background_clouds, (0, 0))

    # Title
    title_img = pygame.image.load("assets/playground-bg/title-background.png").convert_alpha()
    title_img = pygame.transform.scale(title_img, (450, 400))
    screen.blit(title_img, (60, 60))

    playground_text = font_title.render("Playground", True, (255, 255, 255))
    screen.blit(playground_text, (200, 180))

    for edge in edges:
        start_pos = nodes[edge[0]]['pos']
        end_pos = nodes[edge[1]]['pos']
        draw_curved_line(screen, (0, 0, 0), start_pos, end_pos, dash_length=10)

    selected_frog = get_selected_pet(size=(180, 180))
    selected_frog.update_animation()
    selected_frog.draw(screen, nodes['Frog']['pos'][0], nodes['Frog']['pos'][1])

    clover = AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-end/clover-end", frame_size=(130, 130), frame_count=625)
    clover_current = AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-b&w/clover", frame_size=(130, 130), frame_count=625)
    clover_dead = AnimatedSprite(frame_path="./assets/giphs/playground-node/clover-black/clover-black", frame_size=(130, 130), frame_count=625)
    for node, data in nodes.items():
        if node != 'Frog':
            if (game_playground_progress.get(node) is not None and game_playground_progress.get(node)['completed']):
                # Renderizar el clover en el centro del nodo
                clover.update_animation()
                clover.draw(screen,data['pos'][0],data['pos'][1])

                # Renderizar la letra del nodo, excepto los niveles de Digrafo que no existen
                letter_text = font.render(node, True, (255, 255, 255))
                letter_rect = letter_text.get_rect(center=data['pos'])
                screen.blit(letter_text, letter_rect)
            elif (game_playground_progress.get(node) is not None and game_playground_progress.get(node)['enabled']):
                # Renderizar el clover en el centro del nodo
                clover_current.update_animation()
                clover_current.draw(screen, data['pos'][0], data['pos'][1])

                # Renderizar la letra del nodo, excepto los niveles de Digrafo que no existen
                letter_text = font.render(node, True, (255, 255, 255))
                letter_rect = letter_text.get_rect(center=data['pos'])
                screen.blit(letter_text, letter_rect)
            else:
                clover_dead.update_animation()
                clover_dead.draw(screen, data['pos'][0], data['pos'][1])

                # Renderizar la letra del nodo, excepto los niveles de Digrafo que no existen
                letter_text = font.render(node, True, (255, 255, 255))
                letter_rect = letter_text.get_rect(center=data['pos'])
                screen.blit(letter_text, letter_rect)


    counter_renderer(screen, font_subtitle, total_nodes, missing_nodes, clover, 200, 200)

    # Draw the "Main Menu" button
    main_menu_button_clicked_playground = render_playground_main_menu_button(screen, font_small_buttons, (1500, 30))

def draw_curved_line(surface, color, start_pos, end_pos, dash_length=10):
    control_x = (start_pos[0] + end_pos[0]) / 2
    control_y = min(start_pos[1], end_pos[1]) - 50
    points = []

    for t in range(0, 101, 5):
        t /= 100
        x = (1 - t) ** 2 * start_pos[0] + 2 * (1 - t) * t * control_x + t ** 2 * end_pos[0]
        y = (1 - t) ** 2 * start_pos[1] + 2 * (1 - t) * t * control_y + t ** 2 * end_pos[1]
        points.append((x, y))

    for i in range(len(points) - 1):
        if i % 2 == 0:
            pygame.draw.line(surface, color, points[i], points[i + 1], 2)


def handle_playground_mousedown(go_to_level, is_screen_on_focus):
    global main_menu_button_clicked_playground, nodes, node_screens, game_playground_progress
    if not is_screen_on_focus:
        return

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0]:
        if main_menu_button_clicked_playground is not None and main_menu_button_clicked_playground.collidepoint(mouse_pos):
            play_button('button.mp3')
            go_to_level(Screens.MAIN)
        else:
            for node, data in nodes.items():
                if game_playground_progress.get(node) is not None and game_playground_progress.get(node)['enabled']:
                    node_pos = data['pos']
                    distance = math.hypot(node_pos[0] - mouse_pos[0], node_pos[1] - mouse_pos[1])
                    if distance <= 20:
                        play_button('frog.mp3')
                        print(f"Node {node} clicked! Navigating to {node_screens[node]}")
                        level = node_screens[node]
                        go_to_level(level)
