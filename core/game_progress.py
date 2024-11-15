game_progress = {
    'Erlem': {
        'enabled': True,
        'completed': False,
        'dependsOn': None
    },
    'Ulfex': {
        'enabled': True,
        'completed': False,
        'dependsOn': None
    },
    'Twyle': {
        'enabled': False,
        'completed': False,
        'dependsOn': 'Ulfex'
    },
    'Bloona': {
        'enabled': False,
        'completed': False,
        'dependsOn': 'Twyle'
    },
    'Frood': {
        'enabled': False,
        'completed': False,
        'dependsOn': 'Erlem'
    },
    'Orrox': {
        'enabled': False,
        'completed': False,
        'dependsOn': 'Frood'
    },
    'Spyx': {
        'enabled': True,
        'completed': False,
        'dependsOn': None
    },
    'Uchya': {
        'enabled': True,
        'completed': False,
        'dependsOn': None
    },
}

def complete_level(level_name):
    game_progress[level_name]['completed'] = True
    previous_level = game_progress[level_name]['dependsOn']
    game_progress[previous_level]['enabled'] = True
