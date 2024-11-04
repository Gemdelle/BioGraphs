import pygame
import networkx as nx
import numpy as np

def draw_curved_line(surface, color, start_pos, end_pos, dash_length=10, dot_radius=2):
    # Definir el punto de control para la curva
    control_x = (start_pos[0] + end_pos[0]) / 2
    control_y = min(start_pos[1], end_pos[1]) - 50
    points = []

    # Generar puntos a lo largo de la curva usando interpolación cuadrática
    for t in np.linspace(0, 1, 100):  # Más puntos para mayor precisión
        x = (1 - t) ** 2 * start_pos[0] + 2 * (1 - t) * t * control_x + t ** 2 * end_pos[0]
        y = (1 - t) ** 2 * start_pos[1] + 2 * (1 - t) * t * control_y + t ** 2 * end_pos[1]
        points.append((x, y))

    # Dibujar puntos con separación uniforme
    current_length = 0  # Para acumular la distancia recorrida entre puntos

    for i in range(len(points) - 1):
        # Calcula la distancia entre el punto actual y el siguiente
        start_point = points[i]
        end_point = points[i + 1]
        distance = np.linalg.norm(np.array(end_point) - np.array(start_point))

        # Acumula la longitud actual
        current_length += distance

        # Dibuja un punto solo si ha recorrido una longitud suficiente
        if current_length >= dash_length:
            pygame.draw.circle(surface, color, (int(start_point[0]), int(start_point[1])), dot_radius)
            current_length = 0  # Reinicia la longitud acumulada después de cada punto


def draw_curved_line(surface, color, start_pos, end_pos, line_width=2):
    # Definir el punto de control para la curva
    control_x = (start_pos[0] + end_pos[0]) / 2
    control_y = min(start_pos[1], end_pos[1]) - 50
    points = []

    # Generar puntos a lo largo de la curva usando interpolación cuadrática
    for t in np.linspace(0, 1, 100):  # Más puntos para una curva suave
        x = (1 - t) ** 2 * start_pos[0] + 2 * (1 - t) * t * control_x + t ** 2 * end_pos[0]
        y = (1 - t) ** 2 * start_pos[1] + 2 * (1 - t) * t * control_y + t ** 2 * end_pos[1]
        points.append((x, y))

    # Dibujar una línea continua conectando los puntos de la curva
    for i in range(len(points) - 1):
        start_point = points[i]
        end_point = points[i + 1]
        pygame.draw.line(surface, color, start_point, end_point, line_width)

def render_graph(screen, G, font, path, positions, animated_nodes):
    # Dibuja bordes curvos y punteados
    for edge in G.edges():
        start_pos = positions[edge[0]]
        end_pos = positions[edge[1]]
        draw_curved_line(screen, (255, 255, 255), start_pos, end_pos)

    # Dibuja nodos y animaciones
    for node, pos in nx.get_node_attributes(G, 'pos').items():
        animated_nodes[node].update_animation()
        animated_nodes[node].draw(screen, pos[0] - 25, pos[1] - 25)

        # Dibuja el texto de cada nodo
        screen.blit(font.render(node, True, (255, 255, 255)), (pos[0] - 10, pos[1] - 10))


def render_simple_node_graph(screen, G, font, path, positions):
    # Cargar la imagen de fondo del nodo
    background_image = pygame.image.load("assets/playground-bg/node.png").convert_alpha()
    background_image = pygame.transform.scale(background_image, (70, 70))  # Ajustar el tamaño de la imagen
    # Dibujar aristas
    for edge in G.edges():
        pygame.draw.line(screen, (0, 0, 0), positions[edge[0]], positions[edge[1]], 8)

    # Dibujar nodos con la imagen de fondo y texto
    for node, pos in positions.items():
        # Colocar imagen de fondo del nodo
        screen.blit(background_image, (pos[0] - 35, pos[1] - 35))  # Posicionar centrado

        # Dibujar el texto del nodo
        text_surface = font.render(node, True, (0, 0, 0))  # Letra blanca
        screen.blit(text_surface, (pos[0] - text_surface.get_width() // 2, pos[1] - text_surface.get_height() // 2))


def get_node_at_position(G, pos):
    for node, data in G.nodes(data=True):
        node_pos = data['pos']
        distance = ((node_pos[0] - pos[0]) ** 2 + (node_pos[1] - pos[1]) ** 2) ** 0.5
        if distance < 20:
            return node
    return None