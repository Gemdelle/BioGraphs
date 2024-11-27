from core.screens import Screens
from ui.screens.common.dialogue_renderer import render_tutorial_dialogue
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui.utils.video import Video
from ui.utils.fonts import font

intro_hamilton_path_video = Video(SCREEN_WIDTH, SCREEN_HEIGHT, "./assets/videos/tutorial-hamilton.mp4")


def render_intro_hamilton_path(screen, go_to_level):
    intro_hamilton_path_video.reset_clock()
    intro_hamilton_path_video.play_video(screen, lambda: go_to_level(Screens.INSTRUCTIONS))
    render_tutorial_dialogue(screen, 'To complete a Hamiltonian path, whether in a graph or digraph,\nyou must '
                                     'pass through all nodes exactly once.\n\nYou can repeat edges, but NOT nodes!',
                             font)
