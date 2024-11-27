game_map_progress = {
    'Erlem': {
        'enabled': True,
        'completed': False,
        'goesTo': 'Frood'
    },
    'Ulfex': {
        'enabled': True,
        'completed': False,
        'goesTo': 'Twyle'
    },
    'Twyle': {
        'enabled': True,
        'completed': False,
        'goesTo': 'Bloona'
    },
    'Bloona': {
        'enabled': True,
        'completed': False,
        'goesTo': None
    },
    'Frood': {
        'enabled': True,
        'completed': False,
        'goesTo': 'Orrox'
    },
    'Orrox': {
        'enabled': True,
        'completed': False,
        'goesTo': None
    },
    'Spyx': {
        'enabled': True,
        'completed': False,
        'goesTo': None
    },
    'Uchya': {
        'enabled': True,
        'completed': False,
        'goesTo': None
    },
}


def complete_level(level_name):
    game_map_progress[level_name]['completed'] = True
    next_level = game_map_progress[level_name]['goesTo']
    game_map_progress[next_level]['enabled'] = True
