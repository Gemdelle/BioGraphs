import pygame
import networkx as nx

from ui.screens.graph_renderer import render_graph

# Crear un DiGraph para representar el digrafo
G = nx.DiGraph()

# Definir posiciones de los nodos
positions = {
    'A': (100, 300), 'B': (50, 100), 'C': (200, 100), 'D': (150, 250),
    'E': (50, 400), 'F': (150, 450), 'G': (250, 400), 'H': (300, 300),
    'I': (400, 100), 'J': (400, 400)
}
for node, pos in positions.items():
    G.add_node(node, pos=pos, color=(0, 0, 0))

# Definir múltiples aristas con direcciones específicas para formar un camino hamiltoniano en el digrafo
edges = [
    ('B', 'A'), ('A', 'C'), ('C', 'D'), ('D', 'F'),
    ('F', 'E'), ('E', 'G'), ('G', 'H'), ('H', 'I'),
    ('I', 'J'), ('J', 'A'), ('A', 'F'), ('F', 'C'),
    ('C', 'H'), ('H', 'D'), ('D', 'J'), ('J', 'E')
]
for edge in edges:
    G.add_edge(edge[0], edge[1])

# Variables para el juego
start_node = None
end_node = 'J'
path = []
timer_started = False
start_time = 0

current_node = None

initial_energy = 17
energy = initial_energy  # Energía inicial
start_ticks = pygame.time.get_ticks()  # Tiempo de inicio
timer_duration = 60000  # 60 segundos


# Función de renderizado con flechas en aristas
def render_digrafos_hamilton_1(screen, font):
    global timer_started, start_time, path, start_node, positions, current_node, energy

    if not timer_started:
        start_time = pygame.time.get_ticks()
        timer_started = True

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    remaining_time = max(0, 60000 - elapsed_time)  # 1 minuto (60000 ms)

    # Actualizar energía en función del tiempo restante
    if remaining_time > 0:
        energy = initial_energy * (remaining_time / timer_duration)
    else:
        energy = initial_energy  # Resetear energía si se acaba el tiempo

    # Renderizar el grafo con flechas
    render_graph_with_arrows(screen, G, font,positions)

    # Dibujar la barra de energía
    pygame.draw.rect(screen, (200, 0, 0), (10, 10, int(energy * 20), 20))

    # Dibujar el texto del temporizador
    timer_text = font.render(f"Time: {remaining_time // 1000}s", True, (0, 0, 0))
    screen.blit(timer_text, (10, 40))

    # Verificar si se acabó el tiempo
    if remaining_time <= 0:
        print("Time's up! You lost.")
        energy = initial_energy
        current_node = None
        for node in G.nodes():
            G.nodes[node]['color'] = (0, 0, 0)  # Resetear color de los nodos
        return False

    return False


# Función para renderizar el grafo con flechas
def render_graph_with_arrows(screen, G, font, positions):
    screen.fill((255, 255, 255))  # Fondo blanco
    for u, v in G.edges():
        start_pos = positions[u]
        end_pos = positions[v]
        # Dibujar flechas
        pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 2)
        draw_arrow(screen, start_pos, end_pos)  # Función auxiliar para flechas

    for node, pos in positions.items():
        color = G.nodes[node]['color']
        pygame.draw.circle(screen, color, pos, 20)
        node_text = font.render(node, True, (255, 255, 255))
        screen.blit(node_text, (pos[0] - 10, pos[1] - 10))


# Función auxiliar para dibujar una flecha en una línea
def draw_arrow(screen, start, end):
    # Calcular dirección y longitud del vector de la flecha
    arrow_length = 10
    angle = pygame.math.Vector2(end[0] - start[0], end[1] - start[1]).angle_to((1, 0))
    arrow_vector = pygame.math.Vector2(arrow_length, 0).rotate(angle)

    # Calcular los puntos para la flecha
    arrow_pos1 = (end[0] - arrow_vector.x - arrow_vector.y, end[1] - arrow_vector.y + arrow_vector.x)
    arrow_pos2 = (end[0] - arrow_vector.x + arrow_vector.y, end[1] - arrow_vector.y - arrow_vector.x)

    pygame.draw.polygon(screen, (0, 0, 0), [end, arrow_pos1, arrow_pos2])


# Función para manejar eventos de teclas en el digrafo de Hamilton
def handle_digrafos_hamilton_1_keydown(event):
    global current_node
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()

        if key in G.nodes:
            if current_node is None:
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
            elif key in G.successors(current_node):  # Solo moverse a nodos sucesores válidos
                G.nodes[current_node]['color'] = (0, 100, 0)
                current_node = key
                G.nodes[current_node]['color'] = (255, 0, 0)
                path.append(current_node)

                # Verificar si el camino hamiltoniano está completo
                if current_node == end_node and len(path) == len(G.nodes):
                    print("Congratulations! You completed the Hamiltonian Path.")
                    return True, current_node
    return False, current_node
