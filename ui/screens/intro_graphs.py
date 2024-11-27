from core.screens import Screens
from ui.screens.common.dialogue_renderer import render_tutorial_dialogue
from ui.utils.config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui.utils.video import Video
from ui.utils.fonts import font

intro_graphs_video = Video(SCREEN_WIDTH, SCREEN_HEIGHT, "./assets/videos/tutorial-graph.mp4")


def render_intro_graphs(screen, go_to_level):
    intro_graphs_video.reset_clock()
    intro_graphs_video.play_video(screen, lambda: go_to_level(Screens.INSTRUCTIONS))
    render_tutorial_dialogue(screen, 'To navigate a graph, start at a chosen node and move along its edges to '
                                     'connected nodes.\n\nYou can only move to nodes that are directly connected by an '
                                     'edge,\nregardless of the direction!', font)
