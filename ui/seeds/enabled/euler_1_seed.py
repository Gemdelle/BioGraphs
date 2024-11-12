import os
import pygame

import os
import pygame


class Euler1Seed:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        # Asegúrate de que el rect tenga un tamaño inicial correcto
        self.rect = pygame.Rect(0, 0, 100, 100)  # Ajustar a las dimensiones de la imagen
        self.is_colliding = False
        self.tooltip_text = "frog"
        self.current_text_length = 0
        self.last_update_time = 0
        self.typing_speed = 100  # Tiempo en milisegundos entre cada caracter
        self.visible = True

    def load_frame(self, index, transformx, transformy):
        if index not in self.frames:
            frame_path = os.path.join("./assets/giphs/seeds/euler-1-seed", f'euler-1-seed.png{index}.gif')
            if os.path.exists(frame_path):
                surf = pygame.image.load(frame_path).convert_alpha()
                surf = pygame.transform.scale(surf, (transformx, transformy))
                self.frames[index] = surf
            else:
                self.frames[index] = None  # Marcar como None si el frame no existe

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        self.frame_index = (current_time // 30) % 74  # Asumiendo 74 frames
        self.load_frame(self.frame_index, 90, 90)  # Cargar solo el frame actual

    def draw(self, screen, x, y):
        # Centrar el rect en (x, y)
        self.rect.center = (x, y)

        was_visible = self.visible

        if not was_visible:
            self.load_frame(self.frame_index)

        if self.frames[self.frame_index] is not None:
            # Dibujar la imagen centrada en el rectángulo
            screen.blit(self.frames[self.frame_index], self.rect.topleft)

        self.visible = True
