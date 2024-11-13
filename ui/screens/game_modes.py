import os

import pygame
import random
import math

from ui.config import SCREEN_WIDTH, SCREEN_HEIGHT


class MovingImage:
    def __init__(self, screen_width, screen_height):
        # Choose a random fish image from 1 to 3
        fish_number = random.randint(1, 3)
        image_path = os.path.join("assets", "fish", f"fish-{fish_number}.png")

        # Load and scale the image
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (75, 50))  # Adjust the size of the moving images
        self.image = self.original_image  # Set the initial image to the original

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(0, screen_width)

        # Spawn in the top 20% or bottom 20% of the screen
        top_or_bottom = random.choice(["top", "bottom"])
        if top_or_bottom == "top":
            self.y = random.randint(0, int(screen_height * 0.16))  # Top 16%
        else:
            self.y = random.randint(int(screen_height * 0.6), screen_height)  # Bottom 40%

        self.speed = random.uniform(1, 2)  # Random speed for each image
        self.direction = random.choice([-1, 1])  # Movement direction
        self.angle = random.uniform(0, 2 * math.pi)

        # Flip the image if the initial direction is -1
        if self.direction == -1:
            self.image = pygame.transform.flip(self.original_image, True, False)

    def update(self):
        # Horizontal wave-like movement
        self.x += self.speed * self.direction
        self.y += math.sin(self.angle) * 2  # Vertical oscillation to mimic ocean movement
        self.angle += 0.05  # Controls the frequency of oscillation

        # Reset horizontal position when the image goes off-screen
        if self.x > self.screen_width or self.x < -self.image.get_width():
            self.x = -self.image.get_width() if self.direction == 1 else self.screen_width
            # Respawn in the top or bottom 20% of the screen
            top_or_bottom = random.choice(["top", "bottom"])
            if top_or_bottom == "top":
                self.y = random.randint(0, int(self.screen_height * 0.16))
            else:
                self.y = random.randint(int(self.screen_height * 0.6), self.screen_height)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


def render_main_screen(screen, title_font, font, moving_images):
    # Background
    background_image = pygame.image.load("assets/main-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    # Title
    title_text = title_font.render("BIOGRAPHS", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5))
    screen.blit(title_text, title_rect)

    # Buttons
    button_texts = ["Instructions", "Playground", "Map"]
    buttons = []
    for i, text in enumerate(button_texts):
        # Button size and coordinates
        button_image = pygame.image.load("./assets/button.png").convert_alpha()
        button_image = pygame.transform.scale(button_image, (300, 80))

        # Adjust vertical spacing
        rect = button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5 + i * 100))

        # Draw button with image and text
        buttons.append((text, draw_image_button(screen, button_image, rect, text, font)))

    # Update and draw each moving image
    for image in moving_images:
        image.update()
        image.draw(screen)

    return buttons


def draw_image_button(screen, image, rect, text, font):
    # Draw button image
    screen.blit(image, rect)

    # Add text on top of the button
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    return rect
