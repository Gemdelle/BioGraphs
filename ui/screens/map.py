import os

import networkx as nx
import pygame
import math

from core.game_progress import game_progress
from core.pet import get_selected_pet
from core.screens import Screens
from ui.flowers.black.d_euler_1_flower_black import DEuler1FlowerBlack
from ui.flowers.black.d_hamilton_1_flower_black import DHamilton1FlowerBlack
from ui.flowers.black.euler_1_flower_black import Euler1FlowerBlack
from ui.flowers.black.euler_2_flower_black import Euler2FlowerBlack
from ui.flowers.black.euler_3_flower_black import Euler3FlowerBlack
from ui.flowers.black.hamilton_1_flower_black import Hamilton1FlowerBlack
from ui.flowers.black.hamilton_2_flower_black import Hamilton2FlowerBlack
from ui.flowers.black.hamilton_3_flower_black import Hamilton3FlowerBlack
from ui.screens.common.graph_renderer import render_map_graph


def render_map(screen, go_to_level):
    background_image = pygame.image.load("assets/map.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0,0))

    font_path = 'assets/fonts/'
    font = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 32)
    font_title = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 40)
    font_subtitle = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 28)

    # NODE IMG
    done_node_image = pygame.image.load('./assets/map-nodes/done-node.png').convert_alpha()
    done_node_image = pygame.transform.scale(done_node_image,(130, 130))
    undone_node_image = pygame.image.load('./assets/map-nodes/undone-node.png').convert_alpha()
    undone_node_image = pygame.transform.scale(undone_node_image,(130,130))

    #SIGN IMG LOAD & RESIZE
    sign_width = 350
    sign_height = 150
    
    sign_euler_image = pygame.image.load('./assets/signs/sign-euler.png').convert_alpha()
    sign_euler_image = pygame.transform.scale(sign_euler_image,(sign_width,sign_height-50))
    sign_hamilton_image = pygame.image.load('./assets/signs/sign-hamilton.png').convert_alpha()
    sign_hamilton_image = pygame.transform.scale(sign_hamilton_image,(sign_width,sign_height))
    sign_d_euler_image = pygame.image.load('./assets/signs/sign-d-euler.png').convert_alpha()
    sign_d_euler_image = pygame.transform.scale(sign_d_euler_image,(sign_width,sign_height))
    sign_d_hamilton_image = pygame.image.load('./assets/signs/sign-d-hamilton.png').convert_alpha()
    sign_d_hamilton_image = pygame.transform.scale(sign_d_hamilton_image,(sign_width,sign_height))

    G = nx.Graph()

    selected_frog = get_selected_pet(size=(150, 150))

    nodes = {
        'Erlem': {'pos': (640, 400-60), 'color': (255, 255, 255)},  # Yellow: GRAFOS_EULER_1
        'Ulfex': {'pos': (1094, 510-60), 'color': (255, 255, 255)},  # Light Blue: GRAFOS_HAMILTON_1
        'Twyle': {'pos': (1307, 418-60), 'color': (255, 255, 255)},  # Pink: GRAFOS_HAMILTON_2
        'Bloona': {'pos': (1225, 246-60), 'color': (255, 255, 255)},  # Orange: GRAFOS_HAMILTON_3
        'Frood': {'pos': (450, 180), 'color': (255, 255, 255)},  # Purple: DIGRAFOS_EULER_1
        'Orrox': {'pos': (329, 364-60), 'color': (255, 255, 255)},  # Red: DIGRAFOS_HAMILTON_1
        'Spyx': {'pos': (753, 713-60), 'color': (255, 255, 255)},  # Black: GRAFOS_EULER_1
        'EII': {'pos': (754, 900-60), 'color': (255, 255, 255)},  # Teal: GRAFOS_EULER_1
        'EIII': {'pos': (930, 799-60), 'color': (255, 255, 255)},  # Black: GRAFOS_EULER_1
        'Uchya': {'pos': (1121, 877-60), 'color': (255, 255, 255)},  # Black: GRAFOS_EULER_1
        'HII': {'pos': (1300, 850), 'color': (255, 255, 255)},  # Black: GRAFOS_EULER_1
        'HIII': {'pos': (1439, 808-60), 'color': (255, 255, 255)},  # Black: GRAFOS_EULER_1
        'Frog': {'pos': (870, 500), 'color': (255, 255, 255)}  # Frog
    }

    for node, pos in nodes.items():
        G.add_node(node, pos=pos, color=(0, 0, 0))

    seeds = {
        'Erlem': Euler1FlowerBlack(), 'Ulfex': Hamilton1FlowerBlack(), 'Twyle': Hamilton2FlowerBlack(), 'Bloona': Hamilton3FlowerBlack(),
        'Frood': Euler2FlowerBlack(), 'Orrox': Euler3FlowerBlack(), 'Spyx': DEuler1FlowerBlack(), 'Uchya': DHamilton1FlowerBlack(), 'Frog': selected_frog
    }

    edges = [
        ('Frog', 'Erlem'),('Erlem', 'Frood'),('Frood', 'Orrox'),('Frog', 'Ulfex'),('Ulfex', 'Twyle'),('Twyle', 'Bloona'),('Frog', 'Spyx'),('Spyx', 'EII'),('EII', 'EIII'),('Frog', 'Uchya'),
        ('Uchya', 'HII'),('HII', 'HIII')
    ]

    for edge in edges:
        G.add_edge(edge[0], edge[1])

    node_screens = {
        'Erlem': Screens.GRAFOS_EULER_1,
        'Ulfex': Screens.GRAFOS_HAMILTON_1,
        'Twyle': Screens.GRAFOS_HAMILTON_2,
        'Bloona': Screens.GRAFOS_HAMILTON_3,
        'Frood': Screens.GRAFOS_EULER_2,
        'Orrox': Screens.GRAFOS_EULER_3,
        'Spyx': Screens.DIGRAFOS_EULER_1,
        # 'H': Screens.DIGRAFOS_EULER_1,
        # 'I': Screens.DIGRAFOS_EULER_1,
        'Uchya': Screens.DIGRAFOS_HAMILTON_1,
        # 'K': Screens.DIGRAFOS_HAMILTON_2,
        # 'L': Screens.DIGRAFOS_HAMILTON_3,
        # 'M': Screens.PROFILE
    }

    render_map_graph(screen, G, nodes, seeds)

    for node, data in nodes.items():
        if node != 'Frog':
            # Dibujar fondo del nodo
            if (game_progress.get(node) is not None and game_progress.get(node)['completed']):
                img_rect = done_node_image.get_rect(center=data['pos'])
                screen.blit(done_node_image, img_rect)
                letter_text_color = (0, 0, 0)
            else:
                img_rect = undone_node_image.get_rect(center=data['pos'])
                screen.blit(undone_node_image, img_rect)
                letter_text_color = (255, 255, 255)
            
            # Renderizar la letra del nodo, excepto los niveles de Digrafo que no existen
            letter_text = font.render(node if node not in ('EII', 'EIII', 'HII', 'HIII') else '?', True, letter_text_color)
            letter_rect = letter_text.get_rect(center=data['pos'])
            screen.blit(letter_text, letter_rect)

    # REGION NAMES
    erryloom_text = font_title.render("Errybloom", True, (0, 0, 0))
    luminore_grove_text = font_title.render("Luminore Grove", True, (0, 0, 0))
    thornscar_text = font_title.render("Thornscar", True, (0, 0, 0))
    chromecore_text = font_title.render("Chromecore", True, (0, 0, 0))

    graph_euler_text = font_subtitle.render("Euler GRAPHS", True, (255, 255, 255))
    graph_hamilton_text = font_subtitle.render("Hamilton GRAPHS", True, (255, 255, 255))
    digraph_euler_text = font_subtitle.render("Euler DIGRAPHS", True, (255, 255, 255))
    digraph_hamilton_text = font_subtitle.render("Hamilton DIGRAPHS", True, (255, 255, 255))

    screen.blit(sign_euler_image, (40,30))
    screen.blit(sign_hamilton_image, (1340, 110))
    screen.blit(sign_d_euler_image, (200, 750))
    screen.blit(sign_d_hamilton_image, (1300, 550))

    screen.blit(erryloom_text, (110+30, 80-25))
    screen.blit(luminore_grove_text, (1400+25, 175-5))
    screen.blit(thornscar_text, (270+40, 805-5))
    screen.blit(chromecore_text, (1350+50, 600-5))

    screen.blit(graph_euler_text, (110+30, 80+60))
    screen.blit(graph_hamilton_text, (1400+25, 175-70))
    screen.blit(digraph_euler_text, (270+20, 805+80))
    screen.blit(digraph_hamilton_text, (1350+30, 600-70))

    handle_node_click(nodes, node_screens, go_to_level)


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


def handle_node_click(nodes, node_screens, go_to_level):
    global game_progress
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0]:
        for node, data in nodes.items():
            if game_progress.get(node) is not None and game_progress.get(node)['enabled']:
                node_pos = data['pos']
                distance = math.hypot(node_pos[0] - mouse_pos[0], node_pos[1] - mouse_pos[1])
                if distance <= 20:
                    print(f"Node {node} clicked! Navigating to {node_screens[node]}")
                    level = node_screens[node]
                    go_to_level(level)
