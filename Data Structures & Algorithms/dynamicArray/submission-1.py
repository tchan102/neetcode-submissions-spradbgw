class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.l = [None] * capacity
            self.capacity = capacity
            self.length = 0


    def get(self, i: int) -> int:
        if 0 <= i < self.capacity:
            return self.l[i]


    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.capacity:
            self.l[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.l[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.l[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        newL = [None] * self.capacity
        for k, v in enumerate(self.l):
            newL[k] = v
        self.l = newL

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
