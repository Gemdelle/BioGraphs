import pygame
from ui.utils.common_graphic_functions import load_frame, update_animation, draw


class DarkEgg:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.is_colliding = False
        self.tooltip_text = "frog"
        self.current_text_length = 0
        self.last_update_time = 0
        self.typing_speed = 100  # Time in milliseconds between each character
        self.visible = False
        self.name = "dark"
        self.total_frames = 248

    def load_frame(self, index):
        load_frame(self, index)  # Llamada a la función importada

    def update_animation(self):
        update_animation(self)  # Llamada a la función importada

    def draw(self, screen, x, y):
        draw(self, screen, x, y)  # Llamada a la función importada
