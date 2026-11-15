class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next, self.right.prev = self.right, self.left
        self.left.prev, self.right.next = self.right, self.left
        self.size = 0
        
        

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False

        newNode = ListNode(value)
        first = self.left.next

        newNode.prev, newNode.next = self.left, first
        self.left.next, first.prev = newNode, newNode

        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        p = self.right.prev.prev
        p.next, self.right.prev = self.right, p
        self.size -= 1

        return True
        
        

    def Front(self) -> int:
        if self.size == 0:
            return -1

        return self.right.prev.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1

        return self.left.next.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()