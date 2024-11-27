import pygame


def render_sign(screen, graph):
    sign_image = pygame.image.load(f"./assets/signs/{graph}.png").convert_alpha()
    sign_image = pygame.transform.scale(sign_image, (310, 120))

    # Calcula la posición del botón (ajusta la posición según tu necesidad)
    sign_image_rect = sign_image.get_rect(center=(340, 120))

    # Dibujar la imagen del botón
    screen.blit(sign_image, sign_image_rect)


def render_hamilton_sign(screen):
    # Cargar y ajustar la imagen del botón
    sign_image = pygame.image.load("./assets/signs/euler.png").convert_alpha()
    sign_image = pygame.transform.scale(sign_image, (310, 120))

    # Calcula la posición del botón (ajusta la posición según tu necesidad)
    sign_image_rect = sign_image.get_rect(center=(340, 120))

    # Dibujar la imagen del botón
    screen.blit(sign_image, sign_image_rect)