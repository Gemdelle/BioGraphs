import pygame
import networkx as nx

from ui.config import SCREEN_WIDTH, SCREEN_HEIGHT

# Colors
background_color = (255, 255, 255)  # White
button_color = (173, 216, 230)  # Light blue
text_color = (0, 0, 0)  # Black
circle_color = (255, 182, 193)  # Light pink
border_color = (0, 0, 0)  # Black

# Text box setup
text_box_width, text_box_height = 1200, 150
text_box_x = (SCREEN_WIDTH - text_box_width) // 2
text_box_y = SCREEN_HEIGHT - text_box_height - 50

# Circle setup
circle_radius = 100
circle_x = text_box_x - 20
circle_y = text_box_y + text_box_height // 2
def render_dialog(screen, text, font, avatar):
    # Dibuja la caja de texto
    pygame.draw.rect(screen, background_color, (text_box_x, text_box_y, text_box_width, text_box_height), border_radius=20)
    pygame.draw.rect(screen, border_color, (text_box_x, text_box_y, text_box_width, text_box_height), 2, border_radius=20)

    # Dibuja el círculo a la izquierda de la caja de texto
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    avatar.update_animation()
    avatar.draw(screen, circle_x-75, circle_y-75)

    # Dibuja el texto del prompt en la caja de texto
    prompt_text = font.render(text, True, text_color)
    prompt_rect = prompt_text.get_rect(center=(text_box_x + text_box_width // 2, text_box_y + text_box_height // 2))
    screen.blit(prompt_text, prompt_rect)
