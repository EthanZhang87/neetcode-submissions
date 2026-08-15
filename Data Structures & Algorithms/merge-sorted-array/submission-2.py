class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n - 1
        j = m - 1
        e = m + n - 1

        while e >= 0:
            if j < 0:
                nums1[e] = nums2[i]
                i -= 1
                e -= 1
                continue
            elif i < 0:
                nums1[e] = nums1[j]
                e -= 1
                j -= 1
                continue 
                
            if nums1[j] > nums2[i]:
                nums1[e] = nums1[j]
                e -= 1
                j -= 1
            else:
                nums1[e] = nums2[i]
                e -= 1
                i -= 1



        


        
        