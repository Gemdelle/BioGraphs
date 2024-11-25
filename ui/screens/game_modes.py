import os

import pygame
import random
import math

from ui.screens.common.sound_player import play_sound
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT


class MovingImage:
    def __init__(self, screen_width, screen_height):
        # Choose a random fish image from 1 to 4
        tadpole_number = random.randint(1, 4)
        image_path = os.path.join("assets", "tadpole", f"tadpole-{tadpole_number}.png")

        # Diccionario con tamaños personalizados según el número de la imagen
        size_by_index = {
            1: (94-20, 28-5),   # Tamaño para tadpole-1.png
            2: (114-20, 24-5),  # Tamaño para tadpole-2.png
            3: (91, 64),        # Tamaño para tadpole-3.png
            4: (115, 91)        # Tamaño para tadpole-4.png
        }
        
        # Selecciona el tamaño según el número de imagen
        selected_size = size_by_index.get(tadpole_number, (75, 50))

        # Load and scale the image
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, selected_size)
        self.image = self.original_image  # Set the initial image to the original

        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Direccion y posicion inicial
        self.direction = random.choice([-1, 1])  # Movement direction
        
        # Ajuste de posición inicial para que aparezcan desde fuera de la pantalla
        if self.direction == 1:
            self.x = -self.image.get_width()  # Inicia fuera del lado izquierdo
        else:
            self.x = self.screen_width  # Inicia fuera del lado derecho

        # Spawn en el 20% superior o inferior de la pantalla
        top_or_bottom = random.choice(["top", "bottom"])
        if top_or_bottom == "top":
            self.y = random.randint(0, int(screen_height * 0.2))  # 20% superior
        else:
            self.y = random.randint(int(screen_height * 0.7), screen_height)  # 20% inferior


        self.speed = random.uniform(1, 2)  # Random speed for each image
        self.angle = random.uniform(0, 2 * math.pi)

        # Flip the image if the initial direction is -1
        if self.direction == -1:
            self.image = pygame.transform.flip(self.original_image, True, False)

    def update(self):
        # Movimiento horizontal en forma de onda
        self.x += self.speed * self.direction
        self.y += math.sin(self.angle) * 2  # Oscilación vertical para simular movimiento en el agua
        self.angle += 0.05  # Controla la frecuencia de oscilación

        # Resetear la posición horizontal cuando salga de la pantalla
        if self.direction == 1 and self.x > self.screen_width:
            self.x = -self.image.get_width()  # Reinicia desde el lado izquierdo
        elif self.direction == -1 and self.x < -self.image.get_width():
            self.x = self.screen_width  # Reinicia desde el lado derecho

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



def render_main_screen(screen, title_font, font, moving_images):
    # Song
    play_sound('button.mp3')

    # Background
    background_image = pygame.image.load("assets/main-bg.png").convert()
    background_image = pygame.transform.scale(background_image, (1710, 1034))
    screen.blit(background_image, (0, 0))

    # Title
    title_text = title_font.render("GRAPH HOPPER", True, (0, 0, 0))
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
