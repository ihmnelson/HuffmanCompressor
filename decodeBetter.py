import bitstring
from character import Character
import pickle

while True:
    folder = input('What folder would you like to uncompress? ')

    try:
        name = folder.split('_')[0]
        with open(f'{folder}/{name}COMPRESSED_BIN.bnr', 'rb') as f:
            # opening binary
            file_contents = f.read()
            bits = bitstring.Bits(bytes=file_contents)
            bintext = bits.bin

        with open(f'{folder}/{name}TREE.obj', 'rb') as f:
            tree = pickle.load(f)

        break
    except FileNotFoundError as e:
        print(f'The given folder couldn\'t be found (ERROR: {e})')

root = tree.root

print(root)
decodedString = ''
cur1sAnd0s = [*bintext]
counter = 0
curNode = root
while len(cur1sAnd0s) > 1:
    if type(curNode) == Character:
        if curNode.character == 'END':
            break
        decodedString += curNode.character
        curNode = root
        cur1sAnd0s = cur1sAnd0s[counter:]
        counter = 0
    else:
        if cur1sAnd0s[counter] == '0':
            curNode = curNode.left
        elif cur1sAnd0s[counter] == '1':
            curNode = curNode.right
        counter += 1

print(decodedString)
