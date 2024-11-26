
from core.screens import Screens
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui.utils.video import Video

intro_digraphs_video = Video(SCREEN_WIDTH, SCREEN_HEIGHT, "./assets/videos/tutorial-digraph.mp4")

def render_intro_diagraphs(screen, go_to_level):
    intro_digraphs_video.reset_clock()
    intro_digraphs_video.play_video(screen, lambda: go_to_level(Screens.INSTRUCTIONS))
