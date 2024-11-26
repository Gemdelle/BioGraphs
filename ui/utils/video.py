import pygame
import numpy as np
from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip


class Video:
    def __init__(self, screen_width, screen_height, clip_path):
        self.clip_path = clip_path
        self.clip = VideoFileClip(clip_path)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.is_clock_reseted = False
        self.initial_time = pygame.time.get_ticks()

    def reload_clip(self):
        self.clip.close()
        self.clip = VideoFileClip(self.clip_path)

    def reset_clock(self):
        if self.is_clock_reseted:
            return
        self.initial_time = pygame.time.get_ticks()
        self.is_clock_reseted = True


    def zoom_frame(self, frame):
        # Convertir el frame a una imagen PIL
        pil_image = Image.fromarray(frame)

        # Obtener dimensiones originales del video
        original_width, original_height = pil_image.size

        # Calcular factor de zoom para cubrir toda la pantalla
        zoom_factor = max(self.screen_width / original_width, self.screen_height / original_height)
        new_width = int(original_width * zoom_factor)
        new_height = int(original_height * zoom_factor)

        # Redimensionar con zoom y centrar
        pil_image = pil_image.resize((new_width, new_height), Image.LANCZOS)

        # Recortar para centrar el video en la pantalla
        left = (new_width - self.screen_width) // 2
        top = (new_height - self.screen_height) // 2
        pil_image = pil_image.crop((left, top, left + self.screen_width, top + self.screen_height))

        return np.array(pil_image)

    def frame_to_surface(self, frame):
        frame = np.rot90(frame)
        frame = np.flipud(frame)
        surface = pygame.surfarray.make_surface(frame)
        return surface

    def play_video(self, screen, go_to_next_screen):
        current_time = (pygame.time.get_ticks() - self.initial_time) / 1000.0

        if current_time < 0:
            current_time = 0.0  # Asegurarse de no tener tiempo negativo o adelantado

        if current_time >= self.clip.duration:
            go_to_next_screen()
            self.reload_clip()
            self.is_clock_reseted = False
        else:
            current_frame = self.clip.get_frame(current_time)
            current_frame = self.zoom_frame(current_frame)
            surface = self.frame_to_surface(current_frame)

            # Rellenar el fondo antes de dibujar el video
            screen.fill((76, 72, 60))

            # Dibujar el video a pantalla completa
            screen.blit(surface, (0, 0))
