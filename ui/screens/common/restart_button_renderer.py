import pygame


def render_restart_button(screen, font_buttons):
    # Carga y ajusta la imagen del botón
    button_image = pygame.image.load("./assets/button.png").convert_alpha()
    button_image = pygame.transform.scale(button_image, (180, 50))

    # Calcula la posición del botón (usando el rectángulo de la imagen)
    restart_button_rect = button_image.get_rect(topleft=(1500, 90))

    # Dibuja solo la imagen del botón
    screen.blit(button_image, restart_button_rect.topleft)

    # Dibuja el texto en el botón
    map_button_text = font_buttons.render("RESTART", True, (0, 0, 0))
    text_rect = map_button_text.get_rect(center=restart_button_rect.center)
    screen.blit(map_button_text, text_rect.topleft)

    return restart_button_rect

def render_playground_restart_button(screen, font_buttons):
    # Carga y ajusta la imagen del botón
    button_image = pygame.image.load("./assets/playground-button.png").convert_alpha()
    button_image = pygame.transform.scale(button_image, (180, 50))

    # Calcula la posición del botón (usando el rectángulo de la imagen)
    restart_button_rect = button_image.get_rect(topleft=(1500, 90))

    # Dibuja solo la imagen del botón
    screen.blit(button_image, restart_button_rect.topleft)

    # Dibuja el texto en el botón
    map_button_text = font_buttons.render("RESTART", True, (0, 0, 0))
    text_rect = map_button_text.get_rect(center=restart_button_rect.center)
    screen.blit(map_button_text, text_rect.topleft)

    return restart_button_rect