# asdasd
import pygame
import networkx as nx

pygame.init()

# CONFIGURACIÓN DE PANTALLA
screen = pygame.display.set_mode((1024, 512))  
clock = pygame.time.Clock()

# CREAR GRAFO
G = nx.Graph()

# CREAR DICCIONARIO DE NODOS
positions = {
    'R': (100, 300), 'P': (50, 100), 'O': (200, 100), 'M': (150, 250), 
    'Q': (50, 400), 'L': (150, 450), 'J': (250, 350), 'K': (350, 450),
    'B': (400, 250), 'A': (550, 300), 'I': (400, 100), 'D': (550, 450),
    'E': (650, 100), 'H': (750, 450), 'G': (750, 100)
}

# AGRGAR NODOS AL GRAFO
for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))  # Color inicial de los nodos

# CREAR DE ARISTAS ENTRE NODOS CON VALENCIAS
edges = [
    ('R', 'M', 2), ('R', 'Q', 6), ('R', 'P', 2), ('O', 'M', 5), ('P', 'O', 9),
    ('O', 'I', 7), ('O', 'B', 5), ('M', 'J', 7), ('M', 'B', 8), ('M', 'A', 9),
    ('Q', 'L', 7), ('J', 'L', 1), ('J', 'K', 8), ('B', 'A', 5), ('B', 'I', 4),
    ('A', 'E', 2), ('A', 'D', 9), ('D', 'H', 4), ('D', 'K', 3), ('E', 'D', 6),
    ('E', 'H', 8), ('E', 'G', 8), ('I', 'G', 8), ('G', 'H', 8)
]

# AGREGAR ARISTAS AL GRAFO
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# -----------------------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Cambia el color del nodo si se presiona la tecla correspondiente
            key = pygame.key.name(event.key).upper()  # Obtiene la tecla presionada en mayúsculas
            if key in G.nodes:
                G.nodes[key]['color'] = (255, 0, 0)  # Cambia el color a rojo (o cualquier otro color)

    screen.fill((255, 255, 255))  # fondo

    # Dibuja el grafo
    for node, data in G.nodes(data=True):
        x, y = data['pos']
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 20)  # Dibuja el nodo como círculo
        color = data['color']  # Obtiene el color del nodo
        pygame.draw.circle(screen, color, (x, y), 20)  # Dibuja el nodo con su color actual
        font = pygame.font.SysFont(None, 24)
        label = font.render(node, True, (255, 255, 255))  # Etiqueta del nodo
        screen.blit(label, (x - 10, y - 10))

    for edge in G.edges(data=True):
        start_pos = G.nodes[edge[0]]['pos']
        end_pos = G.nodes[edge[1]]['pos']
        weight = edge[2]['weight']
        pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 2)  # Dibuja la arista
        
        # peso de arista
        mid_x = (start_pos[0] + end_pos[0]) // 2
        mid_y = (start_pos[1] + end_pos[1]) // 2
        label = font.render(str(weight), True, (0, 0, 0))
        screen.blit(label, (mid_x, mid_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
