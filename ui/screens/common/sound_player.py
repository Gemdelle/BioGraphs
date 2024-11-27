import pygame


# Variable global para rastrear la música actual
current_music = None


def play_sound(sound_name, volume=1.0):
    """
    Reproduce un archivo de sonido desde la carpeta 'assets/sounds/' sin reiniciar si ya está sonando.

    :param sound_name: Nombre del archivo de sonido (incluyendo extensión).
    :param volume: Volumen del sonido (valor entre 0.0 y 1.0).
    """
    global current_music

    # Inicializar el mixer si no está inicializado
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Ruta base para los sonidos
    base_path = "./assets/sounds/"
    sound_path = f"{base_path}{sound_name}"

    # Verifica si ya está sonando la misma música
    if current_music == sound_name and pygame.mixer.music.get_busy():
        return  # No reiniciar la música

    # Cargar y reproducir la nueva música
    try:
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.set_volume(volume)  # Establecer el volumen
        pygame.mixer.music.play(loops=-1)  # Reproducir en loop
        current_music = sound_name  # Actualizar la música actual
    except pygame.error as e:
        print(f"Error al reproducir el sonido {sound_name}: {e}")


def play_button(sound_name):
    """
    Reproduce un archivo de sonido desde la carpeta 'assets/sounds/' al máximo volumen.

    :param sound_name: Nombre del archivo de sonido (incluyendo extensión).
    """
    # Inicializar el mixer si no está inicializado
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Ruta base para los sonidos
    base_path = "./assets/sounds/"
    sound_path = f"{base_path}{sound_name}"

    try:
        # Cargar y reproducir el efecto de sonido
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(1.0)  # Volumen máximo
        sound.play()
    except pygame.error as e:
        print(f"Error al reproducir el sonido {sound_name}: {e}")


