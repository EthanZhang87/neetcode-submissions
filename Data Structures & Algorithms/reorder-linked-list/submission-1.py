# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy = slow.next
        
        slow.next = None

        while dummy:
            temp = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = temp

        while prev and head:
            temp = head.next
            temp2 = prev.next
            head.next = prev
            head = head.next
            head.next = temp
            head = head.next
            prev = temp2

        

        
   



        

        


        
    

        

        