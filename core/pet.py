from ui.utils.animated_sprite import AnimatedSprite

selected_pet = [None]

def get_selected_pet(size=(290, 290), mood="neutral"):
    if selected_pet[0] is not None and selected_pet[0].upper() == "DARK":
        return AnimatedSprite(frame_path=f"./assets/giphs/frog/{mood}/frog-dark/frog-dark", frame_size=size, frame_count=192)
    elif selected_pet[0] is not None and selected_pet[0].upper() == "NEUTRAL":
        return AnimatedSprite(frame_path=f"./assets/giphs/frog/{mood}/frog-common/frog-common", frame_size=size, frame_count=192)
    elif selected_pet[0] is not None and selected_pet[0].upper() == "SWAMP":
        return AnimatedSprite(frame_path=f"./assets/giphs/frog/{mood}/frog-swamp/frog-swamp", frame_size=size, frame_count=192)
    return None