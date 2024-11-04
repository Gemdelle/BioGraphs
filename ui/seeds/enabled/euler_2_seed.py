import os
import pygame

class Euler2Seed:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        self.is_colliding = False
        self.tooltip_text = "frog"
        self.current_text_length = 0
        self.last_update_time = 0
        self.typing_speed = 100  # Time in milliseconds between each character
        self.visible = True

    def load_frame(self, index):
        if index not in self.frames:
            frame_path = os.path.join("./assets/giphs/seeds/euler-2-seed", f'euler-2-seed.png{index}.gif')
            if os.path.exists(frame_path):
                surf = pygame.image.load(frame_path).convert_alpha()
                # Escalar la imagen a 90x90 píxeles
                surf = pygame.transform.scale(surf, (80, 80))
                self.frames[index] = surf
            else:
                self.frames[index] = None  # Marca como None si el frame no existe

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        self.frame_index = (current_time // 30) % 74  # Suponiendo 74 frames
        self.load_frame(self.frame_index)  # Carga el frame actual si no está cargado

    def draw(self, screen, x, y):
        # Cargar el frame si es necesario
        if self.frames[self.frame_index] is not None:
            # Obtener ancho y alto del frame actual
            frame_width, frame_height = self.frames[self.frame_index].get_size()
            # Calcular coordenadas centradas
            centered_x = x - frame_width // 2
            centered_y = y - frame_height // 2
            # Dibujar la imagen centrada
            screen.blit(self.frames[self.frame_index], (centered_x, centered_y))

        self.visible = True
