import pygame


def render_main_menu_button(screen, font, font_buttons):
    # Draw the "main menu" button
    main_button_rect = pygame.Rect(1500, 150, 200, 60)
    pygame.draw.rect(screen, (0, 0, 0), main_button_rect, width=5, border_radius=15)

    main_button_text = font_buttons.render("MENU", True, (0, 0, 0))
    screen.blit(main_button_text, (1510, 160))

    return main_button_rect