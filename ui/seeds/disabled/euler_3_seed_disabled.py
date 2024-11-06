import os
import pygame
from ui.seeds.common.seed_functions import load_frame, update_animation, draw

class Euler3SeedDisabled:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.last_update_time = 0
        self.visible = True
        # Parámetros específicos de la animación
        self.path = "./assets/giphs/seeds-b&w/euler-3-seed"
        self.file_prefix = "euler-3-seed.png"
        self.scale = (90, 90)  # Ajusta esto si el tamaño varía

    def load_frame(self, index):
        # Usa la función de `seed_functions` para cargar el frame
        load_frame(self, index, path=self.path, file_prefix=self.file_prefix, scale=self.scale)

    def update_animation(self):
        # Usa la función de `seed_functions` para actualizar la animación
        update_animation(self)

    def draw(self, screen, x, y):
        # Usa la función de `seed_functions` para dibujar el frame actual en la pantalla
        draw(self, screen, x, y)
