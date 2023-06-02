# In individual file cause it being in encodeByCharacter broke stuff
from character import Character
from huffmanNode import Node
from priorityQueue import PriorityQueue


class HuffmanTree:
    root: Node

    def __init__(self, char_data: [Character]):
        # Creating priority queue
        q = PriorityQueue(char_data)
        # other stuff
        index = 0
        while len(q) >= 2:
            # iteration stuff
            index += 1
            # real stuff
            z = Node()
            # set let
            left = q.pop_min()
            z.left = left  # if type(left) == Node else Node(left)
            # set right
            right = q.pop_min()
            z.right = right  # if type(right) == Node else Node(right)
            # other stuff
            z.frequency = z.left.frequency + z.right.frequency
            q.insert(z)

        self.root = q.pop()

