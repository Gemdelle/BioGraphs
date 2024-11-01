import pygame
import networkx as nx

from core.screens import Screens
from ui.screens.digrafos_euler_1 import render_digrafos_euler_1
from ui.screens.digrafos_hamilton_1 import render_digrafos_hamilton_1
from ui.screens.grafos_euler_1 import handle_graph_events, render_grafos_euler_1
from ui.screens.grafos_hamilton_1 import render_grafos_hamilton_1
from ui.screens.grafos_hamilton_2 import render_grafos_hamilton_2
from ui.screens.grafos_hamilton_3 import render_grafos_hamilton_3
from ui.screens.main import render_main
from ui.screens.splash import render_splash

pygame.init()
pygame.font.init()

# CONFIGURACIÓN DE PANTALLA
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

Grafo = nx.Graph()

positions = {
    'A': (100, 300), 'B': (50, 100), 'C': (200, 100), 'D': (150, 250),
    'E': (50, 400), 'F': (150, 450)
}

for node, pos in positions.items():
    Grafo.add_node(node, pos=pos, color=(0, 0, 0))

edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'E'), ('A', 'D'), ('D', 'F'),
    ('E', 'D')
]

for edge in edges:
    Grafo.add_edge(edge[0], edge[1])

running = True
current_node = None

font = pygame.font.SysFont(None, 36)

screen_selected = Screens.SPLASH
start_ticks = pygame.time.get_ticks()
timer_duration = 30000

def goToMain():
    global screen_selected
    screen_selected = Screens.MAIN
def goToLevel(screen):
    global screen_selected
    screen_selected = screen


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if screen_selected == Screens.GRAFOS_EULER_1:
            current_node = handle_graph_events(Grafo, current_node, event)

    if screen_selected == Screens.SPLASH:
        render_splash(screen, goToMain)
    elif screen_selected == Screens.MAIN:
        render_main(screen, goToLevel)
    elif screen_selected == Screens.GRAFOS_EULER_1:
        render_grafos_euler_1(screen, Grafo, font, 0)
    elif screen_selected == Screens.GRAFOS_HAMILTON_1:
        completed = render_grafos_hamilton_1(screen, font)
        if completed:
            print("Hamiltonian path completed!")
            screen_selected = Screens.MAIN
    elif screen_selected == Screens.GRAFOS_HAMILTON_2:
        energy = 0
        render_grafos_hamilton_2(screen, Grafo, font, energy)
    elif screen_selected == Screens.GRAFOS_HAMILTON_3:
        energy = 0
        render_grafos_hamilton_3(screen, Grafo, font, energy)
    elif screen_selected == Screens.DIGRAFOS_EULER_1:
        energy = 0
        render_digrafos_euler_1(screen, Grafo, font, energy)
    elif screen_selected == Screens.DIGRAFOS_HAMILTON_1:
        energy = 0
        render_digrafos_hamilton_1(screen, Grafo, font, energy)
    else:
        print("Screen not found")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
