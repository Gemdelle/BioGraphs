import pygame
import math
from core.screens import Screens


def render_playground(screen, goToLevel):
    # background_image = pygame.image.load("assets/map-pg.png").convert()
    # background_image = pygame.transform.scale(background_image, (1710, 1034))
    # screen.blit(background_image, (0,0))
    screen.fill((255, 255, 255))

    nodes = {
        'A': {'pos': (255, 453), 'color': (0, 0, 0), 'enabled': False},  # Negro
        'B': {'pos': (591, 255), 'color': (255, 255, 102), 'enabled': True},  # Amarillo
        'C': {'pos': (476, 722), 'color': (200, 150, 255), 'enabled': True},  # Lila
        'D': {'pos': (1038, 575), 'color': (102, 204, 255), 'enabled': True},  # Celeste
        'E': {'pos': (1316, 338), 'color': (255, 182, 193), 'enabled': True},  # Rosa
        'F': {'pos': (1465, 846), 'color': (144, 238, 144), 'enabled': True},  # Verde
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
        pygame.draw.circle(screen, data['color'], data['pos'], 60)

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
