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

        second = slow.next
        slow.next = None
     

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        

        

        while prev and dummy:
            temp = dummy.next
            dummy.next = prev
            temp2 = prev.next
            dummy.next.next = temp
            dummy = temp

            prev = temp2




        

        


        
    

        

        