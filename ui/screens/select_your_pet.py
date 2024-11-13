import os
import pygame


from core.screens import Screens
from ui.egg.dark_egg import DarkEgg
from ui.egg.neutral_egg import NeutralEgg
from ui.egg.swamp_egg import SwampEgg
from core.pet import selected_pet

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1710, 1034
CHARACTER_SIZE = (300, 300)  # Size for each character image
BUTTON_SIZE = (300, 70)  # Size for the button

selected_character = None

def render_select_your_pet_screen(screen, go_to_level):
    global selected_character  # Use the global variable to keep the selection across frames

    # Load background
    background_image = pygame.image.load("assets/eggs-background.png").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background_image, (0, 0))

    # Load character
    characters = [
        {"animation": DarkEgg(), "name": "Dark"},
        {"animation": NeutralEgg(), "name": "Neutral"},
        {"animation": SwampEgg(), "name": "Swamp"}
    ]

    # Calculate positions for characters
    spacing = 50
    start_x = (SCREEN_WIDTH - (3 * CHARACTER_SIZE[0] + 2 * spacing)) // 2
    y_position = SCREEN_HEIGHT // 2 - CHARACTER_SIZE[1] // 2 - 100

    # Colors for highlighting
    selected_color = (0, 255, 0)  # Green (selected)

    # Detect if a character is clicked and set it as selected
    if pygame.mouse.get_pressed()[0]:  # Left mouse button click
        for idx, character in enumerate(characters):
            x_position = start_x + idx * (CHARACTER_SIZE[0] + spacing)
            rect = pygame.Rect(x_position, y_position, *CHARACTER_SIZE)
            if rect.collidepoint(pygame.mouse.get_pos()):
                selected_character = idx
                selected_pet[0] = character["name"]

    # Render each character
    for idx, character in enumerate(characters):
        x_position = start_x + idx * (CHARACTER_SIZE[0] + spacing)
        rect = pygame.Rect(x_position, y_position, *CHARACTER_SIZE)

        # Draw character animation
        character["animation"].update_animation()
        character["animation"].draw(screen, rect.topleft[0], rect.topleft[1])

        # Draw character name, highlighted if selected
        font = pygame.font.Font(os.path.join('assets/fonts/', 'Alice_in_Wonderland_3.ttf'), 40)
        name_color = selected_color if selected_character == idx else (255, 255, 255)
        text_surface = font.render(character["name"], True, name_color)
        text_rect = text_surface.get_rect(center=(rect.centerx, rect.bottom + 30))
        screen.blit(text_surface, text_rect)

    # Draw Select button
    button_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_SIZE[0]) // 2, SCREEN_HEIGHT - 150, *BUTTON_SIZE)
    button_color = (200, 0, 0) if button_rect.collidepoint(pygame.mouse.get_pos()) else (150, 0, 0)
    pygame.draw.rect(screen, button_color, button_rect)

    # Button text
    button_text = font.render("Select Pet", True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

    # Check if button clicked
    if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if selected_pet[0] is not None:
            go_to_level(Screens.MAIN)

