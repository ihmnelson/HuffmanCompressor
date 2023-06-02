# import character
from huffmanTree import HuffmanTree
from huffmanNode import *
from heapSort import heap_sort
import os
import pathlib
import json
import time
import bitstring
import logging
import pickle


def get_translation(root) -> dict:
    ret_dict = {}
    get_translation_helper(root, ret_dict)
    return ret_dict


def get_translation_helper(root, ret: dict, cur_string=''):
    if root is None:
        return
    if type(root) == Character:
        ret[root.character] = cur_string
    else:
        get_translation_helper(root.left, ret, cur_string + '0')
        get_translation_helper(root.right, ret, cur_string + '1')


# Getting the text file
while True:
    file = input('What file would you like to compress? ')

    try:
        with open(file, 'r') as f:
            contents = f.read()
            name = pathlib.Path(file).stem
            break
    except FileNotFoundError as e:
        print(f'The given file couldn\'t be found (ERROR: {e})')

# logging
folderName = name + '_' + str(time.strftime("%H:%M:%S", time.localtime()))
os.mkdir(folderName)
logging.basicConfig(filename=f'{folderName}/log.log', encoding='utf-8', level=logging.DEBUG)

# Getting the contents as a list
contents_as_list = [*contents]

# Finding frequency
data: [Character] = []
for char in contents_as_list:
    foundChar = False
    for obj in data:
        if char == obj.character:
            foundChar = True
            obj.frequency += 1
    if not foundChar:
        data.append(Character(char, 1))

end_node = Character('END', 0)
data.append(end_node)\

# heapsort - unnecessary as heapsort is used in the queue, but for purpose of demonstration it's here as well
heap_sort(data)
logging.debug(f'Sorted characters and frequency: {data}')


tree = HuffmanTree(data)
root_node = tree.root
logging.debug(f'root_node: {root_node}')

with open(f'{folderName}/{name}TREE.obj', 'wb') as f:
    pickle.dump(tree, f)

# getting translation
translation_key = get_translation(root_node)
logging.debug(translation_key)

translation = ''
for char in contents_as_list:
    translation += translation_key[char]

# adding end character
translation += translation_key['END']

logging.debug(translation)
# saving

# All binary stuff
# Goal: 4 bytes for number of bits of data, rest for data
bint = int(translation, base=2)
barray = bint.to_bytes((bint.bit_length() + 7) // 8, "big")

with open(f'{folderName}/{name}COMPRESSED_BIN.bnr', 'wb') as f:
    bstring = bitstring.Bits(bin=f'0b{translation}')
    bstring.tofile(f)
