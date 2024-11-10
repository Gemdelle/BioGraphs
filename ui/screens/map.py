import os

import networkx as nx
import pygame
import math
from core.screens import Screens
from ui.flowers.black.d_euler_1_flower import DEuler1FlowerBlack
from ui.flowers.black.d_hamilton_1_flower import DHamilton1FlowerBlack
from ui.flowers.black.euler_1_flower import Euler1FlowerBlack
from ui.flowers.black.euler_2_flower import Euler2FlowerBlack
from ui.flowers.black.euler_3_flower import Euler3FlowerBlack
from ui.flowers.black.hamilton_1_flower import Hamilton1FlowerBlack
from ui.flowers.black.hamilton_2_flower import Hamilton2FlowerBlack
from ui.flowers.black.hamilton_3_flower import Hamilton3FlowerBlack
from ui.screens.common.graph_renderer import render_map_graph

#from graph import fonts

def render_map(screen, goToLevel):
    background_image = pygame.image.load("assets/map.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0,0))
    #font = fonts[0]
    font_path = 'assets/fonts/'

    #FUENTES QUE DEBERÍA IMPORTAR COMO ARRAY DESDE GRAPH
    berry_rotunda = pygame.font.Font(os.path.join(font_path, 'Berry Rotunda.ttf'), 32)
    celtg = pygame.font.Font(os.path.join(font_path, 'CELTG___.TTF'), 32)
    magic_school_two = pygame.font.Font(os.path.join(font_path, 'MagicSchoolTwo.ttf'), 32)
    megphis = pygame.font.Font(os.path.join(font_path, 'MEGPHIS.otf'), 32)
    strange_dreams = pygame.font.Font(os.path.join(font_path, 'Strange Dreams.otf'), 32)
    strange_dreams_italic = pygame.font.Font(os.path.join(font_path, 'Strange Dreams Italic.otf'), 32)
    van_helsing = pygame.font.Font(os.path.join(font_path, 'Van Helsing.ttf'), 32)
    alice_in_wonderland = pygame.font.Font(os.path.join(font_path, 'Alice_in_Wonderland_3.ttf'), 32)

    font = strange_dreams_italic #5 fea pero se entiende
    font = berry_rotunda #6 puede ser
    font = celtg #6 zafa pero no me gusta tanto
    font_water = megphis #7 parece agua
    font = strange_dreams #7 se entiende
    font = magic_school_two #8 no se entiende pero bueno para algún tiítulo
    font = van_helsing #8
    font = alice_in_wonderland #9

    G = nx.Graph()

    nodes = {
        'Erlem': {'pos': (640, 400-60), 'color': (255, 255, 255), 'enabled': True},  # Yellow: GRAFOS_EULER_1
        'Ulfex': {'pos': (1094, 510-60), 'color': (255, 255, 255), 'enabled': True},  # Light Blue: GRAFOS_HAMILTON_1
        'Twyle': {'pos': (1307, 418-60), 'color': (255, 255, 255), 'enabled': True},  # Pink: GRAFOS_HAMILTON_2
        'Bloona': {'pos': (1225, 246-60), 'color': (255, 255, 255), 'enabled': True},  # Orange: GRAFOS_HAMILTON_3
        'Frood': {'pos': (450, 180), 'color': (255, 255, 255), 'enabled': True},  # Purple: DIGRAFOS_EULER_1
        'Orrox': {'pos': (329, 364-60), 'color': (255, 255, 255), 'enabled': True},  # Red: DIGRAFOS_HAMILTON_1
        'Spyx': {'pos': (753, 713-60), 'color': (255, 255, 255), 'enabled': True},  # Black: GRAFOS_EULER_1
        'DE-II': {'pos': (754, 900-60), 'color': (255, 255, 255), 'enabled': False},  # Teal: GRAFOS_EULER_1
        'DE-III': {'pos': (930, 799-60), 'color': (255, 255, 255), 'enabled': False},  # Black: GRAFOS_EULER_1
        'Uchya': {'pos': (1121, 877-60), 'color': (255, 255, 255), 'enabled': True},  # Black: GRAFOS_EULER_1
        'DH-II': {'pos': (1300, 850), 'color': (255, 255, 255), 'enabled': False},  # Black: GRAFOS_EULER_1
        'DH-III': {'pos': (1439, 808-60), 'color': (255, 255, 255), 'enabled': False},  # Black: GRAFOS_EULER_1
        'Frog': {'pos': (870, 500), 'color': (255, 255, 255), 'enabled': False}  # Frog
    }

    for node, pos in nodes.items():
        G.add_node(node, pos=pos, color=(0, 0, 0))

    seeds = {
        'Erlem': Euler1FlowerBlack(), 'Ulfex': Hamilton1FlowerBlack(), 'Twyle': Hamilton2FlowerBlack(), 'Bloona': Hamilton3FlowerBlack(),
        'Frood': Euler2FlowerBlack(), 'Orrox': Euler3FlowerBlack(), 'Spyx': DEuler1FlowerBlack(), 'Uchya': DHamilton1FlowerBlack()
    }

    edges = [
        ('Frog', 'Erlem'),('Erlem', 'Frood'),('Frood', 'Orrox'),('Frog', 'Ulfex'),('Ulfex', 'Twyle'),('Twyle', 'Bloona'),('Frog', 'Spyx'),('Spyx', 'DE-II'),('DE-II', 'DE-III'),('Frog', 'Uchya'),
        ('Uchya', 'DH-II'),('DH-II', 'DH-III')
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
        pygame.draw.circle(screen, data['color'], data['pos'], 45)
    
        # Renderizar la letra del nodo
        letter_text = font.render(node, True, (0, 0, 0))
        letter_rect = letter_text.get_rect(center=data['pos'])
        screen.blit(letter_text, letter_rect)

    grafo_euler_text = font.render("GRAFO Euler", True, (0, 0, 0))
    grafo_hamilton_text = font.render("GRAFO Hamilton", True, (0, 0, 0))
    digrafo_euler_text = font.render("DIGRAFO Euler", True, (0, 0, 0))
    digrafo_hamilton_text = font.render("DIGRAFO Hamilton", True, (0, 0, 0))


    screen.blit(grafo_euler_text, (100, 100))
    screen.blit(grafo_hamilton_text, (1400, 100))
    screen.blit(digrafo_euler_text, (100, 950))
    screen.blit(digrafo_hamilton_text, (1400, 950))

    handle_node_click(nodes, node_screens, goToLevel)


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


def handle_node_click(nodes, node_screens, goToLevel):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0]:
        for node, data in nodes.items():
            if data['enabled']:
                node_pos = data['pos']
                distance = math.hypot(node_pos[0] - mouse_pos[0], node_pos[1] - mouse_pos[1])
                if distance <= 20:
                    print(f"Node {node} clicked! Navigating to {node_screens[node]}")
                    goToLevel(node_screens[node])
