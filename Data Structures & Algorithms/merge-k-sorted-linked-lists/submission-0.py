# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        heap = []
        for k,v in enumerate(lists):
            if v:
                heapq.heappush(heap, (v.val, k, v)) 

        dummy = head = ListNode(0)
        count = 0

        while heap:
            element = heapq.heappop(heap)
            head.next = element[2]
            head = head.next
            if element[2].next != None:
                heapq.heappush(heap, (element[2].next.val, count, element[2].next))
                count += 1

        return dummy.next
