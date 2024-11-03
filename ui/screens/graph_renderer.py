import pygame
import networkx as nx

def render_graph(screen, G, font, path, positions):
    # screen.fill((255, 255, 255))  # Fondo blanco
    for edge in G.edges():
        pygame.draw.line(screen, (0, 0, 0), positions[edge[0]], positions[edge[1]], 2)

    for node, pos in nx.get_node_attributes(G, 'pos').items():
        color = (0, 255, 0) if node in path else (0, 0, 0)  # Verde si es parte del camino
        pygame.draw.circle(screen, (255,0,0), pos, 35)
        pygame.draw.circle(screen, color, pos, 30)
        screen.blit(font.render(node, True, (255, 255, 255)), (pos[0] - 10, pos[1] - 10))


def get_node_at_position(G, pos):
    for node, data in G.nodes(data=True):
        node_pos = data['pos']
        distance = ((node_pos[0] - pos[0]) ** 2 + (node_pos[1] - pos[1]) ** 2) ** 0.5
        if distance < 20:
            return node
    return None
