#!/usr/bin/env python3

import collections
import os

from dragoonterminal.database import Pokemon


SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SCRIPT_DIR = os.path.join(SCRIPT_DIR, "dragoonterminal")
DATA_DIR = os.path.join(SCRIPT_DIR, 'Data')
IMAGES_DIR = os.path.join(SCRIPT_DIR, 'Images')
EXTRA_DIR = os.path.join(IMAGES_DIR, 'Extra')

region_info = collections.namedtuple('region_info', 'start end dir_name')
region_dict = {
    'logo': region_info(1, 2, 'I - Logos'),
    'spirit': region_info(3, 10, 'II - Spirits'),
    'character': region_info(11, 23, 'III - Characters'),
    'location': region_info(24, 25, 'IV - Locations'),
    'extra': region_info(0, 0, 'Extra')
}

g_pokemon_dict = None  # potential fathers for extra pokemon


def region_name_by_id(id):
    if not id:
        return 'extra'
    for name, region in region_dict.items():
        if region.start <= int(id) <= region.end:
            return name
    assert False, 'region_name_by_id({})'.format(id)


def make_a_pokemon(id, line):
    id = '{:03}'.format(id)
    line = line.strip().split()
    while len(line) < 4:  # add '' as the subtype if it is missing
        line.append('')
    name, threshold, main_type, subtype = line
    name = name.lower()
    threshold = float(threshold)
    region = region_name_by_id(id)
    dir_name = region_dict[region].dir_name
    path = os.path.join(IMAGES_DIR, dir_name, id + '.jpg')
    return Pokemon(id, name, region, path, main_type, subtype, threshold)


def load_pokemon(filename='dragoon.txt'):
    """Load everything but the images from the 'Extra' folder"""
    with open(os.path.join(DATA_DIR, filename)) as in_file:
        return [make_a_pokemon(i, line) for i, line in enumerate(in_file, 1)]


# TODO: uncomment this when all files become jpg
# def make_an_extra_pokemon(filename, in_ext='.jpg'):
#     name, ext = os.path.splitext(filename)
#     if ext.lower() == in_ext:
#         name = name.lower()
#         path = os.path.join(EXTRA_DIR, filename)
#         father = g_pokemon_dict.get(name.split('-')[0])
#         if father:
#             return Pokemon(None, name,
#                            father.get_region(), path,
#                            father.get_pkmn_type(),
#                            father.get_pkmn_type_secondary(),
#                            father.get_dark_threshold())
#         else:
#             return Pokemon(None, name, None, path, None, None, None)
#     assert False, 'Bad file extention: {} != {}'.format(ext, in_ext)


# def load_extra(image_dir=None):
#     """Load all the file names of the images in the Extra folder."""
#     filenames = os.listdir(image_dir or EXTRA_DIR)
#     return [make_an_extra_pokemon(filename) for filename in filenames]


# def load_all_pokemon():
#     global g_pokemon_dict
#     pokemon_list = load_pokemon()
#     g_pokemon_dict = {pokemon.get_name(): pokemon for pokemon in pokemon_list}
#     return pokemon_list + load_extra()


if __name__ == '__main__':
    pokemon_list = load_all_pokemon()
    pokemon_dict = {pokemon.get_name(): pokemon for pokemon in pokemon_list}
    print(len(pokemon_list), len(set(pokemon_list)), len(pokemon_dict))
    for i in (0, -1):
        pokemon = pokemon_list[i]
        print(pokemon.is_extra(), pokemon)
