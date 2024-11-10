import os
import pygame
from ui.flowers.common import load_frame, update_animation, draw

class DHamilton1FlowerBlack:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.is_colliding = False
        self.tooltip_text = "frog"
        self.current_text_length = 0
        self.last_update_time = 0
        self.typing_speed = 100  # Tiempo en milisegundos entre cada carácter
        self.visible = False

        # Atributos específicos para cada flor
        self.flower_name = "d-hamilton-flower-black"  # Cambia este nombre según la flor
        self.total_frames = 74  # Número total de frames para la animación

    def load_frame(self, index):
        load_frame(self, index)  # Llama a la función común

    def update_animation(self):
        update_animation(self)  # Llama a la función común

    def draw(self, screen, x, y):
        draw(self, screen, x, y)  # Llama a la función común
