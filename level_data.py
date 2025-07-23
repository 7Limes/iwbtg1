UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


LEVEL1 = {
    'meta': {
        'prev_level': LEFT,
        'next_level': RIGHT,
    },
    'objects': [
        [4, 0, 12, 21, 1],
        [5, 0, 13, 20, 2],
        [5, 10, 9, 2, 1],
        [0, 6, 6, 1, 1],
        [1, 6, 5, 1, 1],
        [2, 6, 4, 1, 1],
        [3, 6, 3, 1, 1],
        [5, 6, 7, 2, 1],
        [5, 12, 5, 3, 1]
    ]
}

LEVEL2 = {
    'meta': {
        'prev_level': LEFT,
        'next_level': RIGHT
    },
    'objects': [
        [5, -1, 12, 10, 3],
        [4, 8, 9, 3, 3]
    ]
}

LEVELS = [
    LEVEL1, LEVEL2
]