"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        old_to_new = {}

        dummy = head

        while dummy:
            old_to_new[dummy] = Node(dummy.val)
            dummy = dummy.next

        dummy2 = curr = old_to_new[head]
        
        while head:
            if head.random:
                curr.random = old_to_new[head.random]
            else:
                curr.random = None
            head = head.next
            if head:
                curr.next = old_to_new[head]
            else:
                curr.next = None
            curr = curr.next

        return dummy2


        
