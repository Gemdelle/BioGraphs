import pygame

def render_digrafos_euler_1(screen, G, font, energy, remaining_time):
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (200, 0, 0), (10, 10, int(energy * 20), 20))

    timer_text = font.render(f"Tiempo: {remaining_time // 1000}s", True, (0, 0, 0))
    screen.blit(timer_text, (10, 40))

    for node, data in G.nodes(data=True):
        x, y = data['pos']
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 20)
        color = data['color']
        pygame.draw.circle(screen, color, (x, y), 20)

        node_label = font.render(node, True, (255, 255, 255))
        screen.blit(node_label, (x - 10, y - 10))

    for edge in G.edges():
        start_pos = G.nodes[edge[0]]['pos']
        end_pos = G.nodes[edge[1]]['pos']
        pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 2)


def handle_graph_events(G, current_node, event):
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key).upper()
        if current_node is None:
            current_node = key
            G.nodes[current_node]['color'] = (255, 0, 0)
        elif key in G.neighbors(current_node):
            G.nodes[current_node]['color'] = (0, 100, 0)
            current_node = key
            G.nodes[current_node]['color'] = (255, 0, 0)
    return current_node