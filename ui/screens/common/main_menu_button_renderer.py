import pygame


def render_main_menu_button(screen, font_buttons, position=(1500, 150)):
    # Carga y ajusta la imagen del botón
    button_image = pygame.image.load("./assets/button.png").convert_alpha()
    button_image = pygame.transform.scale(button_image, (180, 50))

    # Calcula la posición del botón (usando el rectángulo de la imagen)
    main_button_rect = button_image.get_rect(topleft=position)

    # Dibuja solo la imagen del botón
    screen.blit(button_image, main_button_rect.topleft)

    # Dibuja el texto en el botón
    map_button_text = font_buttons.render("MENU", True, (0, 0, 0))
    text_rect = map_button_text.get_rect(center=main_button_rect.center)
    screen.blit(map_button_text, text_rect.topleft)

    return main_button_rect