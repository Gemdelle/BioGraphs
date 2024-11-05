import pygame

def render_energy_and_timer(screen, font, energy, timer_duration, remaining_time):
    # Draw the energy bar
    pygame.draw.rect(screen, (200, 0, 0), (110, 30, int(energy * 40), 50))

    # Draw the timer text
    timer_text = font.render(f"{remaining_time // 1000}", True, (0, 0, 0))
    screen.blit(timer_text, (50, 50))