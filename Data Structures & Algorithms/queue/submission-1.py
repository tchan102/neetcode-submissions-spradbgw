class Deque:
    class Node:
        def __init__(self, v, l = None, r = None):
            self.v = v
            self.l = l
            self.r = r
    def __init__(self):
        self.left = None
        self.right = None
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        newNode = self.Node(value, self.right)
        if self.isEmpty():
            self.left = newNode
        else:
            self.right.r = newNode
        self.right = newNode
        self.length += 1

    def appendleft(self, value: int) -> None:
        newNode = self.Node(value, r = self.left)
        if self.isEmpty():
            self.right = newNode
        else:
            self.left.l = newNode
        self.left = newNode
        self.length += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        res = self.right.v
        if self.length == 1:
            self.left = None
            self.right = None
        else:
            prev = self.right.l
            prev.r = None
            self.right = prev
        self.length -= 1
        return res


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        res = self.left.v
        if self.length == 1:
            self.left = None
            self.right = None
        else:
            nxt = self.left.r
            nxt.l = None
            self.left = nxt
        self.length -= 1
        return res

