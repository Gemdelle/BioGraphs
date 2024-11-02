import pygame


start_scale = 1
target_scale = 1.4
total_duration = 2
frames_per_second = 60

scale_change_per_frame = (target_scale - start_scale) / (total_duration * frames_per_second)

current_scale = start_scale

def render_splash(screen, go_to_map):
    global current_scale

    background_image = pygame.image.load("assets/splash_background.png").convert()
    background_rect = background_image.get_rect()
    logo_image = pygame.image.load("assets/UB_logo.jpg").convert()
    logo_rect = logo_image.get_rect()

    current_scale += scale_change_per_frame
    current_scale = min(current_scale, target_scale)

    if current_scale < target_scale:
        new_width = int(background_rect.width * current_scale)
        new_height = int(background_rect.height * current_scale)
        new_logo_width = int(logo_rect.width * current_scale)
        new_logo_height = int(logo_rect.height * current_scale)

        scaled_background = pygame.transform.scale(background_image, (new_width, new_height))
        scaled_rect = scaled_background.get_rect(center=screen.get_rect().center)

        scaled_logo = pygame.transform.scale(logo_image, (new_logo_width, new_logo_height))
        scaled_logo_rect = scaled_logo.get_rect(center=screen.get_rect().center)

        ############################
        screen.fill((255, 255, 255))
        screen.blit(scaled_background, scaled_rect)
        screen.blit(scaled_logo, scaled_logo_rect)
    else:
        go_to_map()
