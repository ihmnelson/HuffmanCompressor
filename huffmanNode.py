from character import Character


class Node:
    left = None
    right = None

    def __init__(self, char: Character = None, frequency=None, left=None, right=None):
        self.character = char.character if char else None
        self.frequency = frequency if frequency else (char.frequency if char else None)
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.character == other.character
        return self.frequency == other.frequency

    def __eq__(self, other):
        if self.frequency == other.frequency:
            return self.character < other.character
        return self.frequency < other.frequency

    def __repr__(self):
        return f'NODE:{self.frequency},[L<{self.left}>,R<{self.right}>]'
