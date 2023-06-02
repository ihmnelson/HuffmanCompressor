from heapSort import heap_sort


class Character:
    character: str
    frequency: int

    def __init__(self, character: str, frequency: int):
        # Comment out assert below for encodeByWord
        # assert len(character) == 1 or character == 'END'

        self.character = character
        self.frequency = frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __repr__(self):
        return f'CHAR:\'{self.character}\':{self.frequency}'

    def jsoninator(self):
        return {
            'character': self.character,
            'frequency': self.frequency
        }
