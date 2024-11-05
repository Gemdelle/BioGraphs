import os
import pygame

class Euler3Seed:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        self.rect = pygame.Rect(0, 0, 100, 100)  # Rectángulo inicial con dimensiones adecuadas
        self.is_colliding = False
        self.tooltip_text = "frog"
        self.current_text_length = 0
        self.last_update_time = 0
        self.typing_speed = 100  # Tiempo en milisegundos entre cada carácter
        self.visible = True

    def load_frame(self, index):
        if index not in self.frames:
            frame_path = os.path.join("./assets/giphs/seeds/euler-3-seed", f'euler-3-seed.png{index}.gif')
            if os.path.exists(frame_path):
                surf = pygame.image.load(frame_path).convert_alpha()
                surf = pygame.transform.scale(surf, (90, 90))  # Escalar a 80x80 píxeles
                self.frames[index] = surf
            else:
                self.frames[index] = None  # Marca como None si el frame no existe

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        self.frame_index = (current_time // 30) % 74  # Suponiendo 74 frames
        self.load_frame(self.frame_index)  # Cargar solo el frame actual

    def draw(self, screen, x, y):
        # Centrar el rect en (x, y)
        self.rect.center = (x, y)

        if self.frames[self.frame_index] is not None:
            # Dibujar la imagen centrada en el rectángulo
            screen.blit(self.frames[self.frame_index], self.rect.topleft)

        self.visible = True
