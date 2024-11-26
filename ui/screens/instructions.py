import pygame

from core.screens import Screens
from ui.screens.common.dialogue_renderer import render_dialogue, render_tutorial_dialogue
from ui.screens.common.main_menu_button_renderer import render_main_menu_button
from ui.screens.game_modes import draw_image_button
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT

from ui.utils.fonts import title_font, font, font_small_buttons

# Button setup
button_width, button_height = 600, 80
button_spacing = 20
button_texts = [
    ("Graphs", Screens.INTRO_GRAPHS),
    ("Digraphs", Screens.INTRO_DIGRAPHS),
    ("Euler path", Screens.INTRO_EULER_PATH),
    ("Hamilton path", Screens.INTRO_HAMILTON_PATH)
]

# Colors
background_color = (255, 255, 255)  # White
button_color = (173, 216, 230)  # Light blue
text_color = (0, 0, 0)  # Black
circle_color = (255, 182, 193)  # Light pink
border_color = (0, 0, 0)  # Black

# Calculate button positions
button_x = (SCREEN_WIDTH - button_width) // 2
buttons_start_y = (SCREEN_HEIGHT - len(button_texts) * (button_height + button_spacing)) // 2.3

# Text box setup
text_box_width, text_box_height = 1400, 100
text_box_x = (SCREEN_WIDTH - text_box_width) // 2
text_box_y = SCREEN_HEIGHT - text_box_height - 50

# Circle setup
circle_radius = 50
circle_x = text_box_x - circle_radius - 20
circle_y = text_box_y + text_box_height // 2
is_instructions_screen_rendered = False
main_menu_button_clicked_instructions = None
def render_instructions(screen):
    global is_instructions_screen_rendered, main_menu_button_clicked_instructions, font
    background_image = pygame.image.load("./assets/tutorial-background.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    title_text = title_font.render("TUTORIALS", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4.5))
    screen.blit(title_text, title_rect)

    # Dibuja los botones
    buttons = []
    button_spacing = 100  # Reduce el espacio entre botones
    start_height = SCREEN_HEIGHT // 3.2  # Mueve el inicio un poco más arriba

    for i, (text, target_screen) in enumerate(button_texts):  # Renombrar 'screen' a 'target_screen'
        # Button size and coordinates
        button_image = pygame.image.load("./assets/playground-button.png").convert_alpha()
        button_image = pygame.transform.scale(button_image, (400, 85))

        # Adjust vertical spacing
        rect = button_image.get_rect(center=(SCREEN_WIDTH // 2, start_height + i * button_spacing))

        # Draw button with image and text
        buttons.append((target_screen, draw_image_button(screen, button_image, rect, text, font)))


    render_tutorial_dialogue(screen, 'What do you want to know more about?', font)

    main_menu_button_clicked_instructions = render_main_menu_button(screen, font_small_buttons, (1500, 30))

    is_instructions_screen_rendered = True


def handle_instructions_mouse_down(event, go_to_level, is_screen_on_focus):
    global main_menu_button_clicked_instructions, is_instructions_screen_rendered
    if not is_screen_on_focus or not is_instructions_screen_rendered:
        return

    if main_menu_button_clicked_instructions is not None and main_menu_button_clicked_instructions.collidepoint(event.pos):
        go_to_level(Screens.MAIN)
        is_instructions_screen_rendered = False
    else:
        for i, (text, screen_value) in enumerate(button_texts):
            button_y = buttons_start_y + i * (button_height + button_spacing)
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            if button_rect.collidepoint(event.pos):
                go_to_level(screen_value)
                is_instructions_screen_rendered = False
                break
