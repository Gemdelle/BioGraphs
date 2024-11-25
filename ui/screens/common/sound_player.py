import pygame


def play_sound(sound_name):
    """
    Reproduce un archivo de sonido desde la carpeta 'assets/sounds/base/'.

    :param sound_name: Nombre del archivo de sonido (incluyendo extensión).
    """
    # Inicializar el mixer si no está inicializado
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Ruta base para los sonidos
    base_path = "./assets/sounds/base/"
    sound_path = f"{base_path}{sound_name}"

    # Cargar y reproducir el sonido
    try:
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(loops=-1)  # Reproducir en loop
    except pygame.error as e:
        print(f"Error al reproducir el sonido {sound_name}: {e}")
