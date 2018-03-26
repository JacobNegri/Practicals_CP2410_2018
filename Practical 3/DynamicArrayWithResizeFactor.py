
from dynamic_array import DynamicArray

class DynamicArrayWithResizeFactor(DynamicArray):

    def __init__(self, resize_factor):
        super().__init__()
        self._resize_factor = resize_factor

    def append(self, obj):

        if self._n == self._capacity:
            self._resize(int(self._resize_factor * self._capacity) + 1)

        self._A[self._n] == obj
        self._n += 1


