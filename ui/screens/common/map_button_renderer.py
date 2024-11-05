import pygame


def render_map_button(screen, font, font_buttons):
    # Draw the "Map" button
    map_button_rect = pygame.Rect(1500, 90, 200, 60)
    pygame.draw.rect(screen, (0, 0, 0), map_button_rect, width=5, border_radius=15)

    map_button_text = font_buttons.render("MAP", True, (0, 0, 0))
    screen.blit(map_button_text, (1510, 100))

    return map_button_rect