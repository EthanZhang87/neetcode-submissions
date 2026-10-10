class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    

    def remove(self, key):
        prevNode = self.cache[key].prev
        nextNode = self.cache[key].next
        prevNode.next, nextNode.prev = nextNode, prevNode

    def insert(self, key, val):
        newNode = Node(key, val)
        self.cache[key] = newNode
        prevNode, nextNode = self.right.prev, self.right
        prevNode.next = newNode
        nextNode.prev = newNode
        newNode.next = nextNode
        newNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.insert(key, self.cache[key].val)
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.insert(key, value)

        if len(self.cache) > self.capacity:
            lruKey = self.left.next.key
            self.remove(lruKey)
            del self.cache[lruKey]
            
            

        
        
