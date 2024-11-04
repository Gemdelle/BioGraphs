import os
import pygame

class Euler1Seed:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        # Asegúrate de que el rect tenga un tamaño inicial correcto
        self.rect = pygame.Rect(0, 0, 90, 90)  # Ajustar a las dimensiones de la imagen
        self.is_colliding = False
        self.tooltip_text = "frog"
        self.current_text_length = 0
        self.last_update_time = 0
        self.typing_speed = 100  # Time in milliseconds between each character
        self.visible = True

    def load_frame(self, index):
        if index not in self.frames:
            frame_path = os.path.join("./assets/giphs/seeds/euler-1-seed", f'euler-1-seed.png{index}.gif')
            if os.path.exists(frame_path):
                surf = pygame.image.load(frame_path).convert_alpha()
                surf = pygame.transform.scale(surf, (80, 80))
                self.frames[index] = surf
            else:
                self.frames[index] = None  # Mark as None if the frame does not exist

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        self.frame_index = (current_time // 30) % 74  # Assuming 74 frames
        self.load_frame(self.frame_index)  # Lazy load the current frame

    def draw(self, screen, x, y):
        self.rect.x = x
        self.rect.y = y
        was_visible = self.visible

        if not was_visible:
            self.load_frame(self.frame_index)
        if self.frames[self.frame_index] is not None:
            screen.blit(self.frames[self.frame_index], (self.rect.x, self.rect.y))
        self.visible = True