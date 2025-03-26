tile_layouts ={
    1:[
        ['w','w','w','w','f','f'],
        ['s','s','w','d','f','f'],
        ['s','s','d','d|cougar','d|cougar','f|cougar']
    ],
    2:[
        ['s|bear','f|bear','f|bear','f','f','f'],
        ['s','s','f','d','d','d'],
        ['s','m','m','m','m','d']
    ],
    3:[
        ['s','s','f','f','f','w'],
        ['s|bear','s|bear','f','m','w','w'],
        ['m|bear','m','m','m','w','w']
    ],
    4:[
        ['d','d','m','m','m','m'],
        ['d','d','m','w','w','w|bear'],
        ['d','d','d','f','f','f|bear']
    ],
    5:[
        ['s','s','s','m','m','m'],
        ['s','d','d','w','m','m|cougar'],
        ['d','d','w','w','w|cougar','w|cougar']
    ],
    6:[
        ['d|cougar','d','s','s','s','f'],
        ['m|cougar','m','s','s','f','f'],
        ['m','w','w','w','w','f']
    ]
}

setup_cards = {
    615432: {
        'inverted':[3, 5],  # not 0 based
        'standing_stones': {'blue':[3,11], 'green':[4,0], 'white':[6,6]}, # 0 based row, col
        'abandoned_shacks': {'blue':[1,4], 'green':[2,5], 'white':[1,0]}, # 0 based row, col
        'clues':{
            3:[42, -1, -1, 13, 2],
            4:[12, 92, -1, 26, 28],
            5:[95, 64, 63, 11, 67]
        }
    },
    613524: {
        'inverted': [1, 2],
        'standing_stones': {'blue':[4,5], 'green':[2,11], 'white':[5,10]},
        'abandoned_shacks': {'blue':[4,8], 'green':[5,5], 'white':[5,2]},
        'clues':{
            3:[61, -1, -1, 49, 21],
            4:[2, 71, -1, 45, 51],
            5:[66, 67, 50, 14, 87]
        }
    },
    215436: {
        'inverted': [5],
        'standing_stones': {'blue':[8,6], 'green':[7,9], 'white':[4,10]},
        'abandoned_shacks': {'blue':[0,6], 'green':[2, 5], 'white':[3,10]},
        'clues':{
            3:[17, 86, 6, -1, -1],
            4:[88, 8, 1, 13, -1],
            5:[26, 34, 27, 85, 86]
        }
    },
    214536: {
        'inverted': [1,3,4,6],
        'standing_stones': {'blue':[1,4], 'green':[7,1], 'white':[3,11]},
        'abandoned_shacks': {'blue':[7,5], 'green':[3, 10], 'white':[2,7]},
        'clues':{
            3:[17, 49, -1, 56, -1],
            4:[95, 6, 6, 40, -1],
            5:[66, 80, 39, 84, 13]
        }
    },
    523641: {
        'inverted': [2,6],
        'standing_stones': {'blue':[6,3], 'green':[0,4], 'white':[0,3]},
        'abandoned_shacks': {'blue':[1,8], 'green':[7, 10], 'white':[8,10]},
        'clues':{
            3:[42, -1, 1, -1, 66],
            4:[19, 89, -1, 30, 89],
            5:[13, 62, 85, 46, 34]
        }
    },
    524136: {
        'inverted': [1,4,6],
        'standing_stones': {'blue':[5,4], 'green':[2,11], 'white':[0,2]},
        'abandoned_shacks': {'blue':[8,3], 'green':[6,6], 'white':[3,9]},
        'clues':{
            3:[17, -1, 11, -1, 66],
            4:[50, 65, -1, 50, 50],
            5:[21, 67, 43, 7, 30]
        }
    },
    435216: {
        'inverted': [1,3,4,6],
        'standing_stones': {'blue':[0,1], 'green':[4,6], 'white':[5,5]},
        'abandoned_shacks': {'blue':[6,1], 'green':[4,11], 'white':[4,2]},
        'clues':{
            3:[-1,45,-1,43,51],
            4:[-1,42,23,91,41],
            5:[42,46,96,34,11]
        }
    },
    436512: {
        'inverted': [1,2,5],
        'standing_stones': {'blue':[5,5], 'green':[6,4], 'white':[4,6]},
        'abandoned_shacks': {'blue':[3,1], 'green':[7,4], 'white':[7,6]},
        'clues':{
            3:[69,-1,31,72,-1],
            4:[69,2,80,-1,57,-1],
            5:[3,80,20,84,16]
        }
    },
    261435: {
        'inverted': [3,4,5,6],
        'standing_stones': {'blue':[3,10], 'green':[7,2], 'white':[1,11]},
        'abandoned_shacks': {'blue':[8,9], 'green':[8,7], 'white':[5,9]},
        'clues':{
            3:[30,45,-1,56,-1],
            4:[28,76,20,77,-1],
            5:[26,71,31,46,86]
        }
    },
    156324: {
        'inverted': [1,3,6],
        'standing_stones': {'blue':[0,1], 'green':[0,11], 'white':[2,5]},
        'abandoned_shacks': {'blue':[8,4], 'green':[6,9], 'white':[2,3]},
        'clues':{
            3:[28,-1,-1,85,8],
            4:[2,43,-1,52,42],
            5:[17,19,73,50,11]
        }
    }
}