"""
Converts tiled map files into a level.dat file that can be read by the game.
"""

import os
import json
import re
from construct import Struct, Int8ub, Int8sb, Array, this
from collections import Counter


LEVELS_PATH = 'tiled/levels'
OUTPUT_PATH = 'iwbtg/assets/levels.dat'
LEVEL_JSON_REGEX = re.compile(r'level(\d+)\.json')

TILE_SIZE = 32
SCREEN_WIDTH = 20
SCREEN_HEIGHT = 15
DEFAULT_TILE_ID = 6

DIRECTION_LOOKUP = {
    'up': 0,
    'right': 1,
    'down': 2,
    'left': 3
}


LevelObjectStruct = Struct(
    'id' / Int8ub,
    'x' / Int8sb,
    'y' / Int8sb,
    'width' / Int8ub,
    'height' / Int8ub
)

LevelDataStruct = Struct(
    'meta' / Struct(
        'prev_direction' / Int8ub,
        'next_direction' / Int8ub,
    ),
    'object_count' / Int8ub,
    'objects' / Array(this.object_count, LevelObjectStruct)
)

LevelsStruct = Struct(
    'level_count' / Int8ub,
    'levels_list' / Array(this.level_count, LevelDataStruct)
)


def convert_level_json(level_json: dict) -> dict:
    properties = {}
    for property_data in level_json['properties']:
        properties[property_data['name']] = property_data['value']
    
    tile_map = level_json['layers'][0]['data']
    objects = level_json['layers'][1]['objects']

    converted_objects = []
    for obj in objects:
        obj_x = obj['x'] // TILE_SIZE
        obj_y = obj['y'] // TILE_SIZE
        obj_width = obj['width'] // TILE_SIZE
        obj_height = obj['height'] // TILE_SIZE

        area_ids = []
        for i in range(obj_y, obj_y+obj_height):
            for j in range(obj_x, obj_x+obj_width):
                if i < 0 or i >= SCREEN_HEIGHT or j < 0 or j >= SCREEN_WIDTH:
                    continue

                index = i * SCREEN_WIDTH + j
                area_ids.append(tile_map[index])

        if area_ids:
            most_common_tile_id = Counter(area_ids).most_common(1)[0][0]
            if most_common_tile_id == 0:
                most_common_tile_id = DEFAULT_TILE_ID
        else:
            most_common_tile_id = DEFAULT_TILE_ID

        converted_obj = {
            'id': most_common_tile_id-1,
            'x': obj_x,
            'y': obj_y,
            'width': obj_width,
            'height': obj_height
        }
        converted_objects.append(converted_obj)

    return {
        'meta': {
            'prev_direction': DIRECTION_LOOKUP[properties['prev_direction']],
            'next_direction': DIRECTION_LOOKUP[properties['next_direction']] 
        },
        'object_count': len(objects),
        'objects': converted_objects
    }


if __name__ == '__main__':
    sorted_level_files = []
    for file in os.listdir(LEVELS_PATH):
        file_path = LEVELS_PATH + '/' + file
        if not os.path.isfile(file_path):
            continue
            
        regex_match = LEVEL_JSON_REGEX.match(file)
        if not regex_match:
            continue

        level_number = int(regex_match.group(1))
        sorted_level_files.append((file_path, level_number))
    sorted_level_files.sort(key=lambda t: t[1])

    levels = []
    for file_path, _ in sorted_level_files:
        with open(file_path, 'r') as f:
            level_json = json.load(f)
            converted_level = convert_level_json(level_json)
            levels.append(converted_level)

    build_dict = {
        'level_count': len(levels),
        'levels_list': levels
    }
    all_level_bytes = LevelsStruct.build(build_dict)

    with open(OUTPUT_PATH, 'wb') as f:
        f.write(all_level_bytes)
    
    print(f'Compiled {len(levels)} levels totaling {len(all_level_bytes)} bytes.')