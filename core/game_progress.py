game_progress = {
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
        'enabled': False,
        'completed': False,
        'goesTo': 'Bloona'
    },
    'Bloona': {
        'enabled': False,
        'completed': False,
        'goesTo': None
    },
    'Frood': {
        'enabled': False,
        'completed': False,
        'goesTo': 'Orrox'
    },
    'Orrox': {
        'enabled': False,
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
    game_progress[level_name]['completed'] = True
    next_level = game_progress[level_name]['goesTo']
    game_progress[next_level]['enabled'] = True
