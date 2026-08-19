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

        curr = head
        while curr:
            copy = old_to_new[curr]
            if curr.next:
                copy.next = old_to_new[curr.next]
            else:
                copy.next = None

            if curr.random:
                copy.random = old_to_new[curr.random]

            else:
                curr.random = None

            curr = curr.next

        return old_to_new[head]
        
