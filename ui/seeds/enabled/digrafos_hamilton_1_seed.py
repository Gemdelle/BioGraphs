import os
import pygame
from ui.seeds.common.seed_functions import load_frame, update_animation, draw

class DigrafosHamilton1Seed:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.is_colliding = False
        self.tooltip_text = "frog"
        self.current_text_length = 0
        self.last_update_time = 0
        self.typing_speed = 100  # Tiempo entre cada carácter
        self.visible = True
        # Parámetros específicos de la animación
        self.path = "./assets/giphs/seeds/d-hamilton-seed"
        self.file_prefix = "d-hamilton-seed"
        self.scale = (80, 80)  # Puedes cambiar esto si el tamaño varía

    def load_frame(self, index):
        # Llama a la función de `seed_functions` y pasa `self` junto con los parámetros específicos
        load_frame(self, index, path=self.path, file_prefix=self.file_prefix, scale=self.scale)

    def update_animation(self):
        # Llama a la función de `seed_functions` para actualizar la animación
        update_animation(self)

    def draw(self, screen, x, y):
        # Llama a la función de `seed_functions` para dibujar el frame actual en la pantalla
        draw(self, screen, x, y)
