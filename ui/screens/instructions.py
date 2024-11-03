import pygame


def render_instructions(screen):
    from graph import SCREEN_WIDTH
    from graph import SCREEN_HEIGHT
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont(None, 36)
    title_text = font.render("INSTRUCTIONS", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(title_text, title_rect)