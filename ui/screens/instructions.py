import pygame

from core.screens import Screens
from ui.config import SCREEN_WIDTH, SCREEN_HEIGHT

# Button setup
button_width, button_height = 600, 80
button_spacing = 20
button_texts = [
    ("¿Qué es un camino de Euler?", Screens.INTRO_EULER_PATH),
    ("¿Qué es un camino de Hamilton?", Screens.INTRO_HAMILTON_PATH),
    ("¿Qué es un ciclo de Euler?", Screens.INTRO_EULER_CYCLE),
    ("¿Qué es un ciclo de Hamilton?", Screens.INTRO_HAMILTON_CYCLE)
]

# Colors
background_color = (255, 255, 255)  # White
button_color = (173, 216, 230)  # Light blue
text_color = (0, 0, 0)  # Black
circle_color = (255, 182, 193)  # Light pink
border_color = (0, 0, 0)  # Black

# Calculate button positions
button_x = (SCREEN_WIDTH - button_width) // 2
buttons_start_y = (SCREEN_HEIGHT - len(button_texts) * (button_height + button_spacing)) // 2

# Text box setup
text_box_width, text_box_height = 1400, 100
text_box_x = (SCREEN_WIDTH - text_box_width) // 2
text_box_y = SCREEN_HEIGHT - text_box_height - 50

# Circle setup
circle_radius = 50
circle_x = text_box_x - circle_radius - 20
circle_y = text_box_y + text_box_height // 2
is_instructions_screen_rendered = False
back_button_clicked_instructions = None
def render_instructions(screen):
    global is_instructions_screen_rendered, back_button_clicked_instructions
    screen.fill((255, 255, 255))

    font = pygame.font.SysFont(None, 36)
    title_text = font.render("INSTRUCTIONS", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(title_text, title_rect)

    # Dibuja los botones
    for i, (text, screen_value) in enumerate(button_texts):
        button_y = buttons_start_y + i * (button_height + button_spacing)
        pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height), border_radius=20)
        button_text = font.render(text, True, text_color)
        text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(button_text, text_rect)

    # Dibuja la caja de texto
    pygame.draw.rect(screen, background_color, (text_box_x, text_box_y, text_box_width, text_box_height), border_radius=20)
    pygame.draw.rect(screen, border_color, (text_box_x, text_box_y, text_box_width, text_box_height), 2, border_radius=20)

    # Dibuja el círculo a la izquierda de la caja de texto
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Dibuja el texto del prompt en la caja de texto
    prompt_text = font.render("¿Qué querés saber?", True, text_color)
    prompt_rect = prompt_text.get_rect(center=(text_box_x + text_box_width // 2, text_box_y + text_box_height // 2))
    screen.blit(prompt_text, prompt_rect)

    # Dibujar el botón "Back"
    back_button_text = font.render("Back", True, (255, 255, 255))
    back_button_clicked_instructions = pygame.Rect(1610, 10, 80, 40)  # Posición y tamaño del botón
    pygame.draw.rect(screen, (0, 0, 200), back_button_clicked_instructions)  # Fondo del botón
    screen.blit(back_button_text, (1620, 15))  # Texto centrado en el botón

    is_instructions_screen_rendered = True


def is_back_button_clicked_instructions(event):
    global back_button_clicked_instructions, is_instructions_screen_rendered
    is_back_button_clicked = back_button_clicked_instructions is not None and back_button_clicked_instructions.collidepoint(event.pos)
    if is_back_button_clicked:
        is_instructions_screen_rendered = False
    return is_back_button_clicked

def handle_instructions_keydown(event, go_to_level):
    global is_instructions_screen_rendered
    if event.type == pygame.MOUSEBUTTONDOWN and is_instructions_screen_rendered is True:
        for i, (text, screen_value) in enumerate(button_texts):
            button_y = buttons_start_y + i * (button_height + button_spacing)
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            if button_rect.collidepoint(event.pos):
                go_to_level(screen_value)
                break