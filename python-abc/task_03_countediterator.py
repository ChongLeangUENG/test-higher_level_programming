class CountedIterator:
    def __iter__(self):
        return self
    
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0
    
    def get_count(self):
        return self._count

    def __next__(self):
        item = next(self._iterator)
        self._count += 1
        return item
