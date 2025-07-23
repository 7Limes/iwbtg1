from construct import Struct, Int8ub, Int8sb, Array, this
from copy import deepcopy
from level_data import LEVELS


OBJECT_KEYS = ['id', 'x', 'y', 'width', 'height']


LevelObjectStruct = Struct(
    'id' / Int8ub,
    'x' / Int8sb,
    'y' / Int8sb,
    'width' / Int8ub,
    'height' / Int8ub
)

LevelDataStruct = Struct(
    'meta' / Struct(
        'prev_level' / Int8ub,
        'next_level' / Int8ub,
    ),
    'object_count' / Int8ub,
    'objects' / Array(this.object_count, LevelObjectStruct)
)

LevelsStruct = Struct(
    'level_count' / Int8ub,
    'levels_list' / Array(this.level_count, LevelDataStruct)
)


def level_to_binary(level: dict):
    level_bytes = b''

    level_bytes = len(level['objects']).to_bytes(1)
    for level_object in level['objects']:
        level_bytes += bytes(level_object)
    return level_bytes


def format_level(level: dict):
    new_level = deepcopy(level)

    new_level['object_count'] = len(new_level['objects'])
    new_level['objects'] = [{k: v for k, v in zip(OBJECT_KEYS, o)} for o in new_level['objects']]
    
    return new_level


if __name__ == '__main__':
    formatted_levels = [format_level(l) for l in LEVELS]

    build_dict = {
        'level_count': len(LEVELS),
        'levels_list': formatted_levels
    }
    all_level_bytes = LevelsStruct.build(build_dict)

    with open('iwbtg/assets/levels.dat', 'wb') as f:
        f.write(all_level_bytes)
    
    print('Compiled level.dat.')