import os
import pygame


class AnimatedSprite:
    def __init__(self, frame_path, frame_size=(100, 100), frame_count=1):
        self.frame_path = frame_path
        self.frame_size = frame_size
        self.frame_count = frame_count
        self.frames = {}
        self.frame_index = 0
        self.rect = pygame.Rect(0, 0, *self.frame_size)
        self.visible = False

    def load_frame(self, index):
        """Carga el frame si no fue cargado previamente."""
        if index not in self.frames:
            frame_file = f"{self.frame_path}{index}.gif"
            if os.path.exists(frame_file):
                surf = pygame.image.load(frame_file).convert_alpha()
                surf = pygame.transform.scale(surf, self.frame_size)
                self.frames[index] = surf
            else:
                self.frames[index] = None  # Marca como None si el frame no existe

    def update_animation(self):
        """Actualiza el índice de frame basado en el tiempo actual."""
        current_time = pygame.time.get_ticks()
        self.frame_index = (current_time // 30) % self.frame_count  # Cambia cada 30ms
        self.load_frame(self.frame_index)

    def draw(self, screen, x, y):
        """Dibuja el frame actual en la posición especificada con el pivot en el centro."""
        self.rect.center = (x, y)
        if not self.visible:
            self.load_frame(self.frame_index)
        if self.frames[self.frame_index] is not None:
            screen.blit(self.frames[self.frame_index], self.rect.topleft)
        self.visible = True
