import pygame


def render_restart_button(screen, font, font_buttons):
    # Draw the "Restart" button
    restart_button_rect = pygame.Rect(1500, 30, 200, 60)
    pygame.draw.rect(screen, (0, 0, 0), restart_button_rect, width=5, border_radius=15)

    restart_button_text = font_buttons.render("RESTART", True, (0, 0, 0))
    screen.blit(restart_button_text, (1510, 40))

    return restart_button_rect