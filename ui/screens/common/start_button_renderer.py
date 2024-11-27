import pygame

from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT


def render_start_button(screen, font, seed):
    # Cargar y ajustar la imagen del botón
    start_button_image = pygame.image.load("./assets/start-button.png").convert_alpha()
    start_button_image = pygame.transform.scale(start_button_image, (300, 300))

    # Calcula la posición del botón (ajusta la posición según tu necesidad)
    start_button_rect = start_button_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

    # Dibujar la imagen del botón
    screen.blit(start_button_image, start_button_rect)

    # Actualizar la animación de la semilla
    seed.update_animation()

    # Dibujar la semilla centrada en el botón
    seed_x = start_button_rect.centerx  # Centro del botón en el eje X
    seed_y = start_button_rect.centery  # Centro del botón en el eje Y
    seed.draw(screen, seed_x, seed_y)

    # Dibuja el texto en el botón (por ejemplo, mostrando el conteo de semillas)
    start_text = font.render("START", True, (255, 255, 255)) 
    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    screen.blit(start_text, start_text_rect)
    return start_button_rect