import pygame
import networkx as nx

def render_graph(screen, G, font, path, positions, animated_nodes):
    # Draw edges
    for edge in G.edges():
        pygame.draw.line(screen, (0, 0, 0), positions[edge[0]], positions[edge[1]], 2)

    # Draw nodes and animations
    for node, pos in nx.get_node_attributes(G, 'pos').items():
        animated_nodes[node].update_animation()
        animated_nodes[node].draw(screen, pos[0] - 25, pos[1] - 25)

        # Draw node circle and label
        # color = (0, 255, 0) if node in path else (0, 0, 0)
        # pygame.draw.circle(screen, (255, 0, 0), pos, 35)
        # pygame.draw.circle(screen, color, pos, 30)
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
