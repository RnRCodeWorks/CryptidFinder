from cryptid_assistant.Modules.tileNode import Structure
STANDING_STONE = 'standing_stone'
ABANDONED_SHACK = 'abandoned_shack'
alpha = {
    1: {
        'terrain': [],
        'structure': [],
        'territory': ['bear'],
        'range': [0, 2]
    },
    2: {
        'terrain':['w','m'],
        'structure':[],
        'territory':[],
        'range': [0]
    },
    3: {
        'terrain': ['m'],
        'structure': [],
        'territory': [],
        'range': [0, 1]
    },
    4: {},
    5: {},
    6: {},
    7: {},
    8: {},
    9: {
        'terrain': ['s', 'm'],
        'structure': [],
        'territory': [],
        'range': [0]
    },
    10: {
        'terrain': ['f', 'w'],
        'structure': [],
        'territory': [],
        'range': [0]
    },
    11: {},
    12: {
        'terrain': ['f'],
        'structure': [],
        'territory': [],
        'range': [0, 1]
    },
    13: {
        'terrain': [],
        'structure': [Structure(STANDING_STONE, 'white'), Structure(ABANDONED_SHACK, 'white')],
        'territory': [],
        'range': [0, 3]
    },
    14: {},
    15: {},
    16: {},
    17: {
        'terrain': [],
        'structure': [],
        'territory': ['cougar'],
        'range': [0, 2]
    },
    18: {
        'terrain': [],
        'structure': [Structure(STANDING_STONE, 'blue'), Structure(ABANDONED_SHACK, 'blue')],
        'territory': [],
        'range': [0, 3]
    },
    19: {
        'terrain': ['s'],
        'structure': [],
        'territory': [],
        'range': [0, 1]
    },
    20: {
        'terrain': [],
        'structure': [Structure(STANDING_STONE, 'green'), Structure(ABANDONED_SHACK, 'green')],
        'territory': [],
        'range': [0, 3]
    },
    84: {
        'terrain': [],
        'structure': [],
        'territory': ['bear', 'cougar'],
        'range': [0, 1]
    }
}
beta = {
    1: {
        'terrain': ['d', 's'],
        'structure': [],
        'territory': [],
        'range': [0]
    },
    79: {
        'terrain':[],
        'structure':[Structure(STANDING_STONE, 'white'),Structure(ABANDONED_SHACK, 'white')],
        'territory':[],
        'range': [0,3]
    }
}
gamma = {
    6: {
        'terrain': [],
        'structure': [Structure(STANDING_STONE, 'blue'), Structure(ABANDONED_SHACK, 'blue')],
        'territory': [],
        'range': [0, 3]
    }
}
delta = {}
epsilon = {
    28: {
        'terrain': [],
        'structure': [Structure(STANDING_STONE, 'green'),Structure(ABANDONED_SHACK, 'green')],
        'territory': [],
        'range': [0, 3]
    },
    67: {
        'terrain': ['d'],
        'structure': [],
        'territory': [],
        'range': [0, 1]
    }
}