import os
import pygame

class Euler2SeedDisabled:
    def __init__(self):
        def __init__(self):
            self.frames = {}
            self.frame_index = 1
            self.rect = pygame.Rect(0, 0, 100, 100)
            self.last_update_time = 0
            self.visible = True
            # Parámetros específicos de la animación
            self.path = "./assets/giphs/seeds-b&w/euler-2-seed"
            self.file_prefix = "euler-2-seed.png"
            self.scale = (90, 90)  # Ajusta esto si el tamaño varía

        def load_frame(self, index):
            # Llama a la función de `seed_functions` y pasa `self` junto con los parámetros específicos
            load_frame(self, index, path=self.path, file_prefix=self.file_prefix, scale=self.scale)

        def update_animation(self):
            # Llama a la función de `seed_functions` para actualizar la animación
            update_animation(self)

        def draw(self, screen, x, y):
            # Llama a la función de `seed_functions` para dibujar el frame actual en la pantalla
            draw(self, screen, x, y)
