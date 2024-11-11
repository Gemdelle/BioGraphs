# COMMON FUNCTIONS
import pygame
import os

# COMMON TO ALL ELEMENTS
def update_animation(element):
    current_time = pygame.time.get_ticks()
    element.frame_index = (current_time // 30) % element.total_frames  # Usa `total_frames` para cada flor
    load_frame(element, element.frame_index)

#EGGS
def load_frame(egg, index):
    if index not in egg.frames:
        frame_path = os.path.join(
            f"./assets/giphs/egg/{egg.name}", 
            f"{egg.name}{index}.gif"
        )
        if os.path.exists(frame_path):
            surf = pygame.image.load(frame_path).convert_alpha()
            surf = pygame.transform.scale(surf, (400, 400))
            egg.frames[index] = surf
        else:
            egg.frames[index] = None  

def draw(element, screen, x, y):
    element.rect.x = x
    element.rect.y = y
    was_visible = element.visible

    if not was_visible:
        load_frame(element, element.frame_index)
    if element.frames[element.frame_index] is not None:
        screen.blit(element.frames[element.frame_index], (element.rect.x-60, element.rect.y-60))
    element.visible = True




