from cryptid_assistant.Modules.tileNode import Structure
STANDING_STONE = 'standing_stone'
ABANDONED_SHACK = 'abandoned_shack'
alpha = {
    # 1: {
    #     'terrain':[],
    #     'structure':[],
    #     'territory':['bear'],
    #     'range': [0,2]
    # },
    2: {
        'terrain':['w','m'],
        'structure':[],
        'territory':[],
        'range': [0]
    }
}
beta = {
    79: {
        'terrain':[],
        'structure':[Structure(STANDING_STONE, 'white'),Structure(ABANDONED_SHACK, 'white')],
        'territory':[],
        'range': [0,3]
    }
}
epsilon = {
    28: {
        'terrain': [],
        'structure': [Structure(STANDING_STONE, 'green'),Structure(ABANDONED_SHACK, 'green')],
        'territory': [],
        'range': [0, 3]
    }
}