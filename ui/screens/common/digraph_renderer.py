import pygame
import networkx as nx
import math

def draw_arrow(screen, start, end, color=(0, 0, 0), arrow_size=20, offset=30):
    # Calcular la dirección del borde
    dx, dy = end[0] - start[0], end[1] - start[1]
    distance = math.hypot(dx, dy)
    angle = math.atan2(dy, dx)

    # Ajustar el punto final para que la flecha no llegue al centro del vértice
    end_adj = (end[0] - offset * math.cos(angle), end[1] - offset * math.sin(angle))
    
    # Acortar la línea para que no se vea después del triángulo
    line_end = (end_adj[0] - arrow_size * 0.1 * math.cos(angle), 
                end_adj[1] - arrow_size * 0.1 * math.sin(angle))

    # Dibuja la línea ajustada que termina antes del triángulo
    pygame.draw.line(screen, color, start, line_end, 2)

    # Calcular las posiciones de las flechas (triángulo más grande)
    left = (end_adj[0] - arrow_size * math.cos(angle - math.pi / 6),
            end_adj[1] - arrow_size * math.sin(angle - math.pi / 6))
    right = (end_adj[0] - arrow_size * math.cos(angle + math.pi / 6),
             end_adj[1] - arrow_size * math.sin(angle + math.pi / 6))

    # Dibujar la flecha (triángulo)
    pygame.draw.polygon(screen, color, [end_adj, left, right])
    

def render_digraph(screen, G, font, remaining_time, visited_edges , start_node, end_node, positions, animated_nodes):
    # Dibuja las aristas y colorea en rojo las aristas visitadas
    for start, end in G.edges():
        start_pos = G.nodes[start]['pos']
        end_pos = G.nodes[end]['pos']
        color = (128,128,128) if (start, end) in visited_edges else (0, 0, 0)
        draw_arrow(screen, start_pos, end_pos, color)

    # Dibuja nodos y animaciones
    for node, pos in nx.get_node_attributes(G, 'pos').items():
        animated_nodes[node].update_animation()
        animated_nodes[node].draw(screen, pos[0], pos[1])
        screen.blit(font.render(node, True, (255, 255, 255)), (pos[0] - 15, pos[1] - 15))

def get_node_at_position(G, pos):
    for node, data in G.nodes(data=True):
        node_pos = data['pos']
        distance = ((node_pos[0] - pos[0]) ** 2 + (node_pos[1] - pos[1]) ** 2) ** 0.5
        if distance < 20:
            return node
    return None
