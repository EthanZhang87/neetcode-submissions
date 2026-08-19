# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = head = ListNode() 

        carry = 0
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            if val1 + val2 + carry > 9:
                temp = carry
                carry = (val1 + val2 + carry) // 10
                head.val = (val1 + val2 + temp) - 10

            else:
                
                head.val = val1 + val2 + carry
                carry = 0

            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                head.next = ListNode()
                head = head.next            


        while l1:
            if l1.val + carry <= 9:
                head.next = ListNode()
                head = head.next
                head.val = l1.val + carry
                carry = 0
                
            else:
                temp = carry
                carry = (l1.val + carry) // 10
                head.next = ListNode()
                head = head.next
                head.val = (l1.val + temp) - 10
            l1 = l1.next
    

        while l2:
            if l2.val + carry <= 9:
                head.next = ListNode()
                head = head.next
                head.val = l2.val + carry
                carry = 0
                
            else:
                temp = carry
                carry = (l2.val + carry) // 10
                head.next = ListNode()
                head = head.next
                head.val = (l2.val + temp) - 10
            l2 = l2.next

        if carry != 0:
            head.next = ListNode(carry)
        
        return dummy        
        