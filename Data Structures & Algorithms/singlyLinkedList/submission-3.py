class LinkedList:
    class Node:
        def __init__(self, val, nextnode = None):
            self.val = val
            self.next = nextnode
    
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if self.length > 0 and -1 < index < self.length:
            cur = self.head
            while index > 0:
                cur = cur.next
                index -= 1
            return cur.val
        return -1

    def insertHead(self, val: int) -> None:
        newNode = self.Node(val, self.head)
        self.head = newNode
        self.length += 1

    def insertTail(self, val: int) -> None:
        newNode = self.Node(val)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
        self.length += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.length: return False
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.length -= 1
        return True


    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur != None:
            res.append(cur.val)
            cur = cur.next
        return res
