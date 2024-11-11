from ui.frog.dark_frog import DarkFrog
from ui.frog.neutral_frog import NeutralFrog
from ui.frog.swamp_frog import SwampFrog

selected_pet = [None]

def get_selected_pet():
    if selected_pet[0] == "DARK":
        return DarkFrog()
    elif selected_pet[0] == "NEUTRAL":
        return NeutralFrog()
    elif selected_pet[0] == "SWAMP":
        return SwampFrog()
    return None
