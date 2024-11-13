from core.screens import Screens

import pygame
import math


def render_playground(screen, goToLevel, time):
    # Fondo de mapa con movimiento flotante
    background_image = pygame.image.load("assets/playground-bg/map.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))

    # Movimiento flotante suave
    float_offset = math.sin(time * 0.3) * 3  # Reduce la frecuencia (0.3) y amplitud (3) para suavizar
    screen.blit(background_image, (0, float_offset))

    # Nubes estáticas
    background_clouds = pygame.image.load("assets/playground-bg/static-clouds.png").convert_alpha()
    background_clouds = pygame.transform.scale(background_clouds, (1710, 1034))
    screen.blit(background_clouds, (0, 0))

    nodes = {
        'A': {'pos': (141, 602-60), 'color': (0, 0, 0), 'enabled': False},  # Negro
        'B': {'pos': (597, 641-60), 'color': (255, 255, 255), 'enabled': True},  # Amarillo
        'C': {'pos': (927, 709-60), 'color': (255, 255, 255), 'enabled': True},  # Lila
        'D': {'pos': (600, 234-60), 'color': (255, 255, 255), 'enabled': True},  # Celeste
        'E': {'pos': (994, 347-60), 'color': (255, 255, 255), 'enabled': True},  # Rosa
        'F': {'pos': (1305, 485-60), 'color': (255, 255, 255), 'enabled': True},  # Verde
    }

    edges = [
        ('A', 'B'), ('B', 'C'), ('C', 'D'),
        ('D', 'E'), ('E', 'F')
    ]

    node_screens = {
        'B': Screens.PLAYGROUND_1,
        'C': Screens.PLAYGROUND_2,
        'D': Screens.PLAYGROUND_3,
        'E': Screens.PLAYGROUND_4,
        'F': Screens.PLAYGROUND_5
    }

    font = pygame.font.SysFont(None, 36)

    for edge in edges:
        start_pos = nodes[edge[0]]['pos']
        end_pos = nodes[edge[1]]['pos']
        draw_curved_line(screen, (0, 0, 0), start_pos, end_pos, dash_length=10)

    for node, data in nodes.items():
        pygame.draw.circle(screen, data['color'], data['pos'], 40)

        # Renderizar la letra del nodo
        letter_text = font.render(node, True, (0, 0, 0))
        letter_rect = letter_text.get_rect(center=data['pos'])
        screen.blit(letter_text, letter_rect)

    playground_text = font.render("Playground", True, (0, 0, 0))

    screen.blit(playground_text, (100, 100))

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
