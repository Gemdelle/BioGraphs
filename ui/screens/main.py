import pygame


def render_main_screen(screen, font):
    from graph import SCREEN_WIDTH
    from graph import SCREEN_HEIGHT
    screen.fill((255, 255, 255))
    title_text = font.render("BioGraphs", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(title_text, title_rect)

    # Button definitions
    button_texts = ["Instructions", "Playground", "Map"]
    buttons = []
    for i, text in enumerate(button_texts):
        rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + i * 70, 200, 50)
        buttons.append((text, draw_rounded_button(screen, rect, text, font)))

    return buttons  # Return button rects for click handling


def draw_rounded_button(screen, rect, text, font, border_radius=10, border_color=(0, 0, 0), fill_color=(200, 200, 200), border_width=3):
    pygame.draw.rect(screen, border_color, rect, border_radius=border_radius)
    inner_rect = rect.inflate(-border_width * 2, -border_width * 2)
    pygame.draw.rect(screen, fill_color, inner_rect, border_radius=border_radius)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=inner_rect.center)
    screen.blit(text_surface, text_rect)
    return rect