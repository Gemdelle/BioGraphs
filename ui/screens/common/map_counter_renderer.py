import pygame

def counter_renderer(screen, font, total_nodes, missing_nodes, element, img_size_x, img_size_y):
    # Cargar y ajustar la imagen del botón
    counter_image = pygame.image.load("./assets/seed-counter.png").convert_alpha()
    counter_image = pygame.transform.scale(counter_image, (img_size_x, img_size_y)) #120

    # Calcula la posición del botón (ajusta la posición según tu necesidad)
    counter_rect = counter_image.get_rect(center=(1585, 200))

    # Dibujar la imagen del botón
    screen.blit(counter_image, counter_rect.topleft)

    # Actualizar la animación de la semilla
    element.update_animation()

    # Dibujar la semilla centrada en el botón
    element_x = counter_rect.centerx  # Centro del botón en el eje X
    element_y = counter_rect.centery  # Centro del botón en el eje Y
    element.draw(screen, element_x, element_y)

    # Dibuja el texto en el botón (por ejemplo, mostrando el conteo de semillas)
    seed_text = font.render(f"{missing_nodes} / {total_nodes}", True, (255, 255, 255))  # Texto en color negro
    seed_text_rect = seed_text.get_rect(center=counter_rect.center)
    screen.blit(seed_text, seed_text_rect)