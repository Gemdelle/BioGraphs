import pygame

def render_main_screen(screen, title_font, font):
    from graph import SCREEN_WIDTH, SCREEN_HEIGHT

    # Fondo
    background_image = pygame.image.load("assets/main-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    # Título
    title_text = title_font.render("BIOGRAPHS", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5))
    screen.blit(title_text, title_rect)

    # Botones
    button_texts = ["Instructions", "Playground", "Map"]
    buttons = []
    for i, text in enumerate(button_texts):
        # Coordenadas y tamaño del botón
        button_image = pygame.image.load("./assets/button.png").convert_alpha()
        button_image = pygame.transform.scale(button_image, (300, 80))
        
        # Ajustar separación vertical (cambiado de 70 a 100)
        rect = button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5 + i * 100))
        
        # Dibujar el botón con imagen y texto
        buttons.append((text, draw_image_button(screen, button_image, rect, text, font)))

    return buttons


def draw_image_button(screen, image, rect, text, font):
    # Dibujar imagen del botón
    screen.blit(image, rect)
    
    # Agregar texto encima del botón
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
    
    return rect
