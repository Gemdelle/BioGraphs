from core.screens import Screens
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui.utils.video import Video

intro_euler_path_video = Video(SCREEN_WIDTH, SCREEN_HEIGHT, "./assets/videos/tutorial-euler.mp4")

def render_intro_euler_path(screen, go_to_level):
    intro_euler_path_video.reset_clock()
    intro_euler_path_video.play_video(screen, lambda: go_to_level(Screens.INSTRUCTIONS))
