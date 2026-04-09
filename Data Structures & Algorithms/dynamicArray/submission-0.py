class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self._capacity = capacity
            self.array = ["null"] * capacity
            self._n = 0


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self._n == self._capacity:
            self.resize()
        self.array[self._n] = n
        self._n += 1

    def popback(self) -> int:
        if self._n > 0:
            # soft delete the last element
            self._n -= 1
        # return the popped element
        return self.array[self._n]

    def resize(self) -> None:
        self._capacity *= 2
        array = [None] * self._capacity
        array[:self._n] = self.array[:self._n]
        self.array = array

    def getSize(self) -> int:
        return self._n
    
    def getCapacity(self) -> int:
        return self._capacity
