class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)

        for i, v in enumerate(nums):
            if dic[v]:
                for x in dic[v]:
                    if abs(x - i) <= k:
                        return True

            dic[v].append(i)
        return False            
