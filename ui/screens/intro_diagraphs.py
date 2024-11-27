
from core.screens import Screens
from ui.screens.common.dialogue_renderer import render_tutorial_dialogue
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui.utils.video import Video
from ui.utils.fonts import font

intro_digraphs_video = Video(SCREEN_WIDTH, SCREEN_HEIGHT, "./assets/videos/tutorial-digraph.mp4")


def render_intro_diagraphs(screen, go_to_level):
    intro_digraphs_video.reset_clock()
    intro_digraphs_video.play_video(screen, lambda: go_to_level(Screens.INSTRUCTIONS))
    render_tutorial_dialogue(screen, 'For a digraph, start at a chosen node and move along its directed edges to '
                                     'connected nodes.\n\nBe careful, you can only move to nodes that are connected\nby'
                                     'edges in the direction specified!', font)
