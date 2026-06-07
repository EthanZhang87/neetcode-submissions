# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first, second = head, head

        while second and second.next:
            if second.next == first:
                return True
            else:
                first = first.next
                second = second.next.next

        return False