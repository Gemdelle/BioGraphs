from core.screens import Screens
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui.utils.video import Video

intro_graphs_video = Video(SCREEN_WIDTH, SCREEN_HEIGHT, "./assets/videos/tutorial-graph.mp4")
def render_intro_graphs(screen, go_to_level):
    intro_graphs_video.reset_clock()
    intro_graphs_video.play_video(screen, lambda: go_to_level(Screens.INSTRUCTIONS))
