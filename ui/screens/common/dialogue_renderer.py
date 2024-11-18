import pygame
import networkx as nx

from core.pet import get_selected_pet
from ui.config import SCREEN_WIDTH, SCREEN_HEIGHT

# Colors
text_white = (255, 255, 255) 
text_black = (0,0,0)

# Text box setup
text_box_width, text_box_height = 1200, 250
text_box_x = (SCREEN_WIDTH - text_box_width) // 2
text_box_y = SCREEN_HEIGHT - text_box_height - 80

# Circle setup
circle_radius = 145
circle_x = text_box_x - 10
circle_y = text_box_y + text_box_height // 2

def render_dialogue(screen, text, font, avatar_mood="neutral"):
    # Cargar las imágenes de los marcos
    dialogue_frame = pygame.image.load("./assets/dialogue/dialogue-frame.png").convert_alpha()
    character_frame = pygame.image.load("./assets/dialogue/character-frame.png").convert_alpha()

    # Escalar las imágenes al tamaño adecuado
    dialogue_frame = pygame.transform.scale(dialogue_frame, (text_box_width + 30, text_box_height + 20))
    character_frame = pygame.transform.scale(character_frame, (circle_radius * 2 + 50, circle_radius * 2 + 50))

    # Dibuja el marco del diálogo
    screen.blit(dialogue_frame, (text_box_x, text_box_y))

    # Dibuja el marco del personaje 
    screen.blit(character_frame, (circle_x - circle_radius - 25, circle_y - circle_radius - 25))

    avatar = get_selected_pet(size=(220, 220), mood=avatar_mood)
    # Actualiza y dibuja la animación del avatar dentro del marco del personaje
    avatar.update_animation()
    avatar.draw(screen, circle_x, circle_y)

    # Dividir el texto usando el salto de línea \n
    lines = text.split('\n')

    # Calcular la altura total del texto para centrarlo
    total_text_height = len(lines) * font.get_height()
    y_offset = text_box_y + (text_box_height - total_text_height) // 2  # Centrar verticalmente

    # Ajuste para mover el texto un poco hacia abajo y hacia la derecha
    x_offset = 35  # Mover a la derecha
    y_offset += 25  # Mover un poco hacia abajo

    # Dibujar el texto línea por línea
    for line in lines:
        prompt_text = font.render(line, True, text_white)
        prompt_rect = prompt_text.get_rect(center=(text_box_x + text_box_width // 2 + x_offset, y_offset))
        screen.blit(prompt_text, prompt_rect)
        y_offset += font.get_height()  # Mover hacia abajo para la siguiente línea


def render_playground_dialogue(screen, text, font, mood):
    # Cargar las imágenes de los marcos
    dialogue_frame = pygame.image.load("./assets/dialogue/playground-dialogue-frame.png").convert_alpha()
    dialogue_frame = pygame.transform.scale(dialogue_frame, (1450, 410))

    # Dibuja el marco del diálogo (en lugar del rectángulo relleno)
    screen.blit(dialogue_frame, (150, 590))

    if mood == 'happy':
        avatar = get_selected_pet(size=(290, 290), mood="happy")
    else: 
        avatar = get_selected_pet()
    # Actualiza y dibuja la animación del avatar dentro del marco del personaje
    avatar.update_animation()
    avatar.draw(screen, circle_x + 100, circle_y - 10)

    # Dividir el texto usando el salto de línea \n
    lines = text.split('\n')

    # Calcular la altura total del texto para centrarlo en la caja
    text_box_width = 1450  # Ancho del marco de diálogo
    text_box_height = 350  # Alto del marco de diálogo
    text_box_x = 150
    text_box_y = 630

    total_text_height = len(lines) * font.get_height()
    y_offset = text_box_y + (text_box_height - total_text_height) // 2  # Centrar verticalmente

    # Ajuste para mover el texto un poco hacia abajo y hacia la derecha
    x_offset = 65  # Mover a la derecha
    y_offset += 35  # Mover un poco hacia abajo

    # Dibujar el texto línea por línea
    for line in lines:
        prompt_text = font.render(line, True, text_black)
        prompt_rect = prompt_text.get_rect(center=(text_box_x + text_box_width // 2 + x_offset, y_offset))
        screen.blit(prompt_text, prompt_rect)
        y_offset += font.get_height()  # Mover hacia abajo para la siguiente línea


