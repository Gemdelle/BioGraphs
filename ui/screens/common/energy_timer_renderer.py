import pygame

def render_energy_and_timer(screen, font, initial_energy, energy, timer_duration, remaining_time):
    # Cargar imágenes dentro de la función
    background_bar_img = pygame.image.load("./assets/timer/background-bar.png").convert_alpha()
    liquid_bar_img = pygame.image.load("./assets/timer/liquid.png").convert_alpha()
    foreground_bar_img = pygame.image.load("./assets/timer/foreground-bar.png").convert_alpha()

    # Escalar las imágenes al tamaño deseado
    background_bar_img = pygame.transform.scale(background_bar_img, (initial_energy*40,50))
    liquid_bar_img = pygame.transform.scale(liquid_bar_img, (int(energy * 40), 50))
    foreground_bar_img = pygame.transform.scale(foreground_bar_img, (initial_energy*40+80,90))

    # Draw the time bar
    screen.blit(background_bar_img, (110+130, 50))
    screen.blit(liquid_bar_img, (110+130, 50))
    screen.blit(foreground_bar_img, (90+130, 30))

    # Draw the timer text
    timer_text = font.render(f"{remaining_time // 1000}", True, (255, 255, 255))
    screen.blit(timer_text, (50+950, 60))