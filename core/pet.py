from ui.animated_sprite import AnimatedSprite

selected_pet = [None]

def get_selected_pet(size=(150, 150)):
    if selected_pet[0] is not None and selected_pet[0].upper() == "DARK":
        return AnimatedSprite(frame_path="./assets/giphs/frog/frog-dark/frog-dark", frame_size=size, frame_count=192)
    elif selected_pet[0] is not None and selected_pet[0].upper() == "NEUTRAL":
        return AnimatedSprite(frame_path="./assets/giphs/frog/frog-neutral/frog-neutral", frame_size=size, frame_count=192)
    elif selected_pet[0] is not None and selected_pet[0].upper() == "SWAMP":
        return AnimatedSprite(frame_path="./assets/giphs/frog/frog-swamp/frog-swamp", frame_size=size, frame_count=192)
    return None