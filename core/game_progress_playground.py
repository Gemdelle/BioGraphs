game_playground_progress = {
    'B': {
        'enabled': True,
        'completed': False,
        'goesTo': 'C'
    },
    'C': {
        'enabled': False,
        'completed': False,
        'goesTo': 'D'
    },
    'D': {
        'enabled': False,
        'completed': False,
        'goesTo': 'E'
    },
    'E': {
        'enabled': False,
        'completed': False,
        'goesTo': 'F'
    },
    'F': {
        'enabled': False,
        'completed': False,
        'goesTo': None
    }
}

def complete_level(level_name):
    game_playground_progress[level_name]['completed'] = True
    next_level = game_playground_progress[level_name]['goesTo']
    game_playground_progress[next_level]['enabled'] = True
