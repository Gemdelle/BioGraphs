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

def render_dialog(screen, text, font):
    # Cargar las imágenes de los marcos
    dialogue_frame = pygame.image.load("./assets/dialogue/dialogue-frame.png").convert_alpha()
    character_frame = pygame.image.load("./assets/dialogue/character-frame.png").convert_alpha()

    # Escalar las imágenes al tamaño adecuado
    dialogue_frame = pygame.transform.scale(dialogue_frame, (text_box_width, text_box_height))
    character_frame = pygame.transform.scale(character_frame, (circle_radius * 2+150, circle_radius * 2+50))

    # Dibuja el marco del diálogo
    screen.blit(dialogue_frame, (text_box_x, text_box_y))

    # Dibuja el marco del personaje 
    screen.blit(character_frame, (circle_x - circle_radius-70, circle_y - circle_radius-25))

    avatar = get_selected_pet()
    # Actualiza y dibuja la animación del avatar dentro del marco del personaje
    avatar.update_animation()
    avatar.draw(screen, circle_x, circle_y)

    # Dibuja el texto en el marco de diálogo
    prompt_text = font.render(text, True, text_white)
    prompt_rect = prompt_text.get_rect(center=(text_box_x + text_box_width // 2, text_box_y + text_box_height // 2))
    screen.blit(prompt_text, prompt_rect)

def render_playground_dialogue(screen, text, font):
    # Cargar las imágenes de los marcos
    dialogue_frame = pygame.image.load("./assets/dialogue/playground-dialogue-frame.png").convert_alpha()
    dialogue_frame = pygame.transform.scale(dialogue_frame, (1450, 350))

    # Dibuja el marco del diálogo (en lugar del rectángulo relleno)
    screen.blit(dialogue_frame, (150, 630))

    avatar = get_selected_pet()
    # Actualiza y dibuja la animación del avatar dentro del marco del personaje
    avatar.update_animation()
    avatar.draw(screen, circle_x+100, circle_y-10)

    # Dibuja el texto en el marco de diálogo
    prompt_text = font.render(text, True, text_black)
    prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH//2+100, text_box_y + text_box_height // 2))
    screen.blit(prompt_text, prompt_rect)

