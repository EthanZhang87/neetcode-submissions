class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.capacity = capacity
        self.length = 0

        self.right.prev, self.left.next = self.left, self.right
        
    def remove(self, key):
        prevNode = self.cache[key].prev
        nextNode = self.cache[key].next
        prevNode.next, nextNode.prev = nextNode, prevNode
        self.length -= 1
        del self.cache[key]
        


    def insert(self, key, val):
        prevNode = self.right.prev
        newNode = ListNode(key, val)
        newNode.prev = prevNode
        prevNode.next = newNode
        newNode.next = self.right
        self.right.prev = newNode
        self.cache[key] = newNode
        self.length += 1


    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache[key].val
            self.remove(key)
            self.insert(key, temp)
            return temp
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        elif self.length == self.capacity:
            node = self.left.next
            self.remove(node.key)
        
        self.insert(key, value)
    

        

        
