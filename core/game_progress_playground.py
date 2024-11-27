game_playground_progress = {
    'B': {
        'enabled': True,
        'completed': False,
        'goesTo': 'C'
    },
    'C': {
        'enabled': True,
        'completed': False,
        'goesTo': 'D'
    },
    'D': {
        'enabled': True,
        'completed': False,
        'goesTo': 'E'
    },
    'E': {
        'enabled': True,
        'completed': False,
        'goesTo': 'F'
    },
    'F': {
        'enabled': True,
        'completed': False,
        'goesTo': 'F'
    }
}


def complete_level(level_name):
    game_playground_progress[level_name]['completed'] = True
    next_level = game_playground_progress[level_name]['goesTo']
    game_playground_progress[next_level]['enabled'] = True
