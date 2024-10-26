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
    'A': (100, 300), 'B': (50, 100), 'C': (200, 100), 'D': (150, 250),
    'E': (50, 400), 'F': (150, 450)
}

# AGREGAR NODOS AL GRAFO
for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))  # Color inicial de los nodos

# CREAR ARISTAS ENTRE NODOS
edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'E'), ('A', 'D'), ('D', 'F'),
    ('E', 'D')
]

# AGREGAR ARISTAS AL GRAFO
for edge in edges:
    G.add_edge(edge[0], edge[1])

# Variables del juego
running = True
current_node = None
font = pygame.font.SysFont(None, 36)
initial_energy = 17  # Energía inicial y ancho máximo de la barra
energy = initial_energy  # Nivel de energía actual

# Configuración del temporizador
start_ticks = pygame.time.get_ticks()
timer_duration = 30000  # 30 segundos
energy_decrement = initial_energy / (timer_duration / 1000)  # Decremento cada segundo

while running:
    # Calcular el tiempo transcurrido desde el inicio del juego
    elapsed_time = pygame.time.get_ticks() - start_ticks
    remaining_time = max(0, timer_duration - elapsed_time)

    # Actualizar la barra de energía
    if remaining_time > 0:
        energy = initial_energy * (remaining_time / timer_duration)
    else:
        # Reiniciar el juego cuando el tiempo llega a cero
        energy = initial_energy
        start_ticks = pygame.time.get_ticks()
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Restablecer el color de los nodos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key).upper()
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
            # Viajar a nodo adyacente
            elif key in G.neighbors(current_node):
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)

    screen.fill((255, 255, 255))  # Fondo

    # Dibujar la barra de energía
    pygame.draw.rect(screen, (200, 0, 0), (10, 10, int(energy * 20), 20))

    # Dibujar el temporizador debajo de la barra de energía
    timer_text = font.render(f"Tiempo: {remaining_time // 1000}s", True, (0, 0, 0))
    screen.blit(timer_text, (10, 40))

    # Dibujar el grafo
    for node, data in G.nodes(data=True):
        x, y = data['pos']
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 20)  # pintar el fondo negro
        color = data['color']
        pygame.draw.circle(screen, color, (x, y), 20)  # dibujar el círculo con el color correspondiente

        # Dibujar etiquetas
        font = pygame.font.SysFont(None, 24)
        label = font.render(node, True, (255, 255, 255))  # letra del nodo
        screen.blit(label, (x - 10, y - 10))
    for edge in G.edges(data=True):
        start_pos = G.nodes[edge[0]]['pos']
        end_pos = G.nodes[edge[1]]['pos']
        pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 2)  # dibujar la arista

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
