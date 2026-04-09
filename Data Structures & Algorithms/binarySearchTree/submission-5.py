class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key 
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        cur = self.root
        while cur != None:
            if key == cur.key:
                return cur.val
            elif key > cur.key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
        return -1


    def getMin(self) -> int:
        cur = self.findMin(self.root)
        return cur.val if cur else -1
    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val if cur else -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def removeHelper(self, curr, key):
        if curr == None:
            return None
        
        if key > curr.key:
            cur.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            cur.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
    def inorderTraversal(self, root, result):
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)

