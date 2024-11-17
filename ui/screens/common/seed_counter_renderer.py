import pygame

def render_counter(screen, font, missing_element, seed):
    # Cargar y ajustar la imagen del botón
    counter_image = pygame.image.load("./assets/seed-counter.png").convert_alpha()
    counter_image = pygame.transform.scale(counter_image, (180, 180))

    # Calcula la posición del botón (ajusta la posición según tu necesidad)
    counter_rect = counter_image.get_rect(center=(120, 120))

    # Dibujar la imagen del botón
    screen.blit(counter_image, counter_rect.topleft)

    # Actualizar la animación de la semilla
    seed.update_animation()

    # Dibujar la semilla centrada en el botón
    seed_x = counter_rect.centerx  # Centro del botón en el eje X
    seed_y = counter_rect.centery  # Centro del botón en el eje Y
    seed.draw(screen, seed_x, seed_y)

    # Dibuja el texto en el botón (por ejemplo, mostrando el conteo de semillas)
    seed_text = font.render(f"{missing_element}", True, (255, 255, 255))  # Texto en color negro
    seed_text_rect = seed_text.get_rect(center=counter_rect.center)
    screen.blit(seed_text, seed_text_rect)