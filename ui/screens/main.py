import pygame
import math
from core.screens import Screens

def render_main(screen, goToLevel):
    screen.fill((255, 255, 255))

    nodes = {
        'A': {'pos': (100, 100), 'color': (255, 204, 102), 'enabled': True},  # Yellow
        'B': {'pos': (150, 200), 'color': (153, 204, 255), 'enabled': True},  # Light Blue
        'C': {'pos': (200, 100), 'color': (255, 178, 102), 'enabled': True},  # Orange
        'D': {'pos': (250, 200), 'color': (255, 102, 102), 'enabled': True},  # Pink
        'E': {'pos': (300, 300), 'color': (204, 153, 255), 'enabled': True},  # Purple
        'F': {'pos': (400, 200), 'color': (255, 102, 178), 'enabled': True},  # Red
        'G': {'pos': (500, 100), 'color': (0, 0, 0), 'enabled': False},        # Black
        'H': {'pos': (600, 200), 'color': (0, 204, 204), 'enabled': False},     # Teal
        'I': {'pos': (700, 300), 'color': (0, 0, 0), 'enabled': False},         # Black
        'J': {'pos': (700, 300), 'color': (0, 0, 0), 'enabled': False},         # Black
        'K': {'pos': (700, 300), 'color': (0, 0, 0), 'enabled': False},         # Black
        'L': {'pos': (700, 300), 'color': (0, 0, 0), 'enabled': False},         # Black
        'M': {'pos': (700, 300), 'color': (0, 0, 0), 'enabled': False},         # Black
    }

    edges = [
        ('A', 'B'), ('B', 'D'), ('D', 'E'), ('E', 'F'), ('G', 'H'), ('H', 'I'),
        ('C', 'D'), ('A', 'C'), ('F', 'D')
    ]

    node_screens = {
        'A': Screens.GRAFOS_EULER_1,
        'B': Screens.GRAFOS_HAMILTON_1,
        'C': Screens.GRAFOS_HAMILTON_2,
        'D': Screens.GRAFOS_HAMILTON_3,
        'E': Screens.DIGRAFOS_EULER_1,
        'F': Screens.DIGRAFOS_HAMILTON_1,
        'G': Screens.GRAFOS_EULER_1,
        'H': Screens.GRAFOS_EULER_1,
        'I': Screens.GRAFOS_EULER_1,
        'J': Screens.GRAFOS_EULER_1,
        'K': Screens.GRAFOS_EULER_1,
        'L': Screens.GRAFOS_EULER_1,
        'M': Screens.GRAFOS_EULER_1,
    }

    for edge in edges:
        start_pos = nodes[edge[0]]['pos']
        end_pos = nodes[edge[1]]['pos']
        draw_curved_line(screen, (0, 0, 0), start_pos, end_pos, dash_length=10)

    for node, data in nodes.items():
        pygame.draw.circle(screen, data['color'], data['pos'], 20)
        pygame.draw.circle(screen, (0, 0, 0), data['pos'], 22, 2)  # Outline in black

    font = pygame.font.SysFont(None, 36)
    grafo_euler_text = font.render("GRAFO Euler", True, (0, 0, 0))
    grafo_hamilton_text = font.render("GRAFO Hamilton", True, (0, 0, 0))
    digrafo_euler_text = font.render("DIGRAFO Euler", True, (0, 0, 0))
    digrafo_hamilton_text = font.render("DIGRAFO Hamilton", True, (0, 0, 0))

    screen.blit(grafo_euler_text, (20, 20))
    screen.blit(grafo_hamilton_text, (300, 150))
    screen.blit(digrafo_euler_text, (500, 250))
    screen.blit(digrafo_hamilton_text, (700, 350))

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
