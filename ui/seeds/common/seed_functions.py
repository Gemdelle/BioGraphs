import os
import pygame

def load_frame(self, index, path, file_prefix, scale=(80, 80)):
    """Carga un cuadro específico de una animación.
    
    Parámetros:
        index (int): Índice del cuadro a cargar.
        path (str): Ruta base de los cuadros.
        file_prefix (str): Prefijo del nombre del archivo.
        file_extension (str): Extensión del archivo.
        scale (tuple): Tamaño de la imagen escalada (ancho, alto).
    """
    if index not in self.frames:
        frame_path = os.path.join(path, f'{file_prefix}{index}.gif')
        if os.path.exists(frame_path):
            surf = pygame.image.load(frame_path).convert_alpha()
            surf = pygame.transform.scale(surf, scale)
            self.frames[index] = surf
        else:
            self.frames[index] = None  # Marcar como None si el cuadro no existe

def update_animation(self, frame_rate=30, total_frames=74):
    """Actualiza el cuadro actual de la animación.
    
    Parámetros:
        frame_rate (int): Duración de cada cuadro en milisegundos.
        total_frames (int): Número total de cuadros en la animación.
    """
    current_time = pygame.time.get_ticks()
    self.frame_index = (current_time // frame_rate) % total_frames
    self.load_frame(self.frame_index)  # Carga perezosa del cuadro actual

def draw(self, screen, x, y):
    """Dibuja el cuadro actual de la animación en la pantalla.
    
    Parámetros:
        screen (Surface): Pantalla de pygame en la que dibujar.
        x (int): Posición x en la pantalla.
        y (int): Posición y en la pantalla.
    """
    was_visible = self.visible
    self.rect.center = (x, y)

    if not was_visible:
        self.load_frame(self.frame_index)
    if self.frames[self.frame_index] is not None:
        screen.blit(self.frames[self.frame_index], self.rect.topleft)
    self.visible = True

