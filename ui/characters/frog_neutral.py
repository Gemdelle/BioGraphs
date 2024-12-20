import os
import pygame


class FrogNeutral:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.is_colliding = False
        self.tooltip_text = "frog"
        self.current_text_length = 0
        self.last_update_time = 0
        self.typing_speed = 100  # Time in milliseconds between each character
        self.visible = False

    def load_frame(self, index):
        if index not in self.frames:
            frame_path = os.path.join("./assets/giphs/frog_neutral_1", f'frog_neutral_1_{index}.png')
            if os.path.exists(frame_path):
                surf = pygame.image.load(frame_path).convert_alpha()
                surf = pygame.transform.scale(surf, (150, 150))
                self.frames[index] = surf
            else:
                self.frames[index] = None  # Mark as None if the frame does not exist

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        self.frame_index = (current_time // 30) % 193  # Assuming 193 frames
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
