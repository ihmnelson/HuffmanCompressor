from heapSort import heap_sort


class PriorityQueue:
    def __init__(self, array=None):
        self.array: [] = array if array else []

    def __repr__(self):
        return self.array.__repr__()

    def __len__(self):
        return len(self.array)

    def insert(self, obj):
        self.array.append(obj)
        heap_sort(self.array)

    def pop(self):
        return self.array.pop()

    def pop_min(self):
        return self.array.pop(0)
