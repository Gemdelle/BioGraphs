import pygame
import networkx as nx
import math

def draw_arrow(screen, start, end, color=(0, 0, 0), arrow_size=10):
    # Dibuja la línea
    pygame.draw.line(screen, color, start, end, 2)

    # Calcular la dirección del borde
    dx, dy = end[0] - start[0], end[1] - start[1]
    angle = math.atan2(dy, dx)

    # Calcular las posiciones de las flechas
    left = (end[0] - arrow_size * math.cos(angle - math.pi / 6),
            end[1] - arrow_size * math.sin(angle - math.pi / 6))
    right = (end[0] - arrow_size * math.cos(angle + math.pi / 6),
             end[1] - arrow_size * math.sin(angle + math.pi / 6))

    # Dibujar las flechas
    pygame.draw.polygon(screen, color, [end, left, right])

def render_digraph(screen, G, font, remaining_time, path, start_node, end_node, positions, animated_nodes):
    # screen.fill((255, 255, 255))  # Fondo blanco
    for node, pos in nx.get_node_attributes(G, 'pos').items():
        animated_nodes[node].update_animation()
        animated_nodes[node].draw(screen, pos[0], pos[1])
        screen.blit(font.render(node, True, (255, 255, 255)), (pos[0] - 15, pos[1] - 15))

    for start, end in G.edges():
        start_pos = G.nodes[start]['pos']
        end_pos = G.nodes[end]['pos']
        draw_arrow(screen, start_pos, end_pos)

    for edge in G.edges():
        pygame.draw.line(screen, (0, 0, 0), positions[edge[0]], positions[edge[1]], 2)

def render_euler_digraph(screen, G, font, remaining_time, visited_edges , start_node, end_node, positions, animated_nodes):
    # Dibuja nodos y animaciones
    for node, pos in nx.get_node_attributes(G, 'pos').items():
        animated_nodes[node].update_animation()
        animated_nodes[node].draw(screen, pos[0], pos[1])
        screen.blit(font.render(node, True, (255, 255, 255)), (pos[0] - 15, pos[1] - 15))

    # Dibuja las aristas y colorea en rojo las aristas visitadas
    for start, end in G.edges():
        start_pos = G.nodes[start]['pos']
        end_pos = G.nodes[end]['pos']
        color = (255, 0, 0) if (start, end) in visited_edges else (0, 0, 0)
        draw_arrow(screen, start_pos, end_pos, color)

def get_node_at_position(G, pos):
    for node, data in G.nodes(data=True):
        node_pos = data['pos']
        distance = ((node_pos[0] - pos[0]) ** 2 + (node_pos[1] - pos[1]) ** 2) ** 0.5
        if distance < 20:
            return node
    return None
