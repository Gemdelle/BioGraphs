# COMMON FLOWER FUNCTIONS
import pygame
import os

def load_frame(flower, index):
    if index not in flower.frames:
        # Utiliza el atributo `flower_name` para formar el path dinámicamente
        frame_path = os.path.join(
            "./assets/giphs/flowers-black", 
            flower.flower_name, 
            f"{flower.flower_name}{index}.gif"
        )
        if os.path.exists(frame_path):
            surf = pygame.image.load(frame_path).convert_alpha()
            surf = pygame.transform.scale(surf, (160, 160))
            flower.frames[index] = surf
        else:
            flower.frames[index] = None  # Marcar como None si el frame no existe

def update_animation(flower):
    current_time = pygame.time.get_ticks()
    flower.frame_index = (current_time // 30) % flower.total_frames  # Usa `total_frames` para cada flor
    load_frame(flower, flower.frame_index)

def draw(flower, screen, x, y):
    flower.rect.x = x
    flower.rect.y = y
    was_visible = flower.visible

    if not was_visible:
        load_frame(flower, flower.frame_index)
    if flower.frames[flower.frame_index] is not None:
        screen.blit(flower.frames[flower.frame_index], (flower.rect.x, flower.rect.y))
    flower.visible = True
