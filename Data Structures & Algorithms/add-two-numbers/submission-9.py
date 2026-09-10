# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        carry = 0
        while l1 and l2:
            val = (l1.val + l2.val + carry)
            if val > 9:
                carry = 1
                dummy.next = ListNode(val % 10)
                
            else:
                carry = 0
                dummy.next = ListNode(val)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry
            if val > 9:
                carry = 1
                dummy.next = ListNode(val % 10)
            else:
                carry = 0
                dummy.next = ListNode(val)

       


            dummy = dummy.next
            l1 = l1.next

        while l2:

            val = l2.val + carry
            if val > 9:
                carry = 1
                dummy.next = ListNode(val % 10)
            else:
                carry = 0
                dummy.next = ListNode(val)

            dummy = dummy.next
            l2 = l2.next

        if carry:
            dummy.next = ListNode(1)
            


        return curr.next
            
      
        