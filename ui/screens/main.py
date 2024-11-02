import pygame
import math
from core.screens import Screens

def render_main(screen, goToLevel):
    # background_image = pygame.image.load("assets/map.png").convert()
    # background_image = pygame.transform.scale(background_image, (1710, 1034))
    # screen.blit(background_image, (0,0))
    screen.fill((255, 255, 255))

    nodes = {
        'A': {'pos': (500, 450), 'color': (255, 204, 102), 'enabled': True},  # Yellow: GRAFOS_EULER_1
        'B': {'pos': (1180, 430), 'color': (153, 204, 255), 'enabled': True},  # Light Blue: GRAFOS_HAMILTON_1
        'C': {'pos': (1450, 260), 'color': (255, 102, 102), 'enabled': True},  # Pink: GRAFOS_HAMILTON_2
        'D': {'pos': (1120, 170), 'color': (255, 178, 102), 'enabled': True},  # Orange: GRAFOS_HAMILTON_3
        'E': {'pos': (450, 180), 'color': (255, 102, 178), 'enabled': False},  # Purple: DIGRAFOS_EULER_1
        'F': {'pos': (200,230), 'color': (255, 102, 178), 'enabled': False},  # Red: DIGRAFOS_HAMILTON_1
        'G': {'pos': (700,700), 'color': (255, 102, 178), 'enabled': False},        # Black: GRAFOS_EULER_1
        'H': {'pos': (600,850), 'color': (255, 102, 178), 'enabled': False},     # Teal: GRAFOS_EULER_1
        'I': {'pos': (300,750), 'color': (255, 102, 178), 'enabled': False},         # Black: GRAFOS_EULER_1
        'J': {'pos': (1050,760), 'color': (255, 102, 178), 'enabled': False},         # Black: GRAFOS_EULER_1
        'K': {'pos': (1300,850), 'color': (255, 102, 178), 'enabled': False},         # Black: GRAFOS_EULER_1
        'L': {'pos': (1550,650), 'color': (255, 102, 178), 'enabled': False},         # Black: GRAFOS_EULER_1
        'M': {'pos': (870,500), 'color': (0, 0, 0), 'enabled': False},         # Black: GRAFOS_EULER_1
    }

    edges = [
        ('M', 'A'),('A', 'E'),('E', 'F'),('M', 'B'),('B', 'C'),('C', 'D'),('M', 'G'),('G', 'H'),('H', 'I'),('M', 'J'),
        ('J', 'K'),('K', 'L')
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
