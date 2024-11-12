from ui.animated_sprite import AnimatedSprite

selected_pet = [None]

def get_selected_pet():
    if selected_pet[0] == "DARK":
        return AnimatedSprite(frame_path="./assets/giphs/frog/frog-dark/frog-dark", frame_size=(400, 400), frame_count=192)
    elif selected_pet[0] == "NEUTRAL":
        return AnimatedSprite(frame_path="./assets/giphs/frog/frog-neutral/frog-neutral", frame_size=(400, 400), frame_count=248)
    elif selected_pet[0] == "SWAMP":
        return AnimatedSprite(frame_path="./assets/giphs/frog/frog-swamp/frog-swamp", frame_size=(150, 150), frame_count=192)
    return None